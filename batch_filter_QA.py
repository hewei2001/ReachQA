import argparse
import json
import os
import re
from tqdm import tqdm

from lmdeploy import pipeline, GenerationConfig, TurbomindEngineConfig
from lmdeploy.vl import load_image


##############################################
Score_Prompt = """You are a visual question answering (VQA) data annotator. You task is to review the following chart and question, and determine if the answer is correct based on the information in the chart. You should carefully analyze the chart, taking into account all relevant data points, labels, and trends. Then, conduct an in-depth analysis to determine if there are any unreasonable or incorrect aspects in the figure, question or answer. 

Specifically, consider the following points:
1. Are the provided question and answer relevant to the chart? Can the answer be found in the chart?
2. Do the colors in the charts and questions correspond correctly? Are there instances where the colors are incorrectly referred to?
3. Do the data in the charts and questions correspond correctly? Are there any errors in the data or misalignment of information?
4. Is the provided answer correct? Are there any logical errors or unreasonable points?
5. Apart from the points listed above, is there anything else in this question and answer that doesn't make sense?

Here is the question and answer about the given chart:
Question: {question}
Answer: {answer}

You are asked to provide a short analysis and decide whether to keep the example. Your response should be in the format: 
Analysis: (your analysis) 
Decision: (yes/no)"""

##############################################

def extract_decision(input_string):
    match = re.search(r"Decision: (yes|no)", input_string, re.IGNORECASE)
    if match:
        return 1 if match.group(1).lower() == 'yes' else -1
    else:
        return 0


def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]
        

def filter_qa(
    pipe,
    gen_config,
    data_path,
    batch_size=100,
):
    full_image_path_list = []
    with open(os.path.join(data_path, "all_instruction_data.jsonl"), 'r') as file:
        instruction_data = [json.loads(line) for line in file]

    full_image_path_list = [os.path.join(data_path, data['image']) for data in instruction_data]
    
    message_list = []
    for data, img_url in zip(instruction_data, full_image_path_list):
        message = [
            {
                'role': 'user',
                'content': [
                    {'type': 'text', 'text': Score_Prompt.format(question=data['question'], answer=data['detail_answer'])},
                    {'type': 'image_url', 'image_url': {'url': img_url}}
                ]
            }
        ]
        message_list.append(message)
    
    total_batches = (len(message_list) + batch_size - 1) // batch_size
    
    print("Start filtering QA...")    
    all_outputs = []
    for batch_prompts in tqdm(batch(message_list, batch_size), total=total_batches, desc="Processing Batches"):
        outputs = pipe(prompts=batch_prompts, gen_config=gen_config)
        all_outputs.extend(outputs)

    # reload meta_data
    with open(os.path.join(data_path, "all_instruction_data.jsonl"), 'r') as file:
        instruction_data = [json.loads(line) for line in file]

    # Add rating to meta_data
    model_name = args.model_path.split("/")[-1]
    for item, output in zip(instruction_data, all_outputs):
        if 'keep' not in item:
            item['keep'] = {}
        item['keep'][model_name] = extract_decision(output.text)

    with open(os.path.join(data_path, "all_instruction_data.jsonl"), "w") as f:
        for item in instruction_data:
            f.write(json.dumps(item) + "\n")
            

def arg_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_path", type=str, default='./llava-v1.6-34b')
    parser.add_argument("--data_path", type=str, default="./data/reachqa_train")
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top_p", type=float, default=0.95)
    parser.add_argument("--num_gpus", type=int, default=4)
    parser.add_argument("--batch_size", type=int, default=100)

    return parser.parse_args()


if __name__ == "__main__":
    args = arg_parser()
    print(args)

    backend_config = TurbomindEngineConfig(
        tp=args.num_gpus,
        session_len=8192,
    )
    gen_config = GenerationConfig(
        top_p=args.top_p,
        temperature=args.temperature,
        max_new_tokens=1024,
    )
    
    pipe = pipeline(args.model_path, backend_config=backend_config)
    
    filter_qa(pipe, gen_config, args.data_path, args.batch_size)
    
