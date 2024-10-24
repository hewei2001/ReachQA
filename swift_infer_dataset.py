import os
import json
import argparse
import glob
import torch
from swift.llm import (
    ModelType, get_lmdeploy_engine, get_default_template_type,
    get_template, inference_lmdeploy, get_vllm_engine, inference_vllm,
    get_model_tokenizer, inference
)
from swift.utils import seed_everything
from tqdm import tqdm


model_name_map = {
    'Qwen-VL-Chat': ModelType.qwen_vl_chat,
    'InternVL2-8B': ModelType.internvl2_8b,
    'DeepSeek-VL-1.3B-Chat': ModelType.deepseek_vl_1_3b_chat,
    'MiniCPM-Llama3-V-2_5': ModelType.minicpm_v_v2_5_chat,
    'LLaVA-1.6-Vicuna-13B': ModelType.llava1_6_vicuna_13b_instruct,
    'llama3-llava-next-8b-hf': ModelType.llama3_llava_next_8b_hf,
    "chartgemma": ModelType.paligemma_3b_pt_448,
    "llava-1.5-13b-hf": ModelType.llava1_5_13b_instruct
}

# TODO: paste your local path to the datasets
dataset_path_map = {
    'ReachQA': "ReachQA/data/reachqa_test",
    'ChartQA': "ReachQA/data/chartqa_test",
    'ChartX': "ReachQA/data/chartx",
    'ChartBench': "ReachQA/data/chartbench",
    'CharXiv': "ReachQA/data/charxiv",
    'MathVista': "ReachQA/data/mathvista",
    'Math-Vision': "ReachQA/data/math_v",
    "ReachQA-Reas": "ReachQA/data/reachqa_test",
    "CharXiv-Reas": "ReachQA/data/charxiv",
}

def load_datasets(dataset_names):
    all_datasets = []
    
    for name in dataset_names:
        if name not in ['ReachQA', 'ChartQA', 'ChartX', 'ChartBench', 'CharXiv', 'MathVista', 'Math-Vision']:
            raise ValueError(f"Dataset name '{name}' is not in the allowed choices.")
        
        dataset_path = dataset_path_map[name]
        data_file = os.path.join(dataset_path, 'data.json')

        with open(data_file, 'r') as file:
            dataset = json.load(file)        
        
        # Update image paths to full paths
        for item in dataset:
            item['image'] = os.path.join(dataset_path, item['image'])
        
        all_datasets.append(dataset)
    
    return all_datasets

def prepare_requests(datasets, model_type):
    requests = []
    
    for dataset in datasets:
        for item in dataset:
            if model_type in [ModelType.qwen_vl_chat, ModelType.llava1_6_vicuna_13b_instruct, \
                                ModelType.deepseek_vl_1_3b_chat, ModelType.llama3_llava_next_8b_hf, \
                                    ModelType.llava1_5_13b_instruct]:
                request = {
                    'query': f"<image>{item['question']} Let's think step by step.",
                    'images': [item['image']]
                }
            elif model_type in [ModelType.minicpm_v_v2_5_chat, ModelType.internvl2_8b, ModelType.paligemma_3b_pt_448]:
                request = {
                    'query': item['question'] + " Let's think step by step.",
                    'images': [item['image']]
                }
            else:
                raise ValueError(f"Unsupported model type: {model_type}")
            
            requests.append(request)
    return requests

def infer_requests(requests, infer_backend):
    # Set generation info
    generation_info = {  
        "do_sample": False,
        "max_new_tokens": 1024,
        # "max_num_batched_tokens": 4096,
        # "temperature": 0,
    }
    
    print(f"Running inference with {infer_backend} backend...")
    
    if infer_backend == 'lmdeploy':
        responses = inference_lmdeploy(lmdeploy_engine, template, requests, generation_info=generation_info, use_tqdm=True)
    elif infer_backend == 'vllm':
        responses = inference_vllm(vllm_engine, template, requests, generation_info=generation_info, use_tqdm=True)
    else:  # 'none'
        responses = []
        for request in tqdm(requests):
            query = request['query']
            response, _ = inference(model, template, query)
            responses.append({'response': response})

    return responses

def save_results(responses, datasets, dataset_names, output_folder, suffix):
    os.makedirs(output_folder, exist_ok=True)
    
    dataset_to_results = {name: [] for name in dataset_names}
    
    current_idx = 0
    for dataset_name, dataset in zip(dataset_names, datasets):
        dataset_length = len(dataset)
        dataset_responses = responses[current_idx:current_idx + dataset_length]

        for item, response in zip(dataset, dataset_responses):
            dataset_to_results[dataset_name].append({
                "question": item['question'],
                "answer": item['answer'],
                "split": item['split'],
                "prediction": response['response']
            })
        
        current_idx += dataset_length

    for dataset_name, results in dataset_to_results.items():
        output_file = os.path.join(output_folder, f"{model_name}-{suffix}-{dataset_name}.json")
        with open(output_file, 'w') as file:
            json.dump(results, file, indent=4)
        
        print(f"Results saved to {output_file}")
        
def arg_parser():
    parser = argparse.ArgumentParser(description="Run multimodal inference with different models.")
    parser.add_argument('--model_name', type=str, required=True, 
                        help='Name of the model to use (e.g., LLaVA-1.6-Vicuna-13B)')
    parser.add_argument('--model_id_or_path', type=str, default=None, 
                        help='Model ID or path for the specific model checkpoint')
    parser.add_argument('--datasets', type=str, required=True, 
                        help='Comma-separated list of datasets to use (e.g., ReachQA,ChartQA)')
    parser.add_argument('--output_folder', type=str, required=True, 
                        help='Folder to save the inference results')
    parser.add_argument('--suffix', type=str, default='', 
                        help='Suffix to append to the output filename')
    parser.add_argument('--infer_backend', type=str, choices=['lmdeploy', 'vllm', 'none'], required=True,
                        help='Inference backend to use (lmdeploy, vllm, or none)')
    parser.add_argument('--tp', type=int, default=None, 
                        help='Tensor parallelism level (used with lmdeploy)')
    return parser.parse_args()

def main():
    args = arg_parser()
    print(args)
    
    seed_everything(42)
    
    global model_name, model_type, model_id_or_path
    
    model_name = args.model_name
    if model_name not in model_name_map:
        raise ValueError(f"Unsupported model name: {args.model_name}")
    model_type = model_name_map[args.model_name]
    model_id_or_path = args.model_id_or_path

    # load model and template
    global template
    if args.infer_backend == 'lmdeploy':
        global lmdeploy_engine
        lmdeploy_engine = get_lmdeploy_engine(model_type, model_id_or_path=model_id_or_path, tp=args.tp)
        template_type = get_default_template_type(model_type)
        template = get_template(template_type, lmdeploy_engine.hf_tokenizer)
        lmdeploy_engine.generation_config.max_new_tokens = 1024

    elif args.infer_backend == 'vllm':
        global vllm_engine
        vllm_engine = get_vllm_engine(model_type, model_id_or_path=model_id_or_path)
        template_type = get_default_template_type(model_type)
        template = get_template(template_type, vllm_engine.hf_tokenizer)
        vllm_engine.generation_config.max_new_tokens = 1024

    else:  # 'none'
        global model, tokenizer
        model, tokenizer = get_model_tokenizer(model_type, torch.bfloat16, model_kwargs={'device_map': 'auto'})
        model.generation_config.max_new_tokens = 1024
        template_type = get_default_template_type(model_type)
        template = get_template(template_type, tokenizer)
        
    # Process datasets
    dataset_names = [name.strip() for name in args.datasets.split(',')]
    datasets = load_datasets(dataset_names)
    
    # Prepare requests and infer
    requests = prepare_requests(datasets, model_type)
    responses = infer_requests(requests, args.infer_backend)
    
    # Save results
    save_results(responses, datasets, dataset_names, args.output_folder, args.suffix)

if __name__ == "__main__":
    main()