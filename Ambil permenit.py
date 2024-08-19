import cv2
import os

def extract_frames(video_path, output_folder, image_format='jpg', interval_minutes=1):
    # Buat folder output jika belum ada
    os.makedirs(output_folder, exist_ok=True)
    
    # Buka video
    video = cv2.VideoCapture(video_path)
    
    if not video.isOpened():
        print("Error: Tidak dapat membuka video.")
        return
    
    # Hitung FPS video
    fps = video.get(cv2.CAP_PROP_FPS)
    
    # Hitung interval frame berdasarkan menit yang diinginkan
    frame_interval = int(fps * 60 * interval_minutes)
    
    # Ekstrak frame
    count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Ambil frame sesuai interval
        if count % frame_interval == 0:
            # Hitung waktu dalam menit
            minutes = int(count / (fps * 60))
            # Simpan frame sebagai gambar
            frame_name = f"frame_{minutes:04d}_minutes.{image_format}"
            cv2.imwrite(os.path.join(output_folder, frame_name), frame)
            print(f"Menyimpan frame pada menit ke-{minutes}")
        
        count += 1
    
    # Tutup video
    video.release()
    print("Ekstraksi selesai!")

# Contoh penggunaan
video_path = r"F:\codingan\Video to jpg\video\2.mp4"
output_folder = "output_frames"
image_format = 'jpg'
interval_minutes = 0.2  # Ambil 1 frame setiap 1 menit

extract_frames(video_path, output_folder, image_format, interval_minutes)