#!/bin/bash

# run:
# bash internvl2_lora.sh

####################

MODEL_NAME="internvl2-8b"

MODEL_PATH="models/InternVL2-8B"

DATA_PATH="ReachQA/data/reachqa_train/instruction_data_20k_swift_minicpm.json"

OUTPUT_PATH="ReachQA/models/${MODEL_NAME}-reachqa-20k-lora"

CUDA_VISIBLE_DEVICES=0 \
swift sft \
    --model_type $MODEL_NAME \
    --model_id_or_path $MODEL_PATH \
    --sft_type lora \
    --tuner_backend peft \
    --template_type AUTO \
    --dtype AUTO \
    --output_dir $OUTPUT_PATH \
    --dataset $DATA_PATH \
    --train_dataset_sample -1 \
    --dataset_test_ratio 0.01 \
    --num_train_epochs 1 \
    --max_length 4096 \
    --check_dataset_strategy warning \
    --lora_rank 16 \
    --lora_alpha 8 \
    --lora_dropout_p 0.05 \
    --lora_target_modules ALL \
    --gradient_checkpointing true \
    --batch_size 1 \
    --weight_decay 0.1 \
    --learning_rate 2e-5 \
    --gradient_accumulation_steps 8 \
    --max_grad_norm 0.5 \
    --warmup_ratio 0.03 \
    --eval_steps 100 \
    --save_steps 100 \
    --save_total_limit -1 \
    --logging_steps 10 \
    --check_model_is_latest false \
    --use_flash_attn false