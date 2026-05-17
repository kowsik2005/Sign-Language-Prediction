from ultralytics import YOLO

model = YOLO(r'C:\Users\ncjay\Desktop\projectcv\env\best.pt')

results = model(source=0, show=True, conf=0.4, save=True)


