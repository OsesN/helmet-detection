# helmet-detection
Real-time computer vision system using YOLOv8 to detect motorcycle helmets and license plates. Trained on a custom, hand-annotated dataset of 1,140 images.

# Real-Time Motorcycle Helmet & Plate Detection

This project implements a real-time object detection system using YOLOv8 to identify motorcycle riders, their helmet usage, and license plates. The model processes live camera feeds to ensure traffic safety compliance.

## 📊 Dataset & Data Annotation
**This project heavily relied on rigorous manual data annotation.** I personally built and curated the dataset from scratch:
* **Size:** 1,140 images.
* **Tool Used:** Roboflow.
* **Annotation Method:** Manual bounding box labeling.
* **Classes:** Overlapping and complex classes to determine passenger count and helmet status:
  * `1PHelmet` (1 Person, with helmet)
  * `2PHelmet` (2 Persons, both with helmets)
  * `1PNoHelmet` (1 Person, without helmet)
  * `2PNoHelmet` (2 Persons, at least one without helmet)
  * `LicensePlate`



## 🛠️ Tech Stack
* **Model:** YOLOv8 (Ultralytics)
* **Language:** Python
* **Computer Vision:** OpenCV (Live camera feed integration)
* **Annotation:** Roboflow

