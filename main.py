import cv2
import os

def extract_frames(video_path, output_folder, image_format='jpg'):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the video
    video = cv2.VideoCapture(video_path)
    
    # Get total number of frames
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Extract frames
    count = 10
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Save frame as image
        frame_name = f"frame_{count:04d}.{image_format}"
        cv2.imwrite(os.path.join(output_folder, frame_name), frame)
        
        count += 1
        print(f"Saving frame {count}/{total_frames}")
    
    # Close the video
    video.release()
    print("Extraction complete!")

# Example usage
video_path = r"F:\codingan\Video to jpg\video\1.mp4"
output_folder = "output_frames"
image_format = 'jpg'

extract_frames(video_path, output_folder, image_format)