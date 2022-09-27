# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import matplotlib.pyplot as plt
import cv2
import pytesseract
img=cv2.imread("D:\Artificial_Intelligence\CHRISTY_SIR\OCR\images 2.jpg")
start=time.time()
print("The text")

"""
text=pytesseract.image_to_string(img)
print(text)
end=time.time()
t=end-start
print(t)

"""

# Use the cvtColor() function to grayscale the image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image,5)

def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY |
                                            cv2.THRESH_OTSU)[1]



gray=get_grayscale(img)

thresh=threshold(gray)

noise=get_grayscale(img)

plt.imshow(gray)
plt.imshow(noise)



img=gray
text=pytesseract.image_to_string(img)
print(text)


img=thresh
text1=pytesseract.image_to_string(img)
print(text1)

img=noise
text2=pytesseract.image_to_string(img)
print(text2)