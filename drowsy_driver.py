import cv2
import numpy as np
import simpleaudio as sa
import dlib
from imutils import face_utils
frequency = 440  
fs = 44100  

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

sleep = 0
drowsy = 0
active = 0
status=""
color=(0,0,0)

def compute(ptA,ptB):
	dist = np.linalg.norm(ptA - ptB)
	return dist

def blink(a,b,c,d,e,f):
	up = compute(b,d) + compute(c,e)
	down = compute(a,f)
	ratio = up/(2.0*down)

	if(ratio>0.25):
		return 2
	elif(ratio>0.21 and ratio<=0.25):
		return 1
	else:
		return 0


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_blink = blink(landmarks[36],landmarks[37], 
        	landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blink(landmarks[42],landmarks[43], 
        	landmarks[44], landmarks[47], landmarks[46], landmarks[45])
        
        if(left_blink==0 or right_blink==0):
        	sleep+=1
        	drowsy=0
        	active=0
        	if(sleep>6):
        		status="SLEEPING !!!"
        		color = (0,0,0)
        		t = np.linspace(0, 3, 3 * fs, False)
        		note = np.sin(frequency * t * 2 * np.pi)
        		audio = note * (2**15 - 1) / np.max(np.abs(note))
        		audio = audio.astype(np.int16)
        		play_obj = sa.play_buffer(audio, 1, 2, fs)
        		play_obj.wait_done()


        elif(left_blink==1 or right_blink==1):
        	sleep=0
        	active=0
        	drowsy+=1
        	if(drowsy>3):
        		status="DROWSY !"
        		color = (0,0,0)
        		t = np.linspace(0, 2, 2 * fs, False)
        		note = np.sin(frequency * t * 2 * np.pi)
        		audio = note * (2**15 - 1) / np.max(np.abs(note))
        		audio = audio.astype(np.int16)
        		play_obj = sa.play_buffer(audio, 1, 2, fs)
        		play_obj.wait_done()




        else:
        	drowsy=0
        	sleep=0
        	active+=1
        	if(active>6):
        		status="ACTIVE :)"
        		color = (0,0,0)
        	
        cv2.putText(frame, status, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)

        for n in range(0, 68):
        	(x,y) = landmarks[n]
        	cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
      	break
