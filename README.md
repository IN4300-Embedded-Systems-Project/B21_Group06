# Smart Door Lock with Face Recognition

## Introduction

The **Smart Door Lock with Face Recognition** is a biometric security system that enhances security and convenience by integrating **facial recognition** technology with **Raspberry Pi 4**. The system uses **OpenCV** and deep learning algorithms to authenticate users and control a **solenoid lock**, ensuring a secure and keyless access method. Additionally, a **3x4 keypad** is included as an alternative authentication method.

## Features

- **Biometric authentication** using face recognition
- **Keypad backup authentication** in case of face recognition failure
- **Real-time image processing** for fast and accurate user verification
- **Logging and monitoring** of authentication attempts
- **Compact and efficient design** using Raspberry Pi 4

## Components

The system is built using the following hardware components:

- **Raspberry Pi 4** – Main controller
- **USB Camera Module** – Captures facial images
- **Solenoid/Electromagnetic Lock** – Controls door access
- **Relay Module** – Controls the lock mechanism
- **3x4 Keypad** – Backup PIN authentication

## System Architecture

1. **User approaches the door** – The system captures a real-time image.
2. **Face recognition processing** – OpenCV and deep learning-based algorithms process and authenticate the user.
3. **Lock mechanism control** – If recognized, the door unlocks; otherwise, access is denied.
4. **Keypad alternative authentication** – Users can enter a PIN if facial recognition fails.
5. **Logging and monitoring** – Records access attempts for security audits.

## Installation and Setup

### Hardware Setup

1. Connect the **USB Camera** to the Raspberry Pi.
2. Wire the **solenoid lock** and **relay module** to the Raspberry Pi’s GPIO pins.
3. Install the **3x4 keypad** for alternative authentication.
4. Secure the components in a protective casing.

### Virtual Environment Setup

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   ```bash
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Testing and Calibration

- **Face Recognition Accuracy Testing** – Tested under various lighting conditions.
- **Environmental Testing** – Validated performance with different face angles, accessories, and distances.
- **Response Time Optimization** – Optimized to ensure authentication occurs within **2 seconds**.
- **Security Testing** – Implemented measures against spoofing attacks using printed images.

## Future Enhancements

- **Liveness detection** to prevent unauthorized access using photos.
- **Mobile/Web App integration** for remote access control.
- **Integration with smart home systems** (Google Home, Alexa).
- **Improved deep learning models** for better accuracy.

## License

This project is **open-source** and can be modified and distributed under the MIT License.
