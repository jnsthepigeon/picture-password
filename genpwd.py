#!/bin/python3

import cv2 as cv
import hashlib
import random
import string

cam_port = 0
cam = cv.VideoCapture(cam_port) 

result, image = cam.read() 

if result:
    m = hashlib.sha512(image)
    random.seed(m.hexdigest(), 16)
    password_length = 16
    characters = string.ascii_letters + string.digits

    generated_password = ''.join(random.choice(characters) for _ in range(password_length))

    print(generated_password)
else: 
    print("No image detected. Please! try again") 