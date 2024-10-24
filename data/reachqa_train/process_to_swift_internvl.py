import json
import random
import os

def load_json_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def process_data(data, base_path):
    processed = []
    for iter in data:
        newdata = {
            "query": iter["question"] + " Let's think step by step.",
            "response": iter["answer"],
            "images": [os.path.join(base_path, iter["image"])]
        }
        processed.append(newdata)
    return processed

def save_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main(input_file, output_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data = load_data(input_file)

    processed_data = process_data(data, current_dir)
    random.shuffle(processed_data)
    save_data(output_file, processed_data)

if __name__ == "__main__":
    # Set your parameters here
    input_file = "instruction_data_20k.json"
    output_file = "instruction_data_20k_swift_internvl.json"
    
    # Execute the main function
    main(input_file, output_file)