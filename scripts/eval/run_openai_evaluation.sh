#! /bin/bash

# run:
# bash run_openai_evaluation.sh

####################

MODEL="gpt-4o-2024-08-06"

FILE=""
    
python ../../openai_llm_evaluation.py \
    --model_name $MODEL \
    --data_dir $FILE \
    --data_format swift \
    --num_workers 3