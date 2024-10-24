import json
import os
import re
import shutil
import subprocess
from multiprocessing import Pool
import argparse

def batch_process_code(code_dir, image_dir, save_dir):
    files = os.listdir(code_dir)

    for file_name in files:
        if re.match(r"\d{5}\.py$", file_name):
            source_file_path = os.path.join(code_dir, file_name)
            target_file_path = os.path.join(save_dir, file_name.replace(".py", "_save.py"))

            with open(source_file_path, "r") as source_file:
                with open(target_file_path, "w") as target_file:
                    for line in source_file:
                        modified_line = re.sub(r'plt\.show\(\)', f'plt.savefig("{image_dir}{file_name.replace(".py", ".jpg")}", dpi=200)', line)
                        modified_line = re.sub(r'plt\.savefig\(.*?\)', f'plt.savefig("{image_dir}{file_name.replace(".py", ".jpg")}", dpi=200)', modified_line)
                        target_file.write(modified_line)


def execute_python_script(file_path):
    try:
        print(f"Executing {file_path}...")
        subprocess.run(["python3", file_path], check=True)
        print(f"{file_path} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {file_path}: {e}")


def execute_python_scripts(directory):
    python_files = [file for file in os.listdir(directory) if file.endswith("save.py")]
    file_paths = [os.path.join(directory, file) for file in python_files]

    with Pool(64) as pool:
        pool.map(execute_python_script, file_paths)


def update_metadata(jsonl_file, image_dir):
    with open(jsonl_file, "r") as f:
        lines = f.readlines()

    updated_metadata = []

    for line in lines:
        data = json.loads(line.strip())

        code_filename = os.path.basename(data["code"])
        image_path = os.path.join(image_dir, code_filename.replace(".py", ".jpg"))

        if os.path.exists(image_path):
            data["image"] = image_path
            updated_metadata.append(data)
        else:
            data["image"] = None
            continue

    with open(jsonl_file, "w") as f:
        for data in updated_metadata:
            f.write(json.dumps(data) + "\n")

    print("Metadata Updated.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process code and execute scripts.")
    
    parser.add_argument('--code_dir', type=str, default="./all_code/", help="Directory containing code files.")
    parser.add_argument('--image_dir', type=str, default="./all_images/", help="Directory to save images.")
    parser.add_argument('--info_file', type=str, default="./all_info.jsonl", help="Path to the info file.")
    parser.add_argument('--save_dir', type=str, default="./temp_code/", help="Temporary directory to save code files.")

    args = parser.parse_args()

    os.makedirs(args.save_dir, exist_ok=True)
    os.makedirs(args.image_dir, exist_ok=True)
    
    batch_process_code(args.code_dir, args.image_dir, args.save_dir)
    execute_python_scripts(args.save_dir)
    shutil.rmtree(args.save_dir)

    if os.path.isfile(args.info_file):
        update_metadata(args.info_file, args.image_dir)