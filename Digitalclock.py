import time
import tkinter as tk

def digital_clock():
    """Displays the current time on the label widget."""
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(1000, digital_clock)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 40))
label.pack()

digital_clock()

root.mainloop()