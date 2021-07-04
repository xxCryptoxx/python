import cv2
import numpy as np

# input
url = "https://IP_ADDRESS_HERE" 
cap = cv2.VideoCapture(url)

# process
while(True):
    # input
    camera, frame = cap.read()
    # process
    if frame is not None:
        # output
        cv2.imshow("Frame", frame)
    # process control
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
# stop everything
cv2.destroyAllWindows()