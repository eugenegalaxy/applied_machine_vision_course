# Applied Machine Vision Course Materials

Materials for AAU Course: Applied Machine Vision using Raspberry Pi 5

**Course Link**: [Moodle Course Section](https://www.moodle.aau.dk/course/section.php?id=677314)

## Introduction
This repository contains supplementary materials and code examples for the Applied Computer Vision course. The scripts are for you to play around with fundamental image processing tasks using OpenCV python library. Have fun! :)

## Hardware Requirements
*   **Raspberry Pi 5** (Desktop mode, pre-installed for you)
*   **Raspberry Pi Case** with fan
*   **Raspberry Pi Camera Module 3**
*   **Monitor, Keyboard, Mouse**

### Important Hardware Notes
*   **Camera Cable**: You must use the **200mm "Camera Cable"** (Orange flex cable that says "Camera Cable").
    *   **Do NOT** use the 500mm "Display Cable" - it will NOT work even though it fits.
*   **Cable Orientation**: The cable orientation is different from previous Raspberry Pi models.
    *   **Silver pins** should face the **Ethernet port**.
*   **Official Documentation**: [Connect the Camera](https://www.raspberrypi.com/documentation/accessories/camera.html#connect-the-camera)
*   **Fan must be enabled!**: sudo nano /boot/firmware/config.txt and add line "dtparam=cooling_fan=on". Reboot system with "sudo reboot".

## Pre-requisites & Setup Guide (already prepared for you except Wi-Fi)

### 1. Initial Raspberry Pi Setup
*   **Official Guide**: [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
*   **OS Installation**: [Installing the Operating System](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system)
    *   Follow the guide to set up Wi-Fi, password, user, etc.
    *   **Default Password** (for this course): `123456`

### 2. Course Environment Setup
Perform the following steps on your fresh Raspberry Pi 5 setup:

1.  **Update System**: Open a Terminal and run:
    ```bash
    sudo apt update
    ```
2.  **Install VS Code**:
    ```bash
    sudo apt install code
    ```
3.  **Install Required Python Libraries**:
    ```bash
    sudo apt install python3-opencv python3-picamzero
    ```
    *   `picamzero` docs: [picamera-zero](https://raspberrypifoundation.github.io/picamera-zero/)
4.  **Setup Project Folder**:
    *   Create or fetch the folder `applied_machine_vision_course` to your Desktop.
    *   Open this folder in VS Code.
5.  **VS Code Python Extension**:
    *   If prompted to install the "recommended Python extension", click **Install**.
    *   Otherwise, go to the "Extensions" tab (square icon on left sidebar), search for "Python", and install it.

## Code Examples
The `src/` directory contains numbered scripts corresponding to course lectures. Each script demonstrates a specific concept.

**General Usage**:
*   Open the script in VS Code.
*   Read the comments to understand the concept.
*   Run the script.
*   Most scripts will open a window showing the live camera feed with an effect applied.
*   **Press 'q'** to close the window and exit the script.

### File List & Lecture Mapping

*   `00_camera_test.py`: **Lecture 1: Introduction**
    *   Simple test to verify camera is working. Shows a preview overlay.
*   `01_grayscale.py`: **Lecture 2**
    *   Converts live feed to grayscale.
*   `02_contrast.py`: **Lecture 2**
    *   Increases contrast (Contrast factor = 1.5).
*   `03_brightness.py`: **Lecture 2**
    *   Increases brightness (Brightness increase = 50).
*   `04_histogram.py`: **Lecture 2**
    *   Displays a real-time histogram of the video feed.
*   `05_histogram_stretching.py`: **Lecture 2**
    *   Applies histogram stretching to improve contrast dynamically.
*   `06_thresholding.py`: **Lecture 2**
    *   Binary thresholding (Object pixels = 1, Noise = 0).
*   `07_background_subtraction.py`: **Lecture 2**
    *   Segments image into foreground and background using MOG2 subtractor.
