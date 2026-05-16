# ---------------------------------
# Image Viewer Project
# ---------------------------------

from tkinter import *
from PIL import Image, ImageTk

# Create Window
window = Tk()

window.title("Image Viewer")
window.geometry("600x500")

# Open Image
image = Image.open("sample.jpg")

# Resize Image
image = image.resize((500, 400))

# Convert Image
photo = ImageTk.PhotoImage(image)

# Show Image
label = Label(window, image=photo)

label.pack(pady=20)

# Run Window
window.mainloop()
