"""
Penulis: Filih 
Instagram: @filih55
Tanggal Dibuat: 2024-05-15

Program ini mengekstrak frame dari video pada interval tertentu dan menyimpannya sebagai gambar.
This program extracts frames from a video at specified intervals and saves them as images.

"""

import cv2
import os

def extract_frames(video_path, output_folder, image_format='jpg', frames_per_second=None):
    # Buat folder output jika belum ada
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Buka video
    # Open the video
    video = cv2.VideoCapture(video_path)
    
    # Hitung jumlah frame dan FPS video
    # Calculate total frames and video FPS
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_fps = video.get(cv2.CAP_PROP_FPS)
    
    # Hitung interval frame jika frames_per_second ditentukan
    # Calculate frame interval if frames_per_second is specified
    frame_interval = int(video_fps / frames_per_second) if frames_per_second else 1
    
    count = 0
    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        if count % frame_interval == 0:
            # Simpan frame sebagai gambar
            # Save frame as an image
            frame_name = f"frame_{frame_count:04d}.{image_format}"
            cv2.imwrite(os.path.join(output_folder, frame_name), frame)
            
            frame_count += 1
            print(f"Menyimpan frame {frame_count}/{total_frames}")
            print(f"Saving frame {frame_count}/{total_frames}")
        
        count += 1
    
    # Tutup video
    # Close the video
    video.release()
    print("Ekstraksi selesai!")
    print("Extraction complete!")

# Contoh penggunaan
# Example usage
video_path = r"F:\codingan\Video to jpg\video\2.mp4"
output_folder = "output_frames"
image_format = 'jpg'
frames_per_second = 100  # Ekstrak 1 frame per detik, sesuaikan sesuai kebutuhan
                         # Extract 1 frame per second, adjust as needed

extract_frames(video_path, output_folder, image_format, frames_per_second)