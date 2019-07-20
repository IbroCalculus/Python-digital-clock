import tkinter as tk
import time

def timeChange():
    timeFormat = time.strftime('%H:%M:%S')
    dispClock.config(text=timeFormat)
    dispClock.after(1000,timeChange)

root = tk.Tk()
dispClock = tk.Label(root, bg='red', fg='white', font=100)
dispClock.pack()
timeChange()

root.mainloop()
