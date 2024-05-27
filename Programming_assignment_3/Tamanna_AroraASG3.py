import cv2

image = input(cv2.imread("Asg3Image.png"))
cv2.imshow("image", image)
cv2.waitKey(0)

def mouse_callback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Left button clicked at ({x}, {y})')

image = cv2.imread('Asg3Image.png')
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
import numpy as np

def mouse_callback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        seed_point = (x, y)
        filled_image = np.zeros_like(image)
        cv2.floodFill(image, filled_image, seed_point, (255, 255, 255))
        cv2.imshow('filled_image', filled_image)

image = cv2.imread('Asg3Image.png')
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
import cv2
import numpy as np

def detect_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)
    return lines

def draw_lines(image, lines, color):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), color, 2)

def mouse_callback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        seed_point = (x, y)
        filled_image = np.zeros_like(image)
        cv2.floodFill(image, filled_image, seed_point, (255, 255, 255))
        cv2.imshow('filled_image', filled_image)

        lines = detect_lines(filled_image)
        corners = []  
