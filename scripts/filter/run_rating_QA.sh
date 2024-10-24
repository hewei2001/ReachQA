#! /bin/bash

# run:
# bash run_filter_QA.sh

DATA_PATH="data/reachqa_train"
MODEL_PATH="models/InternVL2-40B"

CUDA_VISIBLE_DEVICES=0,1 python ./batch_filter_QA.py \
    --model_path $MODEL_PATH \
    --data_path $DATA_PATH \
    --temperature 0 \
    --num_gpus 2