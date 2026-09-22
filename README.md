# Real-Time Motorcycle Helmet & Plate Detection

Real-time computer vision system using YOLOv8 to detect motorcycle helmets and license plates, integrated with an ESP32 microcontroller to operate a physical traffic light. Trained on a custom, hand-annotated dataset of 1,140 images.

This project implements a real-time object detection system using YOLOv8 to identify motorcycle riders, their helmet usage, and license plates. The model processes live camera feeds to ensure traffic safety compliance.

## 📊 Dataset & Data Annotation
**This project heavily relied on rigorous manual data annotation.** I personally built and curated the dataset from scratch:

🔗 **[View the full annotated dataset on Roboflow](https://app.roboflow.com/chona/helmetnohelmet/models)**

* **Size:** 1,140 images.
* **Tool Used:** Roboflow.
* **Annotation Method:** Manual bounding box labeling.
* **Classes:** Overlapping and complex classes to determine passenger count and helmet status:
  * `1PHelmet` (1 Person, with helmet)
  * `2PHelmet` (2 Persons, both with helmets)
  * `1PNoHelmet` (1 Person, without helmet)
  * `2PNoHelmet` (2 Persons, at least one without helmet)
  * `LicensePlate`

## 🔌 Hardware Integration (ESP32 & Traffic Light)
The system bridges computer vision with real-world electronics. The Python inference script communicates with an ESP32 microcontroller (via Serial). Based on the real-time detection of helmets and license plates, the ESP32 triggers an electrical interface containing relays to operate a physical traffic light, effectively automating traffic control based on safety compliance.

## 🧠 Model
🔗 **[Download / Check the trained model weights](https://drive.google.com/drive/folders/10CUniM-NlrZTFSkWrjHaexQ-dYA0Uawp?usp=sharing)**

## 🛠️ Tech Stack
* **Model:** YOLOv8 (Ultralytics)
* **Language:** Python
* **Computer Vision:** OpenCV (Live camera feed integration)
* **Annotation:** Roboflow
* **Hardware:** ESP32 Microcontroller, Relay modules, Physical Traffic Light
* **Microcontroller Programming:** C++ / Arduino
