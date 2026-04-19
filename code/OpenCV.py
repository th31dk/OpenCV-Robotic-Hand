import cv2
 
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import numpy as np
import serial
import os
import time

uno = serial.Serial('COM3', baudrate=9600)
time.sleep(2)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

mp_hands = mp.tasks.vision.HandLandmarksConnections
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles

MARGIN = 10
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)
FINGER_LETTERS = ['T', 'I', 'M', 'R', 'P']
FINGER_TIPS = [4, 8, 12, 16, 20]
FINGER_MCPS = [2, 5, 9, 13, 17]

# calibrate this
FINGER_ANGLES = {
    'T': 1500,
    'I': 1800,
    'M': 2500,
    'R': 0,
    'P': 0,
}


def draw_landmarks_on_image(rgb_image, detection_result):
    annotated_image = np.copy(rgb_image)
    height, width, _ = annotated_image.shape
    for hand_landmarks in detection_result.hand_landmarks:
        for landmark in hand_landmarks:
            x = int(landmark.x * width)
            y = int(landmark.y * height)
            cv2.circle(annotated_image, (x, y), 5, (0, 255, 0), -1)

    return annotated_image

prev_state = {}

def servo_angles(results):
    if not results.hand_landmarks:
        return
    hand = results.hand_landmarks[0]
    handedness = results.handedness[0][0].category_name

    for letter, tip, mcp in zip(FINGER_LETTERS, FINGER_TIPS, FINGER_MCPS):
        if letter == 'T':
            curled = hand[tip].x < hand[mcp].x if handedness == "Right" else hand[tip].x > hand[mcp].x
        else:
            curled = hand[tip].y > hand[mcp].y

        angle = FINGER_ANGLES[letter] if curled else 0

        if prev_state.get(letter) != angle:
            prev_state[letter] = angle
            msg = f'{letter}{angle}\n'
            print(repr(msg))
            uno.write(msg.encode())


model_path = os.path.join(os.path.dirname(__file__), 'hand_landmarker.task')
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(base_options=base_options, running_mode=vision.RunningMode.VIDEO, num_hands=1)
detector = vision.HandLandmarker.create_from_options(options)

while True:

    ret, frame = cam.read()
    if not ret:
        break
        
    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
    timestamp_ms = int(time.time() * 1000)
    results = detector.detect_for_video(mp_image, timestamp_ms)
    servo_angles(results)

    annotated = draw_landmarks_on_image(frame_rgb, results)
    cv2.imshow("OpenCV", cv2.cvtColor(annotated, cv2.COLOR_RGB2BGR))

    if cv2.waitKey(30) == 27:
        break
