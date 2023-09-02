from ultralytics import YOLO

# # 모델 로드
# model = YOLO('yolov8n.yaml')  # build a new model from YAML
# model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# # 모델 학습
# model.train(data='C:\\FTS\\halflabeling\\dataset.yaml', epochs=100, imgsz=640)


# 학습 모델
model = YOLO('C:\\FTS\\runs\\detect\\train4\\weights\\best.pt')

# 이미지 폴더 위치
source = 'C:\\project_images\\images_americancasual\\americancasual_openpose_bg'

# 결과 이미지
results = model.predict(source, save=True)  # save=true = 이미지 저장


# 모델 로드
# model = YOLO('C:\\FRS\\runs\\detect\\train\\weights\\best.pt')  # pretrained YOLOv8n model