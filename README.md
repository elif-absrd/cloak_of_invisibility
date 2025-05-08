# Harry's Cloak of Invisibility 

This project creates a digital "Cloak of Invisibility" effect using Python and OpenCV. It uses a webcam to capture video, detects a piece of cloth (e.g., a green cloth) based on its color, and replaces the cloth area with a background image to simulate invisibility, mimicking the effect of Harry Potter's invisibility cloak.<br/>
Deathly hollows count - 1/3, now try to cheat death, IF YOU CAN...


## Prerequisites

- Python 3.8 or higher
- A webcam
- A piece of cloth with a distinct color (e.g., green, similar to a green screen)
- A well-lit environment for consistent color detection

## OUTPUT

![alt text](<Screenshot 2025-05-08 180954.png>)

## Setup Instructions

### 1. Clone the Repository or Download Files
Ensure you have the following files in your project directory:
- `invisibility_cloak.py` (the main script)
- `requirements.txt` (dependency list)

### 2. Set Up a Virtual Environment
To avoid conflicts with other Python projects, set up a virtual environment.

#### On Windows:
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, your terminal should show the virtual environment name (e.g., `(venv)`).

### 3. Install Dependencies
With the virtual environment activated, install the required libraries:
```bash
pip install -r requirements.txt
```

This installs `opencv-python` and `numpy` as specified in `requirements.txt`.

### 4. Run the Script
Run the main script:
```bash
python invisibility_cloak.py
```

### 5. Using the Invisibility Cloak
1. **Capture Background**: When the script starts, it will prompt you to keep the cloth out of the webcam's frame for 3 seconds to capture a static background.
2. **Introduce the Cloth**: After the background is captured, hold the colored cloth (e.g., green) in front of the webcam. The area covered by the cloth should appear "invisible," showing the background instead.
3. **Exit**: Press `q` to quit the application.

## Troubleshooting
- **Webcam Issues**: Ensure your webcam is connected and accessible. If you have multiple cameras, you may need to change the camera index in the script (e.g., `cv2.VideoCapture(1)`).
- **Poor Invisibility Effect**: Adjust the lighting to ensure the cloth color is consistent. You may need to tweak the HSV color range (`lower_color` and `upper_color`) in `invisibility_cloak.py` to match your cloth's color.
- **Performance Issues**: Ensure no other applications are heavily using the webcam or CPU.

## Notes
- The script assumes a green cloth by default. To use a different color, adjust the HSV color range in the script.
- For best results, use a cloth with a uniform color and avoid shadows or wrinkles.

## License
This project is for educational purposes and is not licensed for commercial use.
