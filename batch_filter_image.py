import argparse
import json
import os
import re
from tqdm import tqdm

from lmdeploy import pipeline, GenerationConfig, TurbomindEngineConfig
from lmdeploy.vl import load_image


##############################################
Score_Prompt = """You are a strict MatplotLib plotter and have been asked to evaluate the given chart. Rate the chart from 1 to 5 based on these criteria: 

**1 point**: This chart is the poorest in quality and fails to accurately represent any relevant data. It is characterized by a complete breakdown in visual representation; elements are cluttered, text heavily overlaps, legend is missing, or large areas are left blank, making the chart unreadable. The design shows no understanding of effective data visualization practices.
**2 points**: The chart displays incorrect or irrelevant visual elements, with significant inaccuracies that misrepresent the data. The layout suffers from clutter, substantial overlapping of text and other visual elements, such as the legend or labels, and poorly designed axes that result in uneven distribution, severely impeding accurate interpretation.
**3 points**: This chart represents some correct data points but makes basic errors in visual representation. It may use misleading scales, inappropriate chart types, omit key data. Visual clutter and overlapping elements, such as text obscuring parts of the chart or sub-diagrams overlapping each other, detract from the chart's clarity and readability.
**4 points**: The chart accurately represents most of the major data points and important details of the dataset. Minor visual errors exist, such as slight occlusions of text or sub-optimal positioning of elements like legends or labels, but these do not significantly affect the overall accuracy or readability. The chart demonstrates a good understanding of effective visualization techniques but could still be improved in terms of visual layout and the balance of details.
**5 points**: This is an exemplary chart that perfectly encapsulates all critical data points and relationships with outstanding visual clarity and no occlusions. It demonstrates a thorough understanding of data visualization techniques, making excellent use of space and visual elements. The chart is informative, clear, engaging, and free from any visual errors.

Score the chart on this scale, providing a short analysis and a single value. Your response should be in the format: 
Analysis: (your analysis) 
Rating: (int)"""

##############################################

def extract_rating(input_string):
    match = re.search(r"Rating: ([1-5])", input_string)
    if match:
        return int(match.group(1))  # Find the first match value
    else:
        return 0


def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]
        

def filter_images(
    pipe,
    gen_config,
    data_path,
    batch_size=100,
):
    meta_data = []
    full_image_path_list = []
    with open(os.path.join(data_path, "all_info.jsonl"), 'r') as file:
        for line in file:
            item = json.loads(line.strip())
            meta_data.append(item)

    full_image_path_list = [os.path.join(data_path, data['image']) for data in meta_data]

    prompts = [(Score_Prompt, load_image(img_url)) for img_url in full_image_path_list]
    total_batches = (len(prompts) + batch_size - 1) // batch_size
    
    print("Start filtering images...")    
    all_outputs = []
    for batch_prompts in tqdm(batch(prompts, batch_size), total=total_batches, desc="Processing Batches"):
        outputs = pipe(batch_prompts, gen_config=gen_config)
        all_outputs.extend(outputs)

    # reload meta_data
    meta_data = []
    with open(os.path.join(data_path, "all_info.jsonl"), 'r') as file:
        for line in file:
            item = json.loads(line.strip())
            meta_data.append(item)

    # Add rating to meta_data
    model_name = args.model_path.split("/")[-1]
    for item, output in zip(meta_data, all_outputs):
        if 'rating' not in item:
            item['rating'] = {}
        item['rating'][model_name] = extract_rating(output.text)

    with open(os.path.join(data_path, "all_info.jsonl"), "w") as f:
        for item in meta_data:
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
    
    filter_images(pipe, gen_config, args.data_path, args.batch_size)
    
