## 😴 Drowsy Driver Detection System

A real-time driver monitoring system that detects drowsiness and sleepiness using computer vision and triggers an alert to prevent accidents! 🚗⚠️

### 🔹 Key Features

👀 Eye Blink Detection: Tracks eye landmarks using Dlib and OpenCV.

⏱ Real-time Monitoring: Continuously analyzes driver’s face through webcam.

🔔 Audio Alerts: Plays sound alerts for drowsy or sleeping states.

📊 Driver Status: Classifies driver as Active, Drowsy, or Sleeping with visual cues.

🎯 Accurate Detection: Uses blink ratio thresholds to detect fatigue reliably.

### 🛠 Tech Stack

- Language: Python

- Libraries: OpenCV, Dlib, NumPy, Imutils, SimpleAudio

- Models: shape_predictor_68_face_landmarks.dat (facial landmarks)

### 🚀 How to Run

- Clone this repository.

- nstall required packages:
pip install opencv-python dlib imutils numpy simpleaudio

-Download shape_predictor_68_face_landmarks.dat and place it in the project folder.

- Run the script:
python drowsy_driver_detection.py

- Look into the webcam and see real-time status updates and audio alerts.

### 📚 References

- [Dlib Facial Landmark Detection](http://dlib.net/face_landmark_detection.py.html)  
- [OpenCV Documentation](https://docs.opencv.org/)  
- [SimpleAudio Python Library](https://simpleaudio.readthedocs.io/)  
