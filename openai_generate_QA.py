import argparse
import json
import os
import regex as re

import openai
from concurrent.futures import ThreadPoolExecutor, as_completed
from rouge_score import rouge_scorer
from tqdm import tqdm
from utils.openai_utils import create_chat_response_by_messages, create_json_mode_chat_response_by_messages


##############################################
Gen_Reasoning_Q = """You are both an expert Matplotlib plotter and a professional maths teacher. Now, you are asked to generate a mathematical reasoning question about a given chart. This chart and question will be used as a question on this year's college admissions examination. As a question writer, you need to ensure that the question is challenging yet fair, testing the student's ability to analyze data, interpret trends, and apply mathematical concepts.

First, please read the following plotting script in Python, try to visualize the figure in your mind and understand the meaning of the chart. After you've analyzed this chart, we'll start generating the associated question.

Here are some tips for you:
1. The plotting script (including the code itself, data mapping and labels) is absolutely correct, and you can trust it completely.
2. The question needs to be based on the chart type, chart topic, and the given data. It can relate to the chart as a whole or to localized details, so you need to look closely.
3. The question should be challenging, requiring visual observation skills and mathematical reasoning skills. So, you need to have a deep understanding of the chart.
4. If there is no data annotation in the figure, try not to generate questions that require too much numerical recognition to reduce inconsistent answers due to visual errors.
5. If some numerical recognition is needed, choose distinguishable colors, lines, heights, and other features that make it easy to estimate without data annotation.
6. You don't need to describe what the chart shows in the question text, including values, labels, etc. This can be left to the student to recognize.

Here is the plotting script:
```python
{code}
```

Now, please generate 4 questions at a time, each of which needs to look at a different aspect of the chart.
Your output needs to follow this JSON format, and no other text should be included:
{{"question_list": ["<the question you generate>"]}}
"""

Gen_Reasoning_A = """You are both a Matplotlib graphing expert and a professional math teacher. Now, you have been asked to generate an answer to a given chart and question. This chart and question will be used as a question on this year's college admissions examination. As the answer writer, you need to ensure that the answer is correct, detailed, and educational.

First, please read the following plotting script in Python, try to visualize the figure in your mind and understand the meaning of the chart. After you've analyzed this chart, we'll start generating the answer.

Here is the plotting script:
```python
{code}
```

Here are some tips for you:
1. First and foremost, the answer needs to be based on the chart information.
2. In the answer, you will also need to solve the question step-by-step, including reasoning steps and recognition steps (but keep concise).
3. You need to explicitly involve a final answer; the type of answer can be a certain number, a noun, or Yes/No, etc.
4. The answer should contain multiple reasoning or calculation steps and be presented in an understandable and educational paragraph.
5. NEVER include any information relating to the Python script in the answer text, as students will ONLY have access to the plotted figure.

Here is the question:
{question}

Now, you can start to generate the answer. Your output needs to follow this JSON format, and no other text included:
{{"analysis": "<your analysis about the scirpt and question>", "answer": "<your step-by-step answer in a string>"}}
"""

##############################################

Gen_Recognizing_Q = """You are both an expert Matplotlib plotter and a professional maths teacher. Now, you are asked to generate a recognition-oriented question about a given chart. This chart and question will be used as a question on this year's elementary math examination to test students' ability to read charts.

First, please read the following plotting script in Python, try to visualize the figure in your mind and understand the meaning of the chart. After you've analyzed this chart, we'll start generating the associated question.

Here are some tips for you:
1. The plotting script (including the code itself, data mapping, and labels) is absolutely correct and you can trust it completely.
2. Descriptive questions are questions that can be answered based on basic chart information, such as titles, labels, tick marks, colors, etc.
3. The generated Q\&A needs to be based on the chart type and data. It should be answerable through visual observation.
4. If there is no data annotation in the figure, try not to generate questions that require too many numerical recognitions to reduce inconsistent answers due to visual errors.
5. If some numerical recognition is needed, choose distinguishable colors, lines, heights, and other features that make it easy to estimate without data annotation.
6. You don't need to describe the content of the figure in the question text. This can be left for students to think about.
7. This question needs to explicitly involve a final answer; the type of answer can be a certain number, a noun, or Yes/No, etc.
8. NEVER include any information relating to the Python script in the question or answer, as students will ONLY have access to the plotted figure.

Here are some examples of recognition-oriented questions:
- How many colors are used in the chart? How many city categories are in the chart?
- What's the leftmost value of the bar in China? And what is the value of the bar next to it?
- For the subplot at row 2 and column 1, what is the minimum value of the solid line?
- Which name does the second-largest sector represent? What is its value?
- Does the blue triangle in the chart represent a higher value than the red circle?
    
Here is the plotting script:
```python
{code}
```

Now, please generate 4 questions at a time, each of which needs to look at a different aspect of the chart.
Your output needs to follow this JSON format, and no other text should be included:
{{"question_list": ["<the question you generate>"]}}
"""

Gen_Recognizing_A = """You are both a Matplotlib graphing expert and a professional math teacher. Now, you have been asked to generate an answer to a given chart and question. This chart and question will be used as a question on this year's elementary math examination to test students' ability to read charts. As the answer writer, you need to ensure that the answer is correct, detailed, and educational.

First, please read the following plotting script in Python, try to visualize the figure in your mind and understand the meaning of the chart. After you've analyzed this chart, we'll start generating the answer.

Here is the plotting script:
```python
{code}
```

Here are some tips for you to generate the answer:
1. First and foremost, the answer needs to be based on the chart information.
2. In the answer, you will also need to solve the question step-by-step, including reasoning steps and recognition steps (but keep concise).
3. You need to explicitly involve a final answer; the type of answer can be a certain number, a noun, or Yes/No, etc.
4. The answer should contain multiple steps and be presented in an understandable and educational paragraph.
5. NEVER include any information relating to the Python script in the answer text, as students will ONLY have access to the plotted figure.

Here is the question:
{question}

Now, you can start to generate the answer. Your output needs to follow this JSON format, and no other text included:
{{"analysis": "<your analysis about the scirpt and question>", "answer": "<your step-by-step answer in a string>"}}
"""

##############################################

def extract_and_validate_json(input_str):
    # Use a regular expression to extract the JSON substring
    json_pattern = r'\{(?:[^{}]|(?R))*\}'
    json_match = re.search(json_pattern, input_str, re.DOTALL)
    
    if json_match:
        json_str = json_match.group(0)
        json_str = json_str.replace('\\', '\\\\')
        json_str = json_str.replace('\n', ' ').replace('\r', ' ')
        try:
            # Convert the JSON string to a dictionary
            temp_dict = json.loads(json_str)

            # Validate if the dictionary contains the required keys
            if 'question_list' in temp_dict:
                if isinstance(temp_dict['question_list'], list):
                    return temp_dict
                elif not isinstance(temp_dict['question_list'], str):
                    print("Invalid response format. The 'question_list' must be a list of strings.")
                    return None
                
            else if 'analysis' in temp_dict and 'answer' in temp_dict:
                return temp_dict
            
            else:
                print("Invalid response format. The response does not contain all 3 required keys.")
                return None
            
        except json.JSONDecodeError:
            print("Failed to decode JSON.")
            return None
    else:
        print("No JSON found in the input string.")
        return None


def generate_instruction_data(
    model,
    client,
    data_path,
    QA_type="Reasoning",
    num_workers=5,
    num_instruction_per_plot=3,
):    
    scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=False)
    output_file_path = os.path.join(data_path, f"all_instruction_data.jsonl")
    
    # Load existing data if available to find the last processed plot
    last_processed_plot_id = None
    if os.path.exists(output_file_path) and os.path.getsize(output_file_path) > 0:
        with open(output_file_path, "r") as f:
            existing_data = [json.loads(line) for line in f]
        if existing_data:
            last_processed_plot_id = max(existing_data, key=lambda x: x["plot_id"])["plot_id"]

    # load meta data
    with open(os.path.join(data_path, "plot_info.jsonl"), "r") as f:
        meta_data = [json.loads(line) for line in f]
        
    print(f"Loaded {len(meta_data)} collected plot(s)")
    
    # Skip already processed plots
    start_index = 0
    if last_processed_plot_id:
        for index, plot in enumerate(meta_data):
            if plot["id"] == last_processed_plot_id:
                start_index = index + 1
                break
    
    print(f"Skipped {start_index} processed plot(s)")
    def process_plot(plot, question_template, answer_template):
        code_file_path = os.path.join(data_path, plot["code"])
        with open(code_file_path, "r") as f:
            code = f.read()

        ### Call LLM to generate questions
        print("\nCalling OpenAI for Generate Questions...")
        question_dict_string = create_json_mode_chat_response_by_messages(
            model=model,
            client=client,
            messages=[
                {"role": "user", "content": question_template.format(code=code)},
            ],
            max_tokens=8192,
            temperature=1.0,
            top_p=0.95,
        )
        
        question_dict = extract_and_validate_json(question_dict_string) 
        question_list = question_dict.get("question_list", []) if question_dict else []

        ### Call LLM to generate answers
        answer_list = []
        print("\nCalling OpenAI for Generate Answers...")
        for question in question_list:
            answer_dict_string = create_json_mode_chat_response_by_messages(
                model=model,
                client=client,
                messages=[
                    {"role": "user", "content": answer_template.format(code=code, question=question)},
                ],
                max_tokens=8192,
                temperature=1.0,
                top_p=0.95,
            )
            answer_dict = extract_and_validate_json(answer_dict_string)
            if answer_dict is not None:
                answer_list.append(answer_dict["answer"])
            else:
                print(f"Warning: extract_and_validate_json returned None for answer_dict_string: {answer_dict_string}")
                question_list.append("")
        
        ### Filter with ROUGE-L
        new_instructions = []
        for (question, answer) in zip(question_list, answer_list):
            if answer == "":
                continue
            new_dict = {
                "question": question,
                "answer": answer,
            }
            is_duplicate = False
            for existing in new_instructions:
                if existing is None:
                    continue
                score = scorer.score(new_dict.get("question", ""), existing.get("question", ""))
                if score["rougeL"].fmeasure > 0.7:
                    is_duplicate = True
                    print(f"Duplicate instruction found: {new_dict['question']}")
                    break
            if not is_duplicate:
                new_instructions.append(new_dict)

        return new_instructions, plot

    question_template = Gen_Reasoning_Q if QA_type == "Reasoning" else Gen_Recognizing_Q
    answer_template = Gen_Reasoning_A if QA_type == "Reasoning" else Gen_Recognizing_A

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = {
            executor.submit(process_plot, plot, question_template, answer_template): plot
            for plot in meta_data[start_index:]
        }
        
        # Open the file in append mode
        with open(output_file_path, "a") as f:
            for future in tqdm(as_completed(futures), total=len(futures)):
                new_instructions, plot = future.result()
                for instruction in new_instructions:
                    sample = {
                        "plot_id": plot["id"],
                        "image": plot["image"],
                        "code": plot["code"],
                        "plot_level": plot["level"],
                        "plot_model": plot["plot_model"],
                        "major_chart_type": plot["major_chart_type"],
                        "minor_chart_type": plot["minor_chart_type"],
                        "QA_type": QA_type,
                        "QA_model": model,
                        "question": instruction["question"],
                        "answer": instruction["answer"],
                    }
                    f.write(json.dumps(sample) + "\n")
                

def arg_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_name", type=str, default="gpt-4-turbo-2024-04-09")
    parser.add_argument("--api_key", type=str, default="key")
    parser.add_argument("--base_url", type=str, default="url")
    
    parser.add_argument("--data_path", type=str, default="./data/reachqa_train")
    parser.add_argument("--num_instruction_per_plot", type=int, default=3)
    parser.add_argument("--QA_type", type=str, default="Reasoning", choices=["Reasoning", "Recognizing"])
    parser.add_argument("--num_workers", type=int, default=5)
    
    return parser.parse_args()


if __name__ == "__main__":
    args = arg_parser()
    print(args)

    openai_client = openai.OpenAI(api_key=args.api_key, base_url=args.base_url)

    generate_instruction_data(
        model=args.model_name,
        client=openai_client,
        data_path=args.data_path,
        QA_type=args.QA_type,
        num_workers=args.num_workers,
        num_instruction_per_plot=args.num_instruction_per_plot,
    )

