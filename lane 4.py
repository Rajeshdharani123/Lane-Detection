import cv2
import numpy as np

def process_frame(frame):
    # Resize the frame for faster processing
    frame_resized = cv2.resize(frame, (640, 480))
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    
    # Gaussian Blur to smooth out the image
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Canny Edge Detection to find edges
    edges = cv2.Canny(blurred, 50, 150)
    
    # Define a mask region to focus on the road area (optional)
    mask = np.zeros_like(edges)
    height, width = edges.shape
    polygon = np.array([[
        (0, height),
        (width, height),
        (int(width*0.6), int(height*0.6)),
        (int(width*0.4), int(height*0.6))
    ]], np.int32)
    
    cv2.fillPoly(mask, polygon, 255)
    
    # Apply the mask to the edges
    masked_edges = cv2.bitwise_and(edges, mask)
    
    # Detect lines using Hough Line Transformation
    lines = cv2.HoughLinesP(masked_edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=50, maxLineGap=150)
    
    # Create an image to draw the lines
    line_image = np.zeros_like(frame_resized)
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    # Overlay the line image on the original frame
    combo_image = cv2.addWeighted(frame_resized, 0.8, line_image, 1, 1)
    
    return combo_image

def detect_road_in_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Process each frame
        road_detected_frame = process_frame(frame)
        
        # Display the frame
        cv2.imshow('Road Detection', road_detected_frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Call the function with the path to your video file
video_path = 'c:\\Users\\4a Freeboard\\Videos\\Highway.mp4'  # Replace with your video path
detect_road_in_video(video_path)
