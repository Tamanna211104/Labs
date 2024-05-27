import cv2
import numpy as np

# Define the ASCII characters to use
ascii_chars = ' `^",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

# Load the image in grayscale mode
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Resize the image to make it fit on the screen
height, width = img.shape
new_width = 100
new_height = int(height * (new_width / width))
img = cv2.resize(img, (new_width, new_height))

# Convert the image to ASCII characters
ascii_img = np.zeros((new_height, new_width), dtype=np.uint8)
for i in range(new_height):
    for j in range(new_width):
        pixel_value = img[i, j]
        ascii_img[i, j] = int((pixel_value / 255) * (len(ascii_chars) - 1))

# Print the ASCII art to the console
for i in range(new_height):
    for j in range(new_width):
        print(ascii_chars[ascii_img[i, j]], end='')
    print()


# Load the video file
vVideoStream = cv2.VideoCapture('video.avi')

while True:
    # Read a frame from the video
    vReturnValue, vFrame = vVideoStream.read()

    # Mirror the frame
    vFrame = cv2.flip(vFrame, 1)

    # Display the frame
    cv2.imshow('Video', vFrame)

    # Check for key press and exit if ESC is pressed
    if cv2.waitKey(1) == 27:
        break

# Release the video stream and destroy all windows
vVideoStream.release()
cv2.destroyAllWindows()

# Load the bird image in grayscale
bird_img = cv2.imread('bird.png', cv2.IMREAD_GRAYSCALE)

# Resize the bird image
bird_img = cv2.resize(bird_img, (200, 200))

# Load the background image
bg_img = cv2.imread('background.jpg')

# Crop the background image to match the size of the bird image
bg_img = bg_img[:200, :200]

# Copy the bird image to the background image
bg_img[bird_img < 255] = bird_img[bird_img < 255]

# Display the resulting image
cv2.imshow('Image', bg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Load the motorcycle image
img = cv2.imread('motorcycle.jpg')

# Define the rotation matrix
center = (img.shape[1] // 2, img.shape[0] // 2)
angle = 0
scale = 1
M = cv2.getRotationMatrix2D(center, angle, scale)

# Define the tire mask
tire_mask = np.zeros_like(img)
tire_mask[320:450, 335:475] = 255

# Define the tire rotation matrix

