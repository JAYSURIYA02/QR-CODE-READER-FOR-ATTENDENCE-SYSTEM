import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    detectedBarcodes = decode(frame)
    if detectedBarcodes:
        for barcode in detectedBarcodes:
            text = barcode.data
            rect = barcode.rect
            poly = barcode.polygon
            print("Decoded Data: ", text)
            print("Rect: ", rect)
            print("Polygon: ", poly)
            cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 2)
            cv2.polylines(frame, np.array([poly], np.int32), True, (255, 0, 0), 2)
            cv2.putText(frame, text.decode("utf-8"), (rect.left, rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            with open("attendance.csv", "a") as f:
                f.write(text.decode("utf-8")[1:-1] + "\n")

    cv2.imshow("QR Code Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
