import os

import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = cv2.imread('QRCODE\jays.jpg')
if (img is None):
    print("Could not read the image.")
    exit()
detectedBarcodes = decode(img)
if detectedBarcodes:
    for barcode in detectedBarcodes:
        text = barcode.data
        rect = barcode.rect
        poly = barcode.polygon
        print("Decoded Data: ", text)
        print("Rect: ", rect)
        print("Polygon: ", poly)
        cv2.rectangle(img, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 2)
        cv2.polylines(img, np.array([poly], np.int32), True, (255, 0, 0), 2)
        cv2.putText(img, text.decode("utf-8"), (rect.left, rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    plt.imshow(img)
    plt.axis('off')
    plt.show()