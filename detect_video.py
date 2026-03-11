




import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Input video
cap = cv2.VideoCapture(r"D:\realme\Download\VID_20220711_130916.mp4")

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Output video writer
out = cv2.VideoWriter(
    "output_video.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    annotated_frame = results[0].plot()

    # Save frame
    out.write(annotated_frame)

    # Show video
    cv2.imshow("Detection", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()