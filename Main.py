from PIL import Image
import time
import qrcode
from Settings import QRbackcolor, QRfillcolor,QRboxsize, QRborder, QRversion

check = ".png"
print("Hi!")
time.sleep(0.8)
# Основная часть / Main
while True:
    data = input("Enter the link (for example https://github.com/ALekzov14): ")
    QRname = input("Enter the file name (for example qrcode.png):")

    if check not in QRname: #По факту это смысла не имеет,ведь пользователю сразу откроется файл,но если добавить это,то оно будет ещё и сохраняться в папку автоматически
        #вместо того,чтобы делать это после вручную
        print("Mistake.You have not entered the png file resolution!\n")
    else:
        break

# Create QR-code / Создание QR-кода
qr = qrcode.QRCode(version = QRversion, box_size = QRboxsize, border = QRborder)
qr.add_data(data)
qr.make(fit=True)

# Create image / Создание изображения QR-кода
img = qr.make_image(fill_color = QRfillcolor, back_color = QRbackcolor)
img.save(QRname)

time.sleep(0.8)

print(f"QR code named {QRname} has been successfully created!")
image = Image.open(f"{QRname}")
image.show()
