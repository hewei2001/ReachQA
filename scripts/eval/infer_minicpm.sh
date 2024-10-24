#! /bin/bash

# run:
# bash infer_minicpm.sh

####################

MODEL_NAME="MiniCPM-Llama3-V-2_5"
DATASET_NAME="ReachQA"

MODLE_PATH="models/MiniCPM-Llama3-V-2_5"
SUFFIX="base"

CUDA_VISIBLE_DEVICES=0 \
python ./swift_infer_dataset.py \
    --model_name $MODEL_NAME \
    --model_id_or_path $MODLE_PATH \
    --datasets $DATASET_NAME \
    --infer_backend vllm \
    --output_folder ./results/$MODEL_NAME \
    --suffix $SUFFIX
