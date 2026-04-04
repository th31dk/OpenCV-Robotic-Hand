import cv2
import mediapipe as mp
import serial

uno = serial.Serial('COM3', 9600)

mp_hands = mp.tasks.vision.HandLandmarker
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) == 27:
        break
        
cam.release()
cv2.destroyAllWindows()