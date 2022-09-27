# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:06:14 2022

@author: thoma
"""

import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread("D:\Artificial_Intelligence\CHRISTY_SIR\OCR\invoice-sample.jpg")

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())



n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        """
        Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
"""
cv2.imshow('img', img)
cv2.waitKey(0)