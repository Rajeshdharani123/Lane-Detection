# Road Detection in Video using OpenCV

This project demonstrates a Python script for detecting road lanes in a video using OpenCV. It processes the video frames, applies Canny edge detection, and detects lines resembling the road using the Hough Line Transformation method.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Requirements
Ensure you have the following libraries installed in your environment:
- Python 3.x
- OpenCV (`opencv-python`)
- Numpy

## Installation

1. Clone this repository or download the files to your local machine:
   
      git clone https://github.com/your-username/road-detection.git

   Install the required dependencies:

       pip install opencv-python numpy
### Usage
Place your video file in the desired directory. In the Python script, update the video file path:


    video_path = 'c:\\path_to_your_video\\video_file.mp4'
Run the Python script:


    python road_detection.py
The script will process the video and display the detected road lanes frame by frame. Press q to quit the video display at any time.

### How It Works
Grayscale Conversion: Each frame is converted to grayscale to reduce complexity.
Blurring: Gaussian blur is applied to reduce noise in the image.
Edge Detection: Canny edge detection is used to find the edges in the video frames.
Masking: A mask is applied to focus on the region of the road.
Line Detection: Hough Line Transformation is used to detect lane lines on the road.
Overlay: Detected lines are overlaid on the original frame and displayed.
Customization
Canny Edge Parameters: Adjust the threshold values for Canny edge detection to improve performance:
python

edges = cv2.Canny(blurred, 50, 150)  # Adjust these values
Hough Line Transformation: You can tweak the parameters for Hough Line detection:
python
Copy code
lines = cv2.HoughLinesP(masked_edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=50, maxLineGap=150)
Contributing
If you'd like to contribute to this project, feel free to submit a pull request or report any issues.
