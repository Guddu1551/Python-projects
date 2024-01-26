import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# Load the image
img = mpimg.imread("Ace.jpg")
image = Image.open("Ace.jpg")
print(f"Current Size : {image.size}")

def resize_image(size1,size2):
        resized_image = image.resize((size1,size2))
        resized_image.save(f"Ace_resize({resized_image.size[0]}x{resized_image.size[1]}).jpg")

size1 = int(input("Enter the width : "))
size2 = int(input("Enter the height : "))

resize_image(size1,size2)

plt.figure(figsize=(8, 8))
plt.imshow(img)
plt.title("Original Image")
plt.show()

plt.figure(figsize=(8, 4))
plt.hist(img.ravel(), bins=256, color='cyan', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

# Apply Gaussian blur to the image
blur = cv2.GaussianBlur(img, (15, 15), 200)

# Display the blurred image
plt.figure(figsize=(8, 8))
plt.imshow(blur)
plt.title("Gaussian Blur Image")
plt.show()