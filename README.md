# Hand Gesture Detection and LCD Display

A real-time computer vision and embedded systems project that detects predefined hand gestures using a camera and displays their corresponding meanings on an LCD through a microcontroller.

The system combines **Python, OpenCV, MediaPipe, serial communication, and Arduino/NodeMCU** to create a simple and interactive gesture-based communication interface. By interpreting hand gestures such as a thumbs up, peace sign, fist, or open palm, the system converts visual input into meaningful text and displays the result locally on an LCD.

---

##  Features

###  Real-Time Hand Gesture Detection

Uses a live camera feed to detect and track hand landmarks in real time using **MediaPipe Hands**.

###  Gesture Classification

The system identifies predefined gestures and maps them to their corresponding meanings.

Supported gestures include:

*  **Thumbs Up** — Good / Okay
*  **Thumbs Down** — Bad / Not Okay
*  **Peace** — Victory / Peace
*  **Fist** — Stop / Power
*  **Palm** — Hello / Stop
*  **Call Me** — Call Gesture / Phone
*  **Point** — Indicating / Direction
*  **Rock** — Rock On / Energy
* **L Sign** — L Shape
* **Middle Finger** — Rude Gesture
* **Yo** — Cool / Yo
* **Nice** — Good Job / Nice

###  LCD Output

The recognized gesture and its meaning are transmitted to a connected microcontroller and displayed on a **16×2 LCD screen**.

###  Serial Communication

Python communicates with the Arduino/NodeMCU using **PySerial**, allowing the detected gesture information to be transferred to the embedded system in real time.

###  Computer Vision Based

The project uses camera-based gesture recognition instead of additional physical gesture sensors such as flex sensors or accelerometers.

###  Real-Time Response

The system is designed for real-time interaction, with the project achieving a response time of less than one second between gesture detection and LCD display under controlled conditions.

###  Offline Operation

The core gesture recognition process does not require an internet connection, making the system suitable for local and standalone demonstrations.

---

##  Tech Stack

### Software

* **Python 3.x**
* **OpenCV** — Camera input and image processing
* **MediaPipe** — Real-time hand landmark detection
* **PySerial** — Serial communication with the microcontroller

### Hardware

* **Arduino Uno / NodeMCU ESP8266**
* **16×2 LCD Display**
* **Laptop Webcam / USB Camera**
* **Breadboard**
* **Jumper Wires**
* **Resistors**
* **Power Supply**

---

##  How It Works

The project follows a simple camera-to-microcontroller pipeline:

```text
Camera
   ↓
Python Application
   ↓
OpenCV + MediaPipe
   ↓
Hand Landmark Detection
   ↓
Gesture Classification
   ↓
Serial Communication
   ↓
Arduino / NodeMCU
   ↓
16×2 LCD
   ↓
Gesture Meaning
```

### Working Process

1. The camera captures live video frames.
2. OpenCV processes the incoming frames.
3. MediaPipe detects the hand and identifies its landmarks.
4. The program analyzes the position of the fingers.
5. The detected finger configuration is classified into a predefined gesture.
6. A corresponding meaning is assigned to the gesture.
7. The result is transmitted through serial communication.
8. The Arduino/NodeMCU receives the message.
9. The gesture meaning is displayed on the LCD.

---

##  Getting Started

Follow these steps to run the project locally.

### Prerequisites

Make sure the following are installed on your system:

* Python 3.x
* Arduino IDE
* A working webcam or USB camera
* Arduino Uno or NodeMCU
* 16×2 LCD
* Required Python libraries

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/HandGestureDetection.git
```

### 2. Navigate to the Project Directory

```bash
cd HandGestureDetection
```

### 3. Install Python Dependencies

```bash
pip install opencv-python
pip install mediapipe
pip install pyserial
```

Or install them together:

```bash
pip install opencv-python mediapipe pyserial
```

---

##  Hardware Setup

The project uses a microcontroller connected to a 16×2 LCD display.

For an I²C-based LCD setup, the basic connections are:

| LCD | Arduino / Microcontroller |
| --- | ------------------------- |
| SDA | SDA                       |
| SCL | SCL                       |
| VCC | 5V                        |
| GND | GND                       |

> The exact wiring may vary depending on the microcontroller and LCD module being used.

---

##  Running the Project

### Start the Python Program

Run the gesture detection script:

```bash
python handgesturecode.py
```

The program will:

1. Detect available COM ports.
2. Connect to the configured microcontroller serial port.
3. Initialize the camera.
4. Open the gesture recognition window.
5. Detect and classify hand gestures.
6. Send the recognized gesture and its meaning to the microcontroller.

Once the camera window opens, place your hand in front of the camera and perform one of the supported gestures.

Press **ESC** to exit the application.

---

##  Project Structure

A typical project structure can be organized as follows:

```text
HandGestureDetection/
│
├── handgesturecode.py
├── README.md
│
├── Arduino/
│   └── lcd_display.ino
│
└── media/
    └── project-images/
```

The Python application handles camera processing and gesture recognition, while the Arduino/NodeMCU program is responsible for receiving the serial message and displaying the result on the LCD.

---

##  Project Objectives

The project was developed with the following objectives:

* To design and implement a real-time hand gesture recognition system.
* To use computer vision techniques for gesture detection.
* To interface gesture recognition with a microcontroller.
* To display recognized gesture meanings on an LCD.
* To provide a simple touch-free human–machine interaction system.
* To develop a low-cost and portable IoT-oriented prototype.

---

##  Results

The system was tested with predefined hand gestures and successfully displayed their corresponding meanings on the LCD.

Example outputs include:

```text
✋  → STOP
👍  → GOOD
👋  → HELLO
✌️  → PEACE
```

Under controlled lighting conditions, the project achieved **over 90% gesture recognition accuracy**, with the response from detection to LCD display taking **less than one second**.

---

##  Limitations

Although the prototype performs effectively under suitable conditions, it has some limitations:

* Recognition performance can be affected by poor lighting.
* The system is designed around a predefined set of gestures.
* Gesture detection may be affected by the distance and positioning of the hand relative to the camera.
* The prototype currently focuses on basic gesture recognition rather than complete sign-language interpretation.

---

##  Future Scope

The project can be further enhanced in several ways:

###  Mobile and IoT Integration

Recognized gestures could be transmitted to a mobile application or IoT dashboard using Wi-Fi or Bluetooth.

###  Voice Output

Gesture meanings could be converted into speech to improve accessibility and communication.

###  Advanced Machine Learning

More advanced machine learning models can be incorporated to recognize a larger and more complex set of gestures.

###  Standalone Computer Vision

The system could be optimized for hardware such as **ESP32-CAM** to create a more compact standalone solution.

---

##  Applications

The system demonstrates potential applications in:

* Human–computer interaction
* Touchless control systems
* Gesture-based communication
* Accessibility solutions
* Educational IoT projects
* Smart device interfaces
* Basic sign and gesture interpretation

---

##  Project Team

**Nilesh Sethi** — 24070122121
**Mishti Kinker** — 24070122108
**Maharshi Dindoliwala** — 24070122100
**Mansi Arora** — 24070122103

**Under the Guidance of:**
Dr. Dipali Dhakhole

**Symbiosis Institute of Technology, Pune**
A Constituent of Symbiosis International University

---

##  References

1. Google Research — MediaPipe Hands: Real-Time Hand Tracking
2. Arduino Documentation — LCD Interfacing with Arduino
3. References related to IoT-based gesture-controlled communication systems
4. References related to vision-based hand gesture recognition using OpenCV

---

##  Project Information

**Project Title:** Hand Gesture Detection and Displaying the Meaning on LCD Screen

**Domain:** Computer Vision · IoT · Embedded Systems · Human–Computer Interaction

**Academic Year:** 2025–26

---

##  Acknowledgement

This project was developed as part of an academic study of **Sensors and Microcontrollers**, combining computer vision with embedded systems to demonstrate a practical real-time gesture recognition and communication system.
