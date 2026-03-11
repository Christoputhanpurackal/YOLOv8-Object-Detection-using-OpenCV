from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

image = cv2.imread(r"C:\Users\chris\Downloads\child playing.jpeg")

results = model(image)

annotated = results[0].plot()

cv2.imshow("Detection", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()