import argparse
import os
import random
import re
import json
import signal

from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

import openai
from utils.openai_utils import create_chat_response_by_messages
from utils.chart_notes import get_chart_note

##############################################
Self_Instruct_Prompt_Data = """As a MatplotLib expert, you are asked to write a new Python plotting script. This script will be used to generate a type-specific chart with artificial data.

Here are the requirements:
1. There are several script examples from which you can draw inspiration, but try not to repeat patterns already shown in the examples to maximize diversity.
2. Use the Matplotlib library in Python for plotting. You can use auxiliary libraries such as Numpy, but make sure the code works!
3. The type of chart you need to plot is [{type}]. Therefore, everything you create must be adapted to fit this type of chart.
4. The topic of the chart can be anything you like, for example, [{topic1}], [{topic2}], etc.
5. Based on the given chart type and the topic you choose, you need to construct a suitable backstory, which should be reflected in the title, labels, legend, etc.
6. Based on the backstory, you need to construct contextual data inputs in the form of Python lists or Numpy arrays. Information contained in the data can be adapted as appropriate to fit the type of chart.
7. You must not use `random()` to construct the data, as it needs to be explicitly created regardless of your chart type and topic.
8. Be as imaginative and creative as possible in drawing the chart, both in terms of data and plotting details.

Here are three examples to consider:

```python
{demo1}
```

```python
{demo2}
```

```python
{demo3}
```

Now, let's take this task step by step. First, we have to plan out the title and backstory of the chart and create data based on the above."""


Self_Instruct_Prompt_Code = """You're doing great! Now, please complete the entire script by plotting a chart based on the data generated. Here are some highlighted requirements and notes.

Requirements:
1. If you find that the generated data is not appropriate while plotting the chart, modify it further as needed.
2. The information on the chart should be complete enough to be understandable, but avoid including the full backstory or too much text in the figure.
3. Avoid occlusion of visual elements. If necessary, automatically adjust the image layout before `plt.show()` using `tight_layout()`.
4. If the text in the chart is too long, find a way to make it all visible instead of overlapping. If the title is too long, you can break it into multiple lines.
5. Once again, be as imaginative and creative as possible in creating the details of the chart.
6. Above all, double-check to ensure the code works. Reduce unnecessary comments and focus on functionality.

{note}
Now, generate your final plotting script in a single python code block."""


Evol_Instruct_Prompt_Thought = """As a MatplotLib expert, you are asked to optimize a Python plotting script to make the plotted chart more complex. The script will be used to generate charts for a mathematical test, so you should made a little more challenging.

This is the code you need to optimize:
```python
{code}
```

Here's what I'd like you to do to optimize the chart: {direction}
Now, let's take this task step by step. First, please read the given code carefully and analyze the chart it draws. Then, think about your optimization ideas with the given directions.
In this step, you don't need to give the final code, only show the design ideas.
"""

Evol_Instruct_Prompt_Code = """You're doing great! Now, please implement the final optimized script based on the above design ideas combined with the original code.

Remember: 
1. Avoid visual elements that obscure each other, e.g., legends, labels. Automatically adjust the image layout before plt.show() via tight_layout() if necessary.
2. If the text in the chart is too long, find a way to make all the text show up instead of overlapping. If the title is too long, you can break it into multiple lines.
3. Be as imaginative and creative as possible in creating details of the chart, but don't make the chart redundant just to cope.
4. If you are adding a new plot, take care that the chart is complete with all the elements, such as labels, axes, legends, and colors, unless it is intended to be shared with the original chart.
5. If you are adding a new plot, carefully construct meaningful data and consider whether to give the new sub-plot a sub-title.
6. You must not use `random()` to construct the data, as it needs to be explicitly constructed regardless of your chart type and topic.
7. Above all, double-check to make sure the code works. Reduce unnecessary comments and focus on functionality.

Now, generate your optimized plotting script in a single python code block.
"""


Code_Fix_Prompt = """As a Python and Matplotlib expert, you have been asked to fix the following code. The error code is:
```python
{code}
```
The code reports the following error message when run: {error}

Please analyze the error first, and then provide the revised code within a single Python code block.
There should only be one Python code block in your response, containing the complete revised code."""

##############################################

# From ChartBench & ChartX, 10 major, 32 minor
Type_of_Chart = {
    "Line Charts": ["line chart", "line chart with data annotation", "line chart with error bar"],
    "Pie Charts": ["pie chart", "donut pie chart", "sector pie chart", "ring chart"],
    "Bar Charts": ["bar chart", "bar chart with data annotation", "stacked bar chart", "percentage bar chart", "horizontal bar chart"],
    "3D Bar Charts": ["3D bar chart", "stacked 3D bar chart", "percentage 3D bar chart"],
    "Node Charts": ["directed node chart", "undirected node chart"],
    "Radar Charts": ["radar chart", "radar chart with area filling"],
    "Area Charts": ["area chart", "stacked area chart"],
    "Box Charts": ["vertical box chart", "horizontal box chart"],
    "Scatter Charts": ["scatter chart", "scatter chart with smooth fitting", "3D scatter chart (bubble chart)"],
    "Specific Charts": ["heat map", "rose chart", "funnel chart", "waterfall chart", "histogram", "tree map"],
}

# From OneChart & ChartX, 36 topics
Topic_of_Chart = [
    "Business and Finance",
    "Healthcare and Health",
    "Science and Engineering",
    "Social Media and the Web",
    "Government and Public Policy",
    "Education and Academics",
    "Environment and Sustainability",
    "Retail and E-commerce",
    "Human Resources and Employee Management",
    "Agriculture and Food Production",
    "Energy and Utilities",
    "Transportation and Logistics",
    "Real Estate and Housing Market",
    "Manufacturing and Production",
    "Sports and Entertainment",
    "Social Sciences and Humanities",
    "Law and Legal Affairs",
    "Food and Beverage Industry",
    "History and Culture",
    "Society and Community",
    "Art and Design",
    "Travel and Exploration",
    "Religion and Spirituality",
    "Language and Communication",
    "Fashion and Style",
    "Music and Performance",
    "Film and Cinema",
    "Literature and Writing",
    "Architecture and Building",
    "Mathematics and Statistics",
    "Physics and Chemistry",
    "Biology and Life Sciences",
    "Astronomy and Space",
    "Computer Science and Information Technology",
    "Marketing and Advertising",
    "Futurism and Innovation",
    "Books and Publishing",
    "Artificial Intelligence and Robotics",
]

Evol_Direction = [
    "Increase the size of the input data or the number of data groups as appropriate so that it requires a higher level of mathematical understanding. Note if there is a sum requirement.",
    "Try changing or adding some visual elements to make visual effect better. The elements you add must make sense and not be redundant.",
    "Incorporate an overlay plot of a different type on the original chart. Use related but not identical data for the added plot.",
    "Extend an additional subplot of a different type beside the original chart (2 in total). Use related but not identical data for the added plot.",
]

##############################################

def post_process_model_response(response):
    if response is None:
        print("Drop out: empty response")
        return None

    code_blocks = extract_python_code_block(response)
    if len(code_blocks) != 1:
        print("Drop out: multiple code blocks found in the response")
        return None
    elif len(code_blocks[0].split("\n")) < 10 or len(code_blocks[0].split("\n")) > 150:
        print("Drop out: code block length out of range")
        return None
    else:
        return code_blocks[0]


def extract_python_code_block(s):
    import re
    pattern = r"(?i)```python(.*?)```"
    code_blocks = re.findall(pattern, s, re.DOTALL)

    if code_blocks == []:
        pattern = r"```(.*?)```"
        code_blocks = re.findall(pattern, s, re.DOTALL)

    code_blocks = [code_block.strip() for code_block in code_blocks]
    return code_blocks


def handler(signum, frame):
    # raise an exception when function execution timed out
    raise Exception("Function execution timed out.")


def simulate_code(code_to_run):
    import signal
    try:
        # set up signal handler for timeout
        signal.signal(signal.SIGALRM, handler)
        # set timeout to 2 second
        signal.alarm(2)

        # execute the code
        result = exec(code_to_run, globals())

        # release the lock before returning the result
        signal.alarm(0)
        return True, result

    except Exception as e:
        # return error if an exception occurs during execution
        signal.alarm(0)
        return False, str(e)


def read_files_with_pattern(data_path, pattern=r"\d{3}\.py$"):
    import os
    import re

    data = []
    files = os.listdir(data_path)

    for file in sorted(files):
        if re.match(pattern, file):
            file_path = os.path.join(data_path, file)
            with open(file_path, "r", encoding="utf-8") as f:
                data.append(f.read())

    return data


def save_files_with_pattern(data_path, data, meta, pattern=r"\d{5}\.py$"):
    import os
    import re
    
    os.makedirs(data_path, exist_ok=True)
    meta_file = os.path.join(os.path.dirname(data_path), "all_info.jsonl")

    files = [f for f in os.listdir(data_path) if re.match(pattern, f)]

    base_number = 0
    if files:
        numbers = [int(re.search(r"\d+", f).group()) for f in files]
        base_number = max(numbers)

    for idx, file_data in enumerate(data):
        save_number = str(base_number + idx + 1).zfill(5)
        file_name = f"{save_number}.py"
        file_path = os.path.join(data_path, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_data)
            
        meta_info = {
            "id": f"reachqa-train-plot-{save_number}",
            "code": f"all_code/{save_number}.py",
            "image": None,
            "level": meta[idx]["level"],
            "plot_model": meta[idx]["plot_model"],
            "major_chart_type": meta[idx]["major_chart_type"],
            "minor_chart_type": meta[idx]["minor_chart_type"],
        }

        with open(meta_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(meta_info, ensure_ascii=False) + "\n")

        print(f"Saved to {file_name}")

def generate_code_data(
    model,
    client,
    seed_data_path="./seed_tasks.jsonl",
    output_dir="./",
    num_data_to_generate=1000,
    num_demo_data=3,
    save_easy_data=True,
    request_batch_size=20,
    num_workers=5,
):
    # load the seed data
    seed_data = read_files_with_pattern(data_path=seed_data_path, pattern=r"\d{3}\.py$")
    print(f"Loaded {len(seed_data)} collected seed code")

    os.makedirs(output_dir, exist_ok=True)
    random.seed(42)

    # load existing generated data (if any, to avoid duplication)
    if os.path.exists(os.path.join(output_dir, "00001.py")):
        llm_generated_data = read_files_with_pattern(data_path=output_dir, pattern=r"\d{5}\.py$")
        print(f"Loaded {len(llm_generated_data)} llm-generated data")
    else:
        llm_generated_data = []

    # now let's generate new data!
    all_code = seed_data + llm_generated_data
    progress_bar = tqdm(total=num_data_to_generate)
    if llm_generated_data:
        progress_bar.update(len(llm_generated_data))

    # multithreaded code generation
    def process_code_generation(meta_info):
        ### Step 1: Self-Instruct
        print("\nCalling OpenAI for Self-Instruct-Data...")
        self_instruct_data_output = create_chat_response_by_messages(
            model=model,
            client=client,
            messages=meta_info["self_message"],
            max_tokens=8192,
            temperature=1.0,
            top_p=0.95,
        )
        meta_info["self_message"].extend([
            {"role": "assistant", "content": self_instruct_data_output},
            {"role": "user", "content": Self_Instruct_Prompt_Code.format(note=get_chart_note(meta_info["minor_chart_type"]))}
        ])
        print("\nCalling OpenAI for Self-Instruct-Code...")
        self_instruct_code_output = create_chat_response_by_messages(
            model=model,
            client=client,
            messages=meta_info["self_message"],
            max_tokens=8192,
            temperature=1.0,
            top_p=0.95,
        )

        ### Step 2: Evolution-Instruct
        self_code = post_process_model_response(self_instruct_code_output)
        if self_code is not None:
            meta_info["self_code"] = self_code
            meta_info["evol_message"] = [
                {"role": "system", "content": "You are a skilled MatplotLib expert."},
                {"role": "user", "content": Evol_Instruct_Prompt_Thought.format(code=self_code, direction=random.choice(Evol_Direction))},
            ]
        else:
            return None
        
        print("\nCalling OpenAI for Evol-Instruct-Thought...")
        evol_instruct_thought_output = create_chat_response_by_messages(
            model=model,
            client=client,
            messages=meta_info["evol_message"],
            max_tokens=8192,
            temperature=1.0,
            top_p=0.95,
        )
        meta_info["evol_message"].extend([
            {"role": "assistant", "content": evol_instruct_thought_output},
            {"role": "user", "content": Evol_Instruct_Prompt_Code}
        ])
        print("\nCalling OpenAI for Evol-Instruct-Code...")
        evol_instruct_code_output = create_chat_response_by_messages(
            model=model,
            client=client,
            messages=meta_info["evol_message"],
            max_tokens=8192,
            temperature=1.0,
            top_p=0.95,
        )
        evol_code = post_process_model_response(evol_instruct_code_output)
        if evol_code is not None:
            meta_info["evol_code"] = evol_code
        
        return meta_info

    # multithreaded code fix
    def fix_code(meta_info):
        ### Step 3: Filter with Execution
        print("\nCalling OpenAI for Code Fix...")
        fix_output = create_chat_response_by_messages(
            model=model,
            client=client,
            messages=[
                {"role": "system", "content": "You are a skilled Python and MatplotLib expert."},
                {"role": "user", "content": Code_Fix_Prompt.format(code=meta_info["final_code"], error=meta_info["error"])},
            ],
            max_tokens=8192,
            temperature=1.0,
            top_p=0.95,
        )
        
        fix_code = post_process_model_response(fix_output)
        if fix_code is not None:
            meta_info["final_code"] = fix_code
        
        return meta_info
    
    # Main loop for generating data
    while len(llm_generated_data) < num_data_to_generate:

        meta_info_list = []
        # construct the meta infomation for each data
        for _ in range(request_batch_size):
            demo_codes = random.sample(all_code, num_demo_data)  # sampling from the seed data + generated data
            major_chart_type = random.choice(list(Type_of_Chart.keys()))
            minor_chart_type = random.choice(Type_of_Chart[major_chart_type])
            select_topics = random.sample(Topic_of_Chart, 2)

            messages = [
                {"role": "system", "content": "You are a skilled MatplotLib expert."},
                {
                    "role": "user",
                    "content": Self_Instruct_Prompt_Data.format(
                        type=minor_chart_type,
                        topic1=select_topics[0],
                        topic2=select_topics[1],
                        demo1=demo_codes[0],
                        demo2=demo_codes[1],
                        demo3=demo_codes[2],
                    ),
                },
            ]
            meta_info_list.append(
                {"major_chart_type": major_chart_type, "minor_chart_type": minor_chart_type, "self_message": messages, "plot_model": model}
            )

        # Start the parallel processing
        meta_to_check_list = []
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = {executor.submit(process_code_generation, meta_info): meta_info for meta_info in meta_info_list}
            for future in tqdm(as_completed(futures), total=len(futures)):
                result = future.result()
                if result is not None:
                    if save_easy_data and "self_code" in result:
                        easy_item = result.copy()
                        easy_item["level"] = "Easy"
                        easy_item["final_code"] = easy_item["self_code"]
                        meta_to_check_list.append(easy_item)
                        
                    if "evol_code" in result:
                        hard_item = result.copy()
                        hard_item["level"] = "Hard"
                        hard_item["final_code"] = hard_item["evol_code"]
                        meta_to_check_list.append(hard_item)

        # Check the code with execution
        for meta in meta_to_check_list:
            success, error = simulate_code(meta["final_code"])
            if success:
                meta["success"] = True
            else:
                meta["success"] = False
                meta["error"] = error
        
        meta_to_save_list = [meta for meta in meta_to_check_list if meta["success"]]
        meta_to_check_list = [meta for meta in meta_to_check_list if not meta["success"]]
        
        # Start the parallel processing
        max_attempts = 2
        for _ in range(max_attempts):
            if len(meta_to_check_list) == 0:
                break
            
            meta_after_fix = []
            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                futures = {executor.submit(fix_code, meta_info): meta_info for meta_info in meta_to_check_list}
                for future in tqdm(as_completed(futures), total=len(futures)):
                    result = future.result()
                    meta_after_fix.append(result)
                    
            for meta in meta_after_fix:
                success, error = simulate_code(meta["final_code"])
                if success:
                    meta["success"] = True
                else:
                    meta["success"] = False
                    meta["error"] = error
            
            meta_to_save_list.extend([meta for meta in meta_after_fix if meta["success"]])
            meta_to_check_list = [meta for meta in meta_after_fix if not meta["success"]]

        code_to_save = [meta["final_code"] for meta in meta_to_save_list]
        llm_generated_data.extend(code_to_save)
        all_code.extend(code_to_save)
        progress_bar.update(len(code_to_save))
        
        print(f"For the batch_size of {request_batch_size}, kept {len(code_to_save)} code!")
        save_files_with_pattern(data_path=output_dir, data=code_to_save, meta=meta_to_save_list, pattern=r"\d{5}\.py$")


def arg_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_name", type=str, default="gpt-4o-2024-08-06")
    parser.add_argument("--api_key", type=str, default="key")
    parser.add_argument("--base_url", type=str, default="url")
    
    parser.add_argument("--output_dir", type=str, default="./data/reachqa_train/all_code")
    parser.add_argument("--seed_data_path", type=str, default="./data/reachqa_seed/code")
    parser.add_argument("--num_data_to_generate", type=int, default=1000)
    parser.add_argument("--num_demo_data", type=int, default=3)
    parser.add_argument("--save_easy_data", type=bool, default=True)

    parser.add_argument("--request_batch_size", type=int, default=20)
    parser.add_argument("--num_workers", type=int, default=5)

    return parser.parse_args()


if __name__ == "__main__":
    args = arg_parser()
    print(args)
    
    openai_client = openai.OpenAI(api_key=args.api_key, base_url=args.base_url)

    generate_code_data(
        model=args.model_name,
        client=openai_client,
        seed_data_path=args.seed_data_path,
        output_dir=args.output_dir,
        num_data_to_generate=args.num_data_to_generate,
        num_demo_data=args.num_demo_data,
        save_easy_data=args.save_easy_data,
        request_batch_size=args.request_batch_size,
        num_workers=args.num_workers,
    )
