import cv2
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('udp://10.0.0.218:1995?overrun_nonfatal=1&fifo_size=50000000?buffer_size=10000000', cv2.CAP_FFMPEG)
if not cap.isOpened():
    print('VideoCapture not opened')
    exit(-1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image', 1280, 720)

while True:
    ret, frame = cap.read()

    if not ret:
        print('frame empty')
        break

    # frameResize = cv2.resize(frame, (720, 480))
    cv2.imshow('image', frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
