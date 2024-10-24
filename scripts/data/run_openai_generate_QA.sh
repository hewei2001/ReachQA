#! /bin/bash

# run:
# cd ReachQA/scripts
# bash run_openai_generate_QA.sh

MODEL="gpt-4o-2024-08-06"
API_KEY="put your api key here"
BASE_URL="put your base url here"

DATA_PATH="ReachQA/data/reachqa_train"

python ./openai_generate_QA.py \
    --model_name $MODEL \
    --api_key $API_KEY \
    --base_url $BASE_URL \
    --data_path $DATA_PATH \
    --num_instruction_per_plot 4 \
    --QA_type "Reasoning" \
    --num_workers 10

