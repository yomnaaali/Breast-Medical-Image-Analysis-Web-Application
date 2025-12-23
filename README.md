# Breast Cancer Detection & Segmentation Web App 🎗️

> **Note:** This is a prototype application for educational and demonstration purposes. It utilizes Computer Vision techniques (OpenCV) to detect high-density regions in mammograms/MRI.

## 📋 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Installation & Usage](#installation--usage)
- [Project Structure](#project-structure)
- [Disclaimer](#disclaimer)

---

## 📖 About the Project | نبذة عن المشروع
This project is a Flask-based web application designed to assist in the preliminary analysis of medical images (specifically breast mammography). The app allows users to upload an X-ray image, processes it to identify the largest high-density area (potential mass), and returns the image with the highlighted region along with an estimated size.


## ✨ Features | المميزات
* **Simple UI:** Easy-to-use interface for uploading medical images.
* **Image Processing:** Automatic detection of high-density areas using OpenCV.
* **Visualization:** Draws a bounding circle around the detected region.
* **Size Estimation:** Calculates the radius of the detected area.
* **Cross-Platform:** Runs on any machine with Python installed.

## 🛠️ How It Works | آلية العمل
1.  **Upload:** User uploads an image via the web interface.
2.  **Preprocessing:** The image is converted to grayscale.
3.  **Thresholding:** A binary threshold is applied to isolate bright (dense) areas.
4.  **Contour Detection:** The algorithm finds contours and selects the largest one.
5.  **Output:** The original image is returned with the detected area circled in red.

## 💻 Technologies Used | التقنيات المستخدمة
* **Python 3.x**
* **Flask** (Web Framework)
* **OpenCV (cv2)** (Image Processing)
* **NumPy** (Numerical Operations)
* **Pillow (PIL)** (Image Manipulation)
* **HTML/CSS** (Frontend)

## 🚀 Installation & Usage | التثبيت والتشغيل

### Prerequisites

```bash
pip install flask opencv-python-headless numpy pillow

## 🚀 Running the App | طريقة تشغيل التطبيق

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Run the application:

```bash
python app.py
