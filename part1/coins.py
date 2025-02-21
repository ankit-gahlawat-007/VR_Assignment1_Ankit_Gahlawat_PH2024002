import cv2
import numpy as np
import os


image = cv2.imread("input.jpg")


# Edge Detection

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 100, 200)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = image.copy()
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)

cv2.imwrite("coins_detected.jpg", output)  

print("Edge detection: coins_detected.jpg")



# Segmentation for each coin

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for K-Means
reshaped_img = image_rgb.reshape((-1, 3))  # Flatten the image for clustering

# Apply K-Means Clustering
K = 2  # Optimized number of clusters
_, labels, centers = cv2.kmeans(np.float32(reshaped_img), K, None, None , 10, cv2.KMEANS_RANDOM_CENTERS)

segmented_img = centers[labels.flatten()].reshape(image.shape).astype(np.uint8)

gray_segmented = cv2.cvtColor(segmented_img, cv2.COLOR_RGB2GRAY)
_, binary = cv2.threshold(gray_segmented, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Morphological Operations to remove noise and merge small segments
kernel = np.ones((5, 5), np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

cv2.imwrite("masks.jpg", binary)

print("Segmented masks for the coins: masks.jpg")



# Counting the number of coins

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

num_coins = len(contours)
print(f"Total number of detected coins: {num_coins}")
