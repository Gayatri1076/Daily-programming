import cv2

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()

    data, points, _ = detector.detectAndDecode(frame)

    if data:
        print("QR Code:", data)

    cv2.imshow("QR Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()