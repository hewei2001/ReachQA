#! /bin/bash

# run:
# bash infer_internvl2.sh

####################

MODEL_NAME="InternVL2-8B"
DATASET_NAME="ReachQA"

MODLE_PATH="models/InternVL2-8B"
SUFFIX="base"

CUDA_VISIBLE_DEVICES=1 \
python ./swift_infer_dataset.py \
    --model_name $MODEL_NAME \
    --model_id_or_path $MODLE_PATH \
    --datasets $DATASET_NAME \
    --infer_backend lmdeploy \
    --output_folder ./results/$MODEL_NAME \
    --tp 1 \
    --suffix $SUFFIX

