import cv2
import numpy as np
import os

# Görüntüyü yükle
image_path = "yesil_kutu.jpg"  # Buraya kendi görüntü dosyanın adını yaz
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Kernel (yapısal eleman)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# İşlemleri uygulama
operations = {
    "original": image,
    "erode": cv2.erode(image, kernel, iterations=1),
    "dilate": cv2.dilate(image, kernel, iterations=1),
    "opening": cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel),
    "closing": cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel),
    "gradient": cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel),
    "tophat": cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel),
    "blackhat": cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel),
}

# Kayıt klasörü oluştur
output_dir = "morph_outputs"
os.makedirs(output_dir, exist_ok=True)

# Her işlemi göster ve kaydet
for name, result in operations.items():
    window_title = f"{name}"
    filename = os.path.join(output_dir, f"{name}.jpg")

    cv2.imshow(window_title, result)
    cv2.imwrite(filename, result)
    print(f"{name} işlemi kaydedildi -> {filename}")

cv2.waitKey(0)
cv2.destroyAllWindows()
