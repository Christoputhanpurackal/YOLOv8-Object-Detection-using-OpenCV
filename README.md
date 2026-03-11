# YOLOv8 Object Detection using OpenCV

## Project Overview

This project implements **real-time object detection** using **YOLOv8** and **OpenCV** in Python.
The system can detect multiple objects such as **person, bottle, chair, laptop, phone, car**, and many more from images, videos, or webcam streams.

The model uses a **pretrained YOLOv8 model trained on the COCO dataset**, which supports detection of **80 different object classes**.

---

## Features

* Real-time object detection
* Detects 80+ object classes
* Works with images, videos, and webcam
* Displays bounding boxes with object labels and confidence scores
* Saves output video with detected objects
* Fast and efficient detection using YOLOv8

---

## Technologies Used

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* NumPy

---

## Project Structure

```
yolov8-object-detection
│
├── detect_webcam.py
├── detect_video.py
├── input_video.mp4
├── output_video.mp4
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/Christoputhanpurackal/object_detection-yolo
cd yolov8-object-detection
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install ultralytics opencv-python numpy
```

---

## Run Object Detection

Run detection on video:

```
python detect_video.py
```

Run detection on webcam:

```
python detect_webcam.py
```

---

## Example Objects Detected

* Person
* Bottle
* Chair
* Laptop
* Mobile Phone
* Car
* Dog
* Cat

---

## Output

The system generates a video with **detected objects highlighted using bounding boxes and labels**.

---

## Future Improvements

* Object tracking
* Person counting system
* Smart surveillance system
* Web API using FastAPI

---

## Author

Christo Puthanpurackal
