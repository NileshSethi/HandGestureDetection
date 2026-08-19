import serial
import time
import cv2
import mediapipe as mp
import serial.tools.list_ports

print("Starting gesture recognition program...")

ports = list(serial.tools.list_ports.comports())
print("Available COM ports:")
for p in ports:
    print(f"  {p.device} - {p.description}")

try:
    print("Attempting to connect to COM6...")
    arduino = serial.Serial('COM6', 9600, timeout=1)
    time.sleep(2)  
    print("Successfully connected to COM6")

    arduino.write(b"Hello LCD\n")
    print("Sent test message to Arduino")
    
except serial.SerialException as e:
    print(f"Error connecting to COM9: {e}")
    print("Trying to continue without Arduino...")
    arduino = None

print("Initializing camera...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera!")
    for i in range(1, 4):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera found at index {i}")
            break
    if not cap.isOpened():
        print("No camera found at any index!")
        if arduino:
            arduino.close()
        exit(1)
else:
    print("Camera initialized successfully at index 0")

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

gesture_meanings = {
    "Thumbs Up": "Good / Okay",
    "Thumbs Down": "Bad / Not Okay",
    "Peace": "Victory / Peace",
    "Fist": "Stop / Power",
    "Palm": "Hello / Stop",
    "Rock": "Rock On / Energy",
    "Call Me": "Call Gesture / Phone",
    "Point": "Indicating / Direction",
    "L Sign": "Loser / L shape",
    "Two Fingers Down": "Scissors / Action",
    "Middle Finger": "Rude Gesture",
    "Yo": "Cool / Yo",
    "Nice": "Good Job / Nice",
    "Unknown": "Unrecognized"
}

def finger_states(hand_landmarks, hand_label):
    lm = hand_landmarks.landmark
    fingers = []
    if hand_label == "Right":
        fingers.append(1 if lm[4].x < lm[3].x else 0)
    else:
        fingers.append(1 if lm[4].x > lm[3].x else 0)

    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    for tip, pip in zip(tips, pips):
        fingers.append(1 if lm[tip].y < lm[pip].y else 0)

    return fingers

def detect_hand_orientation(hand_landmarks):
    lm = hand_landmarks.landmark
    return "Down" if lm[0].y < lm[12].y else "Up"

def classify_gesture(states, hand_orientation):
    if states == [0, 0, 0, 0, 0]:
        return "Fist"
    elif states == [1, 0, 0, 0, 0] and hand_orientation == "Up":
        return "Thumbs Up"
    elif states == [1, 0, 0, 0, 0] and hand_orientation == "Down":
        return "Thumbs Down"
    elif states == [0, 1, 1, 0, 0]:
        return "Peace"
    elif states == [1, 1, 1, 1, 1]:
        return "Palm"
    elif states == [1, 0, 0, 0, 1]:
        return "Rock"
    elif states == [1, 0, 0, 0, 1]:
        return "Call Me"
    elif states == [0, 1, 0, 0, 0]:
        return "Point"
    elif states == [1, 1, 0, 0, 0]:
        return "L Sign"
    elif states == [0, 1, 1, 0, 0]:
        return "Two Fingers Down"
    elif states == [0, 0, 1, 0, 0]:
        return "Middle Finger"
    elif states == [1, 1, 0, 0,1]:
        return "Yo"
    elif states == [0, 0, 1, 1, 1]:
        return "Nice"
    else:
        return "Unknown"
    
print("Starting main loop...")
last_time = 0
delay = 1.0

with mp_hands.Hands(max_num_hands=1,
                    min_detection_confidence=0.8,
                    min_tracking_confidence=0.8) as hands:
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame_count += 1
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks, hand_label in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                label = hand_label.classification[0].label
                states = finger_states(hand_landmarks, label)
                hand_orientation = detect_hand_orientation(hand_landmarks)
                gesture = classify_gesture(states, hand_orientation)
                meaning = gesture_meanings.get(gesture, "")

                current_time = time.time()
                if current_time - last_time > delay:
                    message = f"{gesture}: {meaning}"
                    print(f"Detected: {message}")
                    if arduino:
                        try:
                            arduino.write((message + "\n").encode('utf-8')) 
                            print(f"Sent to Arduino: {message}")
                        except serial.SerialException as e:
                            print(f"Serial communication error: {e}")

                    last_time = current_time

                cv2.putText(frame, gesture, (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            if frame_count % 30 == 0:
                print("No hand detected")

        cv2.imshow("Gesture Recognition", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            print("Exiting...")
            break

print(f"Processed {frame_count} frames total")
cap.release()
if arduino:
    arduino.close()
cv2.destroyAllWindows()
print("Program ended")