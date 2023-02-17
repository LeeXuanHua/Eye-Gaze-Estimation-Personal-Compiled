#!/bin/bash

# uncomment this if you use eye_net
MODEL_WEIGHTS="model_weights/eye_net.pkl"
MODEL_NAME="eye_net"

# uncomment this if you use pruned_eye_net
# MODEL_WEIGHTS="model_weights/pruned_eye_net.pkl"
# MODEL_NAME="pruned_eye_net"

# uncomment this if you use eye_net_m
# MODEL_WEIGHTS="model_weights/eye_net_m.pkl"
# MODEL_NAME="eye_net_m"

BBOX_WEIGHTS_PATH="model_weights/G030_c32_best.pth"

# MODES=("org" "filter")
MODES=("filter")

# THRESHOLDS=("001" "005" "010" "050" "100")
THRESHOLDS=("001")

for MD in "${MODES[@]}"
do
	for TH in "${THRESHOLDS[@]}"
	do
		OUTPUT_DIR="output_${MODEL_NAME}_${MD}_${TH}"
		for num in {1..1}
		do
			if [ $MD == "filter" ]; then
				python editted_main.py --sequence ${num}  \
				--mode ${MD} \
				--density_threshold 0.${TH} \
				--dataset openEDS \
				--model ${MODEL_NAME} \
				--pytorch_model_path ${MODEL_WEIGHTS} \
				--bbox_model_path ${BBOX_WEIGHTS_PATH} \
				--output_path ${OUTPUT_DIR} \
				--suffix _${TH} \
				--preview
				# --video_shape 240 320
				# --video_shape 260 346
				# --disable_edge_info \ 
				# --use_sift
			else
				python editted_main.py --sequence ${num} \
				--mode ${MD} \
				--model ${MODEL_NAME} \
				--dataset openEDS \
				--pytorch_model_path ${MODEL_WEIGHTS} \
				--output_path ${OUTPUT_DIR} \
				--suffix _${TH} \
				--preview
			fi
			
		done
	done
done

			# --video_shape 240 320 \