# aircursor-navigate-pc-hand-gestures
Project Overview
AirCursor is a computer vision-based Python project that lets you control your mouse cursor using hand gestures. It uses MediaPipe for hand tracking, OpenCV for camera input, and PyAutoGUI to simulate mouse actions.You can move the cursor using your index finger, and simulate a mouse click by bringing your thumb and index finger together.

Features
- Cursor Control: Move your mouse using your index finger.
- Click Gesture: Click by pinching your thumb and index finger.
- Real-Time Tracking: Hand detection with webcam using MediaPipe.
- Smooth Movement: Smart smoothing for stable pointer control.
- One-Hand Use: Fully operable with a single hand.
- Lightweight: Runs efficiently even on low-end machines.

Tech Stack
- OpenCV
- MediaPipe
- PyAutoGUI
- Python

Getting Started
    1.Clone the Repository
    2.Set Up a Virtual Environment
    3.Install Dependencies
      pip install -r requirements.txt
    4.Run the Project
      python main.py

Project Structure
            AirCursor/
            │
            ├── main.py               # Gesture + cursor control
            ├── utils.py              # Utility functions (distance, smoothing)
            ├── gestures.py           # Gesture definitions
            ├── requirements.txt      # Libraries

Controls:

    Action                              What It Does

    Move index finger                 Move mouse cursor
    Pinch thumb + index               Click the mouse
    Press 'q'                         Quit the program

How It Works

    1.OpenCV opens webcam feed.
    2.MediaPipe detects and tracks hand landmarks (21 points).
    3.Landmark index 8 (index fingertip) is used to control the cursor.
    4.A click gesture is detected if the index fingertip and thumb tip (index 4) are close together.
    5.PyAutoGUI moves the mouse and performs a click.

 
