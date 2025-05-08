import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# it captures a static background image (before the cloth is introduced)
print("Capturing background. Please keep the cloth out of the frame for 3 seconds.")
for i in range(30):  # Capture 30 frames to stabilize
    ret, background = cap.read()
    if not ret:
        print("Error: Unable to capture any background.")
        cap.release()
        exit()
background = cv2.flip(background, 1)  # Flip horizontally for mirror effect

# Define the color range for the cloth (e.g., green cloth in HSV)
cloak_lower_color = np.array([35, 100, 100])  # lower bound for green in HSV
cloak_upper_color = np.array([85, 255, 255])  # upper bound for green in HSV

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.flip(frame, 1)  # flipping it horizontally for mirror effect

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the cloth color
    mask = cv2.inRange(hsv, cloak_lower_color, cloak_upper_color)

    # Refine the mask with morphological operations to reduce noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8))

    # Invert the mask to get the non-cloth area
    mask_inv = cv2.bitwise_not(mask)

    # Extract the non-cloth part of the current frame
    visible_scene = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Extract the background part where the cloth is
    hidden_background_part = cv2.bitwise_and(background, background, mask=mask)

    # Combine the foreground and background to create the invisibility effect
    spell_result = cv2.add(visible_scene, hidden_background_part)

    # Display the result
    cv2.imshow('Invisibility Cloak', spell_result)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()