"""
Penulis: Filih 
Instagram: @filih55
Tanggal Dibuat: 2024-05-15

Program ini mengekstrak frame dari video pada interval tertentu dan menyimpannya sebagai gambar.
This program extracts frames from a video at specified intervals and saves them as images.

"""

import cv2
import os

def extract_frames(video_path, output_folder, image_format='jpg', interval_minutes=1):
    # Buat folder output jika belum ada
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Buka video
    # Open the video
    video = cv2.VideoCapture(video_path)
    
    if not video.isOpened():
        print("Error: Tidak dapat membuka video.")
        print("Error: Cannot open video.")
        return
    
    # Hitung FPS video
    # Calculate video FPS
    fps = video.get(cv2.CAP_PROP_FPS)
    
    # Hitung interval frame berdasarkan menit yang diinginkan
    # Calculate frame interval based on desired minutes
    frame_interval = int(fps * 60 * interval_minutes)
    
    # Ekstrak frame
    # Extract frames
    count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Ambil frame sesuai interval
        # Capture frame according to interval
        if count % frame_interval == 0:
            # Hitung waktu dalam menit
            # Calculate time in minutes
            minutes = int(count / (fps * 60))
            # Simpan frame sebagai gambar
            # Save frame as image
            frame_name = f"frame_{minutes:04d}_minutes.{image_format}"
            cv2.imwrite(os.path.join(output_folder, frame_name), frame)
            print(f"Menyimpan frame pada menit ke-{minutes}")
            print(f"Saving frame at minute {minutes}")
        
        count += 1
    
    # Tutup video
    # Close video
    video.release()
    print("Ekstraksi selesai!")
    print("Extraction complete!")

# Contoh penggunaan
# Example usage
video_path = r"F:\codingan\Video to jpg\video\2.mp4"
output_folder = "output_frames"
image_format = 'jpg'
interval_minutes = 0.2  # Ambil 1 frame setiap 0.2 menit (12 detik)
                        # Capture 1 frame every 0.2 minutes (12 seconds)

extract_frames(video_path, output_folder, image_format, interval_minutes)