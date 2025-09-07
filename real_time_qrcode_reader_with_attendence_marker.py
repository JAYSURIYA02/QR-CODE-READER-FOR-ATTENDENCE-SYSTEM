import cv2
import csv
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import numpy as np
import os

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

            attendence = text.decode("utf-8").strip()
            row = [field.strip() for field in attendence[1:-1].split(",")]
            roll_number = row[0]

            if not os.path.exists("attendance.csv"):
                with open("attendance.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Roll No", "Email", "Name"])

            with open("attendance.csv", "r") as f:
                existing = [line.split(",")[0] for line in f.read().splitlines()[1:]]  

            if roll_number not in existing:
                with open("attendance.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(row)

    cv2.imshow("QR Code Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
