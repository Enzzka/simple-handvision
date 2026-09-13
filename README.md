# simple-handvision

Another script to log my programming progress. The code is still messy and far from perfect, but it works. Just tracking my progress.

A simple computer vision script using OpenCV and CVZone (MediaPipe Deep Learning model) to track hands and render geometric overlays in real-time based on the distance between your fingers.

## How it Works & How to Use

1. **Start the App:** Run the script, and it will open your webcam feed.
2. **Switch Modes (0 to 5):** Bring the **thumb** and **pinky finger** of your first hand close together (touch them) to cycle through the 5 different modes. You will see the active mode number on the top-left of the screen.
3. **Render Shapes:** Show **two hands** to the camera. The script tracks your index and thumb tips to dynamically draw shapes (like rectangles, lines, arrows, or cross markers) between your two hands based on the active mode.
4. **Exit:** Press the `q` key on your keyboard to close the application.

## Feedback & Critics

Any critics, suggestions, or advice are highly welcome! Feel free to open an issue or leave a comment if you have tips on how I can optimize this script or clean up the code.

## Requirements

* Python 3.14
* opencv-python
* cvzone

## How to Run

1. Clone this repository:
   git clone https://github.com/Enzzka/simple-handvision

2. Install the libraries:
   pip install opencv-python cvzone

3. Run the script via terminal:
   python cam.py
