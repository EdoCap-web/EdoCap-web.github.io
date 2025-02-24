import qrcode

# URL fisso che il QR code deve aprire
url = "https://edocap-web.github.io/"

# Crea il QR Code
qr = qrcode.QRCode(
    version=1,  # Controlla la dimensione del QR Code (1 è il più piccolo)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Livello di correzione degli errori
    box_size=10,  # Dimensione di ogni box del QR
    border=4,  # Bordo attorno al QR Code
)

qr.add_data(url)
qr.make(fit=True)

# Genera l'immagine del QR Code
img = qr.make_image(fill="black", back_color="white")

# Salva il QR Code come immagine
img.save("qrcode_fisso.png")

print("QR Code generato e salvato come qrcode_fisso.png")
