import cv2
import os

def extract_frames(video_path, output_folder, image_format='jpg'):
    # Buat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Buka video
    video = cv2.VideoCapture(video_path)
    
    # Hitung jumlah frame
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Ekstrak frame
    count = 10
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Simpan frame sebagai gambar
        frame_name = f"frame_{count:04d}.{image_format}"
        cv2.imwrite(os.path.join(output_folder, frame_name), frame)
        
        count += 1
        print(f"Menyimpan frame {count}/{total_frames}")
    
    # Tutup video
    video.release()
    print("Ekstraksi selesai!")

# Contoh penggunaan
video_path = r"F:\codingan\Video to jpg\video\1.mp4"
output_folder = "output_frames"
image_format = 'jpg'

extract_frames(video_path, output_folder, image_format)