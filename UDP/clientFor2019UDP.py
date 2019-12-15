# # import socket
# # import cv2
# # import time
# #
# # # cv2.namedWindow("Preview")
# # capture = cv2.VideoCapture(0)
# # #
# # # if capture.isOpened():
# # #     rval, frame = capture.read()
# # # else:
# # #     rval = False
# # #
# # # while rval:
# # #     rval, frame = capture.read()
# # #     cv2.imshow("Preview", frame)
# # #     key = cv2.waitKey(20)
# # #     if key == 27:
# # #         break
# # #     else:
# # #         cv2.line(img=frame, pt1=(10, 10), pt2=(100, 10), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
# # #
# # # capture.release()
# # # cv2.destroyAllWindows()
# # # cv2.waitKey(1)
# #
# # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET represents IPV4, SOCK_STREAM represents TCP
# #
# # s.connect(("10.0.0.218", 1995))
# #
# # ret, frame = capture.read()
# # data = cv2.imencode('.jpg', frame)[1].tostring()
# # stringLength = len(data)
# # print(stringLength)
# #
# # while True:
# #     ret, frame = capture.read()
# #     data = ''.join(cv2.imencode('.jpg', frame))
# #     data = bytes(data, "utf-8")
# #     s.send(data)
# #     time.sleep(2)
# import cv2
# import numpy as np
# import socket
# import sys
# import pickle
# import struct ### new code
#
# HOST = '10.0.0.218'
# PORT = 1995
#
# cap = cv2.VideoCapture(0)
# clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# clientsocket.connect((HOST, PORT))
# while True:
#     ret, frame = cap.read()
#     data = pickle.dumps(frame) ### new code
#     clientsocket.sendall(struct.pack("L", len(data))+data) ### new code

import socket
import numpy as np
import cv2 as cv


addr = ("10.0.0.218", 1995)
buf = 9216
width = 1280
height = 720
cap = cv.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
code = 'start'
code = ('start' + (buf - len(code)) * 'a').encode('utf-8')


if True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            s.sendto(code, addr)
            data = frame.tostring()
            for i in range(0, len(data), buf):
                s.sendto(data[i:i+buf], addr)
            # cv.imshow('send', frame)
            # if cv.waitKey(1) & 0xFF == ord('q'):
                # break
        else:
            break
    # s.close()
    # cap.release()
    # cv.destroyAllWindows()