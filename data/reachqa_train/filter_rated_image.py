import json
import os
import shutil
import numpy as np
from collections import Counter
import argparse


def read_jsonl(file_path):
    with open(file_path, "r") as file:
        return [json.loads(line) for line in file]


def save_jsonl(data, file_path):
    with open(file_path, "w") as file:
        for item in data:
            file.write(json.dumps(item) + "\n")


def renumber_and_move_files(data, start_id=1, waste=False):
    new_data = []
    for index, item in enumerate(data, start=start_id):
        new_id = f"reachqa-train-plot-{index:05}"
        old_image_path = item['image']
        old_code_path = item['code']
        
        if waste:
            new_image_path = os.path.join("waste_images", f"{index:05}.jpg")
            new_code_path = os.path.join("waste_code", f"{index:05}.py")
        else:
            new_image_path = os.path.join("images", f"{index:05}.jpg")
            new_code_path = os.path.join("code", f"{index:05}.py")
        
        # Move and rename files
        shutil.copy(old_image_path, new_image_path)
        shutil.copy(old_code_path, new_code_path)
        
        # Update item paths
        item['image'] = new_image_path
        item['code'] = new_code_path
        item['id'] = new_id
        new_data.append(item)
    return new_data


def calculate_stats(avg_ratings):
    average = np.mean(avg_ratings)
    median = np.median(avg_ratings)

    print(f"\nAverage Rating: {average:.2f}")
    print(f"Median Rating: {median:.2f}")
    
    rating_bins = Counter()

    for avg_rating in avg_ratings:
        bin_key = round(avg_rating * 2) / 2.0
        rating_bins[bin_key] += 1

    print("Rating Distribution:")
    for key in sorted(rating_bins.keys()):
        print(f"{key}: {rating_bins[key]}")
        
    return median


def main(data_dir):
    info_file = os.path.join(data_dir, "all_info.jsonl")
    
    data = read_jsonl(info_file)
    for item in data:
        if isinstance(item["rating"], dict):
            item["avg_rating"] = sum(item["rating"].values()) / len(item["rating"])
        elif isinstance(item["rating"], list):
            item["avg_rating"] = sum(item["rating"]) / len(item["rating"])

    avg_ratings = [item["avg_rating"] for item in data]
    median = calculate_stats(avg_ratings)

    high_rating = [item for item in data if item['avg_rating'] >= 3.75]
    low_rating = [item for item in data if item['avg_rating'] < 3.75]

    # Create directories for low rating files
    os.makedirs(os.path.join(data_dir, "waste_images"), exist_ok=True)
    os.makedirs(os.path.join(data_dir, "waste_code"), exist_ok=True)
    os.makedirs(os.path.join(data_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(data_dir, "code"), exist_ok=True)

    # Process low rating files
    low_rating = renumber_and_move_files(low_rating, waste=True)
        
    # Process high rating files
    high_rating = renumber_and_move_files(high_rating, waste=False)

    # Save new jsonl files
    save_jsonl(high_rating, os.path.join(data_dir, "plot_info.jsonl"))
    save_jsonl(low_rating, os.path.join(data_dir, "waste_info.jsonl"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter and process rated images and code files.")
    parser.add_argument('--data_dir', type=str, default="./", help="Directory containing data files.")

    args = parser.parse_args()
    main(args.data_dir)