#!/bin/bash

# run:
# bash merge_lora.sh

####################
path=""  

CUDA_VISIBLE_DEVICES=0 \
swift export \
    --ckpt_dir $pth \
    --merge_lora true