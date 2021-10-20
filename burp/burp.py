import tkinter as tk
from tkinter import Button
from playsound import playsound


sound = "burp.mp3"

root = tk.Tk()

def onclick():
    playsound(sound)



root.geometry('300x300')
root.title('Application')
root["bg"] = "black"
button = Button(root, text="Hello", padx=100, pady=100, command=onclick)
button.pack()



root.mainloop()
