import argparse
from datetime import datetime
import os
import re
import json
import pandas as pd

import openai
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from utils.openai_utils import create_json_mode_chat_response_by_messages, create_chat_response_by_messages

##############################################
Answer_Judge_Prompt = """Compare the ground truth with the prediction from AI model and determine if the prediction is correct. The question is about an image, which we have not given here. You need to determine whether the model's prediction is consistent with the ground truth. No points will be awarded for wrong answers, over answers or under answers. The reasoning process in the prediction does not need to be considered too much, you only need to determine if the final answer is consistent. There are times when the answer may have a different form of expression and some variation is acceptable.

## Question: {question}
## Ground Truth: {answer}
## Prediction: {prediction}

Now, let's take a analysis and then provide your judgement. Your response must follow the format below:
Analysis: (analyze the correctness briefly) 
Correctness: (Yes or No)"""


##############################################

def post_process_model_response(response):
    # Regular expression to match the rewritten answer with case insensitivity
    match = re.search(r"Correctness:\s*(.*)", response, re.IGNORECASE | re.DOTALL)
    
    if match:
        answer_string = match.group(1).strip()
        if "yes" in answer_string.lower():
            return 1
        elif "no" in answer_string.lower():
            return 0
        else:
            return -1
    else:
        print("Failed to extract the correctness")
        return -1
    

def load_swift_outputs(data_dir):
    with open(data_dir, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        item["correctness"] = -1  # Initialize correctness
    print(f"Loaded {len(data)} records from {data_dir}")
    return data


def load_vlmevalkit_outputs(data_dir):
    # List all .xlsx files in the directory
    xlsx_files = [f for f in os.listdir(data_dir) if f.endswith('.xlsx')]
    if len(xlsx_files) != 1:
        raise ValueError(f"Expected one .xlsx file in {data_dir}, but found {len(xlsx_files)}.")

    data_path = os.path.join(data_dir, xlsx_files[0])
    df = pd.read_excel(data_path, usecols=["index", "question", "answer", "prediction"])
    data = df.to_dict(orient="records")
    for item in data:
        item["correctness"] = -1  # Initialize correctness
    print(f"Loaded {len(data)} records from {data_path}")
    return data


def load_llms_eval_outputs(data_dir):
    json_file = os.path.join(data_dir, 'chartqa.json')

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    logs = data.get("logs", [])
    extracted_data = []

    for log in logs:
        doc = log.get("doc", {})
        resps = log.get("resps", [[]])
        prediction = resps[0][0] if resps and resps[0] else ""

        extracted_data.append({
            "index": log.get("doc_id", 0),
            "question": doc.get("question", ""),
            "answer": doc.get("answer", ""),
            "prediction": prediction,
            "correctness": -1  # Initialize correctness
        })

    print(f"Loaded {len(extracted_data)} records from {json_file}")
    return extracted_data


def llm_evaluation(
    model,
    client,
    data_dir,
    data_format,
    output_file,
    num_workers
):
    # 1. load data
    if data_format == "vlmevalkit":
        data = load_vlmevalkit_outputs(data_dir)
    elif data_format == "llms_eval":
        data = load_llms_eval_outputs(data_dir)
    elif data_format == "swift":
        data = load_swift_outputs(data_dir)
    else:
        raise ValueError(f"Unsupported data format: {data_format}")

    # 2. start evaluation
    def evaluation(item):
        eval_messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": Answer_Judge_Prompt.format(
                    question=item["question"],
                    answer=item["answer"],
                    prediction=item["prediction"],
                ),
            },
        ]
        
        ### Call LLM
        print("\nCalling OpenAI for Judge...")
        output = create_chat_response_by_messages(
            model=model,
            client=client,
            messages=eval_messages,
            max_tokens=4096,
            temperature=0,
            top_p=0.95,
        )
        item['output'] = output
        
        item["correctness"] = post_process_model_response(output)
        return item

    eval_results = []

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(evaluation, item): item for item in data}
    
        for future in tqdm(as_completed(futures), total=len(futures)):
            new_item = future.result()
            eval_results.append(new_item)
    
    # 3. post process
    correct_count = 0
    split_correct_counts = {}  # Dictionary to store correct counts for each Split
    split_total_counts = {}  # Dictionary to store total counts for each Split

    for item in eval_results:
        # Get the split name for the current record
        correctness = item["correctness"]
        split = item["split"]
        
        # Update counts for the current split
        if split not in split_correct_counts:
            split_correct_counts[split] = 0
            split_total_counts[split] = 0

        if correctness == 1:
            split_correct_counts[split] += 1
        split_total_counts[split] += 1

        # Update the overall correct count
        correct_count += 1 if correctness == 1 else 0

    # 4. calculate total score
    total_count = len(data)
    accuracy = 100 * correct_count / total_count if total_count > 0 else 0

    # Print total accuracy
    print(f"total: {total_count}\tacc: {accuracy:.2f}")

    # Print accuracy for each split
    for split_name, total in split_total_counts.items():
        split_accuracy = 100 * split_correct_counts[split_name] / total if total > 0 else 0
        print(f"{split_name}: {total}\tacc: {split_accuracy:.2f}")

    # 5. save results
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Results saved to {output_file}")


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, default="gpt-4-turbo-2024-04-09")
    
    parser.add_argument(
        "--data_dir", type=str, default=""
    )
    parser.add_argument("--data_format", type=str, choices=["vlmevalkit", "llms_eval", "swift"], default="swift")
    parser.add_argument("--num_workers", type=int, default=5)

    return parser.parse_args()


if __name__ == "__main__":
    args = arg_parser()
    print(args)
    current_time = datetime.now()
    formatted_time_for_filename = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    
    
    openai_key = "key"
    openai_client = openai.OpenAI(api_key=openai_key, base_url="url")

    filename = os.path.basename(args.data_dir)
    filename = os.path.splitext(filename)[0]

    if args.data_format == "swift":
        output_file = args.data_dir
    else:
        output_file = os.path.join(args.output_dir, f"Eval-{args.output_suffix}.json")

    llm_evaluation(
        model=args.model_name,
        client=openai_client,
        data_dir=args.data_dir,
        data_format=args.data_format,
        output_file=output_file,
        num_workers=args.num_workers,
    )