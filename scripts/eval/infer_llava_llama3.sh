#! /bin/bash

# run:
# bash infer_llava_llama3.sh

####################

MODEL_NAME="llama3-llava-next-8b-hf"
DATASET_NAME="ReachQA"

MODLE_PATH="models/llama3-llava-next-8b-hf"
SUFFIX="base"

CUDA_VISIBLE_DEVICES=0 \
python ./swift_infer_dataset.py \
    --model_name $MODEL_NAME \
    --model_id_or_path $MODLE_PATH \
    --datasets $DATASET_NAME \
    --infer_backend vllm \
    --output_folder ./results/$MODEL_NAME \
    --suffix $SUFFIX
