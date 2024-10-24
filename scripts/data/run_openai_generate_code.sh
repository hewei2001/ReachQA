#! /bin/bash

# run:
# cd ReachQA/scripts
# bash ./run_openai_generate_code.sh

MODEL="gpt-4o-2024-08-06"
API_KEY="put your api key here"
BASE_URL="put your base url here"

OUTPUT_PATH="ReachQA/data/reachqa_train/all_code"
SEED_PATH="ReachQA/data/reachqa_seed/code"

python ./openai_generate_code.py \
    --model_name $MODEL \
    --api_key $API_KEY \
    --base_url $BASE_URL \
    --output_dir $OUTPUT_PATH \
    --seed_data_path $SEED_PATH \
    --num_data_to_generate 1000 \
    --num_demo_data 3 \
    --request_batch_size 100 \
    --num_workers 20