import os
import json
import argparse


def count_negative_samples(data):
    """
    Count and print the number of samples with '-1' occurrences ranging from 0 to 4.
    """
    # Initialize a dictionary to count occurrences of '-1'
    count_dict = {i: 0 for i in range(5)}
    
    for item in data:
        # Count occurrences of -1
        negative_count = sum(1 for v in item['keep'].values() if v == -1)
        
        # Update the count if within range
        if negative_count in count_dict:
            count_dict[negative_count] += 1
    
    # Print the result
    for count, num_samples in count_dict.items():
        print(f"Number of samples with {count} occurrences of '-1': {num_samples}")


def filter_and_modify_data(data):
    """
    Filter samples based on the 'keep' field and modify 'data_id' to be sequential.
    Remove the 'keep' field and return the processed data.
    """
    # Sort data by plot_id
    data.sort(key=lambda x: x['plot_id'])
    
    filtered_data = []
    new_data_id = 1
    
    for item in data:
        # Count occurrences of -1
        negative_count = sum(1 for v in item['keep'].values() if v == -1)
        
        # Keep samples with fewer than 2 occurrences of -1
        if negative_count < 2:
            new_item = {
                "data_id": f"reachqa-train-{str(new_data_id).zfill(5)}",
                "plot_id": item["plot_id"],
                "image": item["image"],
                "code": item["code"],
                "plot_level": item["plot_level"],
                "plot_model": item["plot_model"],
                "major_chart_type": item["major_chart_type"],
                "minor_chart_type": item["minor_chart_type"],
                "QA_type": item["QA_type"],
                "QA_model": item["QA_model"],
                "question": item["question"],
                "detail_answer": item["detail_answer"],
                "concise_answer": item["concise_answer"],
            }

            new_data_id += 1
            filtered_data.append(new_item)
    
    return filtered_data


def main(data_dir):
    # Set input and output file names
    input_file = os.path.join(data_dir, 'all_instruction_data_20k.jsonl')
    output_file = os.path.join(data_dir, 'instruction_data_20k.json')
    
    with open(input_file, 'r') as f:
        data = [json.loads(line) for line in f]

    # Print the count of '-1' occurrences
    count_negative_samples(data)
    
    # Filter and modify data
    modified_data = filter_and_modify_data(data)
    
    # Save the processed data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(modified_data, f, indent=4)

    print(f"Processing complete. Results saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter and process rated QA data.")
    parser.add_argument('--data_dir', type=str, default="./", help="Directory containing data files.")

    args = parser.parse_args()
    main(args.data_dir)