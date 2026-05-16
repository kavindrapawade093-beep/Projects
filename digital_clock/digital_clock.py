# ---------------------------------
# Digital Clock Project
# ---------------------------------

from tkinter import *
from time import strftime

# Create Window
window = Tk()

window.title("Digital Clock")
window.geometry("500x200")
window.config(bg="black")

# Function To Update Time


def time():

    current_time = strftime("%H:%M:%S %p")

    label.config(text=current_time)

    label.after(1000, time)


# Clock Label
label = Label(
    window,
    font=("Arial", 50, "bold"),
    background="black",
    foreground="lime"
)

label.pack(anchor="center")

# Start Clock
time()

# Run Window
window.mainloop()
