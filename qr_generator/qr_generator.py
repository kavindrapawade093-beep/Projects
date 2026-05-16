# ---------------------------------
# QR Code Generator
# ---------------------------------

import qrcode

print("===== QR CODE GENERATOR =====")

# User Input
data = input("Enter Text or URL: ")

# Create QR Code
qr = qrcode.make(data)

# Save QR Code
qr.save("qrcode.png")  # type: ignore

print("\nQR Code Generated Successfully!")
print("Saved As: qrcode.png")
