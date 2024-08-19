"""
Penulis: Filih 
Instagram: @filih55
Tanggal Dibuat: 2024-05-15

Program ini mengekstrak frame dari video pada interval tertentu dan menyimpannya sebagai gambar.
This program extracts frames from a video at specified intervals and saves them as images.

"""

import cv2
import os

def extract_frames(video_path, output_folder, image_format='jpg', extraction_type='second', interval=1):
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
    
    # Hitung interval frame berdasarkan tipe ekstraksi
    # Calculate frame interval based on extraction type
    if extraction_type == 'second':
        frame_interval = int(video_fps * interval)
    elif extraction_type == 'minute':
        frame_interval = int(video_fps * 60 * interval)
    elif extraction_type == 'frame':
        frame_interval = interval
    else:
        raise ValueError("Tipe ekstraksi tidak valid. Pilih 'second', 'minute', atau 'frame'.")
        # Invalid extraction type. Choose 'second', 'minute', or 'frame'.
    
    count = 0
    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        if count % frame_interval == 0:
            # Simpan frame sebagai gambar
            # Save frame as image
            frame_name = f"frame_{frame_count:04d}.{image_format}"
            cv2.imwrite(os.path.join(output_folder, frame_name), frame)
            
            frame_count += 1
            print(f"Menyimpan frame {frame_count}/{total_frames}")
            # Saving frame {frame_count}/{total_frames}
        
        count += 1
    
    # Tutup video
    # Close the video
    video.release()
    print("Ekstraksi selesai!")
    # Extraction complete!

# Contoh penggunaan
# Usage example
video_path = r"F:\codingan\Video to jpg\video\2.mp4"
output_folder = "output_frames"
image_format = 'jpg'

# Pilih salah satu dari tiga opsi di bawah ini:
# Choose one of the three options below:

# 1. Ekstrak 1 frame per detik
# 1. Extract 1 frame per second
extract_frames(video_path, output_folder, image_format, extraction_type='second', interval=1)

# 2. Ekstrak 1 frame per menit
# 2. Extract 1 frame per minute
# extract_frames(video_path, output_folder, image_format, extraction_type='minute', interval=1)

# 3. Ekstrak setiap 10 frame
# 3. Extract every 10 frames
# extract_frames(video_path, output_folder, image_format, extraction_type='frame', interval=10)