# Gesture Controlled LED Glow

This project demonstrates a **gesture-controlled LED system** that allows users to control the glow of LEDs using finger count detection. The system utilizes a webcam for real-time gesture recognition, OpenCV for image processing, and an Arduino for hardware control.

## Project Overview

- **Input**: Hand gestures detected via webcam
- **Processing**: Finger count detection using OpenCV
- **Output**: LED control via Arduino

## Components

- **Arduino Uno**: 
  - Microcontroller that interfaces with LEDs based on input from the gesture recognition system.
- **Webcam**: 
  - Captures hand gestures in real-time.
- **LEDs**: 
  - Visual indicators that light up based on the number of fingers detected.
- **Breadboard and Jumper Wires**: 
  - Used for prototyping and connecting components.

## Software Used

- **Arduino IDE**: 
  - To program the Arduino for LED control.
- **OpenCV**: 
  - A computer vision library used for image processing and gesture detection.
- **Python**: 
  - Scripting language to handle real-time gesture recognition and communication with the Arduino.

## How It Works

1. **Capture Hand Gesture**: 
   - A webcam captures the user's hand gestures in front of it.
2. **Process Image**: 
   - OpenCV processes the images to detect and count raised fingers using image segmentation and contour detection techniques.
3. **Control LEDs**: 
   - The Arduino receives the finger count via serial communication and controls the number of LEDs lit according to the detected count.

## Setup Instructions

1. **Hardware Setup**:
   - Connect the Arduino to the LEDs, ensuring the correct pin assignments.
   - Set up the webcam in a position to clearly capture hand gestures.

2. **Software Installation**:
   - Install the required libraries:
     - OpenCV for Python: 
       ```bash
       pip install opencv-python
       ```
   - Install the Arduino IDE from the [official website](https://www.arduino.cc/en/software).

3. **Upload Arduino Code**:
   - Open the Arduino IDE and upload the provided Arduino sketch to your Arduino Uno.

4. **Run Python Script**:
   - Execute the provided Python script to start capturing gestures and control the LEDs.

## Features

- **Real-time Gesture Detection**: 
  - Detects and counts fingers in real-time, providing instant feedback.
- **LED Control**: 
  - LEDs can glow based on the number of fingers detected, enhancing user interaction.
- **User-Friendly Interface**: 
  - Simple gestures allow easy control without the need for physical buttons.

## Future Enhancements

- **Wireless Control**: 
  - Implement Bluetooth or Wi-Fi for remote operation of the LED system.
- **Advanced Gestures**: 
  - Add support for more complex gestures using machine learning techniques to improve recognition accuracy.
- **Mobile App Integration**: 
  - Develop a mobile application for better control and monitoring of the LED system.

## Authors

- B. Indhu Priya
- M. Sai Varshini
- M. Sravani
- A. Sarayu

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the OpenCV community for their valuable resources and documentation.
- Inspired by various gesture recognition projects and tutorials available online.

