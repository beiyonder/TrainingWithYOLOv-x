Configuration Setup: The YOLOv4-tiny configuration file was customized to suit the project requirements. Parameters such as the number of classes, anchor box dimensions, and training hyperparameters were defined.

Model Initialization: The pre-trained weights for the YOLOv4-tiny model were downloaded from [[here](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.conv.29)]. These weights were used as a starting point to initialize the model before training.

Training: The model was trained using the annotated dataset. The training process involved optimizing the model's parameters to minimize the detection loss. This process typically involves multiple epochs of training.

Evaluation: After training, the model was evaluated using the validation set. Metrics such as mean average precision (mAP) and precision-recall curves were computed to assess the model's performance in detecting elevator buttons.

Results:
The trained YOLOv4-tiny model demonstrated promising results in detecting elevator buttons. The following metrics were obtained during the evaluation:
Mean Average Precision (mAP): 91.43%
For best weights:
detections_count = 3498, unique_truth_count = 1198  
class_id = 0, name = button, ap = 91.43%   	 (TP = 1098, FP = 296) 

for conf_thresh = 0.25, precision = 0.79, recall = 0.92, F1-score = 0.85 
for conf_thresh = 0.25, TP = 1098, FP = 296, FN = 100, average IoU = 64.53 % 

IoU threshold = 50 %, used Area-Under-Curve for each unique Recall 
mean average precision (mAP@0.50) = 0.914312, or 91.43 % 
Total Detection Time: 1 Seconds.

Precision-Recall Curve: ![download](https://github.com/beiyonder/TrainingWithYOLOv-x/assets/86228410/cf64d1a7-fbe8-4c1d-b308-665c4aaf99f1)

A Few more processed images:
![download](https://github.com/beiyonder/TrainingWithYOLOv-x/assets/86228410/ff899ba0-6d48-4ea4-9eb5-3d34a2b4abb8)


![download](https://github.com/beiyonder/TrainingWithYOLOv-x/assets/86228410/9ccd9492-9e9c-4eef-9d47-3f25ed741fe3)


![download](https://github.com/beiyonder/TrainingWithYOLOv-x/assets/86228410/aabfe58d-0218-442e-a50a-76dc4e430109)


![download](https://github.com/beiyonder/TrainingWithYOLOv-x/assets/86228410/e23a8a92-9d5f-4cd5-9863-1e95c357472d)
