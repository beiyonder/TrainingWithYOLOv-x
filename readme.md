Configuration Setup: The YOLOv4-tiny configuration file was customized to suit the project requirements. Parameters such as the number of classes, anchor box dimensions, and training hyperparameters were defined.

Model Initialization: The pre-trained weights for the YOLOv4-tiny model were downloaded from [[here](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.conv.29)]. These weights were used as a starting point to initialize the model before training.

Training: The model was trained using the annotated dataset. The training process involved optimizing the model's parameters to minimize the detection loss. This process typically involves multiple epochs of training.

Evaluation: After training, the model was evaluated using the validation set. Metrics such as mean average precision (mAP) and precision-recall curves were computed to assess the model's performance in detecting elevator buttons.

Results:
The trained YOLOv4-tiny model demonstrated promising results in detecting elevator buttons. The following metrics were obtained during the evaluation:
Mean Average Precision (mAP): 91.43%
Precision-Recall Curve: ![download](https://github.com/beiyonder/TrainingWithYOLOv-x/assets/86228410/cf64d1a7-fbe8-4c1d-b308-665c4aaf99f1)
