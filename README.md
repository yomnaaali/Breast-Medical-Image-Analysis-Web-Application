# Breast-Medical-Image-Analysis-Web-Application 🎗️

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![OpenCV](https://img.shields.io/badge/Library-OpenCV-red)

A web-based medical imaging tool designed to process and analyze breast mammography scans. This application utilizes Computer Vision techniques (OpenCV) to detect high-density regions, segment potential abnormalities, and provide size estimations.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Technology Stack](#-technology-stack)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Disclaimer](#-disclaimer)

---

## 📖 Project Overview
This project serves as a prototype for automated medical image analysis. It provides a simple interface for radiologists or users to upload X-ray images. The system automatically processes the image to highlight the largest area of high density (which can indicate a mass or calcification) and calculates its approximate radius.

## ✨ Key Features
* **Web Interface:** Simple and clean UI for uploading `.jpg`, `.jpeg`, and `.png` medical images.
* **Automated Segmentation:** Uses image thresholding to isolate bright regions in the mammogram.
* **ROI Detection:** Automatically identifies the largest contour (Region of Interest).
* **Visual Output:** Draws a red bounding circle around the detected area.
* **Size Estimation:** Calculates and displays the radius of the mass in centimeters (based on pixel-to-cm conversion logic).

## ⚙️ How It Works
The underlying logic in `app.py` follows this pipeline:
1.  **Input:** User uploads an image via the Flask web interface.
2.  **Preprocessing:** The image is converted to grayscale using OpenCV.
3.  **Thresholding:** A binary threshold (Pixel intensity > 200) separates high-density (white) areas from the background.
4.  **Contour Extraction:** The algorithm finds all contours and selects the one with the maximum area.
5.  **Output:** The result is rendered back to the user with the detected mass highlighted.

## 💻 Technology Stack
* **Backend:** Python 3, Flask
* **Computer Vision:** OpenCV (`cv2`), NumPy
* **Image Handling:** Pillow (PIL)
* **Frontend:** HTML5, CSS3

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/Breast-Medical-Image-Analysis-Web-Application.git](https://github.com/your-username/Breast-Medical-Image-Analysis-Web-Application.git)
cd Breast-Medical-Image-Analysis-Web-Application

###2. Create a Virtual Environment (Optional)
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

