# VR_Assignment1_Ankit_Gahlawat_PH2024002

**Part 1: Use computer vision techniques to Detect, segment, and count coins from an image containing scattered Indian coins.**

The script for part 1 is "coins.py". <br />
It uses the following libraries: _cv2_ and _numpy_. <br />
To run the script, simply do "python coins.py". <br />

This is the input image: ![a](https://github.com/user-attachments/assets/1d9b54ce-8149-45e7-b070-95fd6aaa9e07)

**a. Detect all coins in the image**
- **Use edge detection, to detect all coins in the image.**
- **Visualize the detected coins by outlining them in the image.**

The canny edge detection is used to detect the edges of the coins. <br />
The output file coins_detected.jpg showcases the coins detected and outlined with green color:

![coins_detected](https://github.com/user-attachments/assets/1364a8ac-869e-4371-b6b4-535650ba561d)

**b. Segmentation of Each Coin**
- **Apply region-based segmentation techniques to isolate individual coins from the image.**
- **Provide segmented outputs for each detected coin.**

For region-based segmentation, k-means clustering is used. <br />
The k is set to 2, as we want to separate the coins from the background. <br />
To isolate individual coins, the segmented image is converted to grayscale and small noises are removed so that the coins are cleanly separated. <br />
The output is saved as masks.jpg: 

![masks](https://github.com/user-attachments/assets/42e64cf6-20b2-4fe9-943f-422b7841956b)

**c. Count the Total Number of Coins**
- **Write a function to count the total number of coins detected in the image.**
- **Display the final count as an output.**

For counting the number of coins, the segmented mask images is used. <br />
First, the boundaries (contours) of each coin is detected. <br />
The total number of boundaries in this case will be the total number of coins in the image: **9**



