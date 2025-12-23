from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageDraw
import io
import base64
import cv2
import numpy as np

app = Flask(__name__)

# Placeholder for a pre-trained MRI model
# Replace with your actual pre-trained model
model = None

def detect_largest_white_area(image):
    # Convert the PIL Image to a NumPy array
    img_np = np.array(image.convert("RGB"))
    

    # Convert the image to grayscale
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

    # Threshold the image to get a binary mask of white areas
    _, thresholded = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the binary mask
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the maximum area (largest white area)
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the minimum enclosing circle for the largest contour
    ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

    # Convert radius to centimeters (replace with your actual conversion factor)
    radius_cm = radius * 0.1

    return (int(x), int(y), int(radius)), radius_cm

def classify_image(image):
    (x, y, radius), radius_cm = detect_largest_white_area(image)
    return "Cancer", f"Radius: {radius_cm:.2f} cm"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        image = Image.open(file)
        result, size = classify_image(image)
        image_with_circle = draw_circle(image)

        buffered = io.BytesIO()
        image_with_circle.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return render_template('result.html', result=result, size=size, img_str=img_str)


def draw_circle(image):
    # Convert image to RGB mode
    image = image.convert("RGB")

    draw = ImageDraw.Draw(image)
    (x, y, radius), _ = detect_largest_white_area(image)
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="red", width=3)
    return image


if __name__ == '__main__':
    app.run(debug=True)
