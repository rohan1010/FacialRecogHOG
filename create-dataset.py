#python encode_faces.py --name name_of_person

import cv2
import os
#import sys
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required = True, help = "name of the person whose images are to be captured for dataset")
args = vars(ap.parse_args())
count = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "dataset")
image_dir = os.path.join(image_dir, args["name"])

if not os.path.exists(image_dir):
	os.makedirs(image_dir)

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv2.imwrite(os.path.join(image_dir, "%d.jpg" % count), frame)
	count += 1
	cv2.imshow('frame', frame)
	if(cv2.waitKey(20) & 0xFF == ord('q')):
		break

cap.release()
cv2.destroyAllWindows()
