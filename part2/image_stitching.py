import cv2
import os

input_folder = 'input'
output_folder = 'output'
image_files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
images = [cv2.imread(os.path.join(input_folder, f)) for f in image_files]
os.makedirs(output_folder, exist_ok=True)

# SIFT for keypoint detection and FLANN for matching
sift = cv2.SIFT_create()
flann = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=50))

for i in range(len(images) - 1):
    kp1, des1 = sift.detectAndCompute(images[i], None)
    kp2, des2 = sift.detectAndCompute(images[i + 1], None)
    matches = flann.knnMatch(des1, des2, k=2)

    good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]
    
    matched_img = cv2.drawMatches(images[i], kp1, images[i + 1], kp2, good_matches, None, flags=2)
    cv2.imwrite(os.path.join(output_folder, f'matches_{i+1}_{i+2}.jpg'), matched_img)



# Stitch images into a panorama

stitcher = cv2.Stitcher_create()
status, panorama = stitcher.stitch(images)

cv2.imwrite(os.path.join(output_folder, 'panorama.jpg'), panorama)
