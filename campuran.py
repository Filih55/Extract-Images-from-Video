import cv2
import os

def extract_frames(video_path, output_folder, image_format='jpg', extraction_type='second', interval=1):
    # Buat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Buka video
    video = cv2.VideoCapture(video_path)
    
    # Hitung jumlah frame dan FPS video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_fps = video.get(cv2.CAP_PROP_FPS)
    
    # Hitung interval frame berdasarkan tipe ekstraksi
    if extraction_type == 'second':
        frame_interval = int(video_fps * interval)
    elif extraction_type == 'minute':
        frame_interval = int(video_fps * 60 * interval)
    elif extraction_type == 'frame':
        frame_interval = interval
    else:
        raise ValueError("Tipe ekstraksi tidak valid. Pilih 'second', 'minute', atau 'frame'.")
    
    count = 0
    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        if count % frame_interval == 0:
            # Simpan frame sebagai gambar
            frame_name = f"frame_{frame_count:04d}.{image_format}"
            cv2.imwrite(os.path.join(output_folder, frame_name), frame)
            
            frame_count += 1
            print(f"Menyimpan frame {frame_count}/{total_frames}")
        
        count += 1
    
    # Tutup video
    video.release()
    print("Ekstraksi selesai!")

# Contoh penggunaan
video_path = r"F:\codingan\Video to jpg\video\2.mp4"
output_folder = "output_frames"
image_format = 'jpg'

# Pilih salah satu dari tiga opsi di bawah ini:

# 1. Ekstrak 1 frame per detik
extract_frames(video_path, output_folder, image_format, extraction_type='second', interval=50)

# 2. Ekstrak 1 frame per menit
# extract_frames(video_path, output_folder, image_format, extraction_type='minute', interval=1)

# 3. Ekstrak setiap 10 frame
# extract_frames(video_path, output_folder, image_format, extraction_type='frame', interval=10)