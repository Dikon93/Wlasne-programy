from distutils.command.config import config
import tkinter as tk
from time import strftime

window = tk.Tk()
label = tk.Label(window,
                 text=strftime("%H:%M:%S"),
                 font=("Tahoma", 100))


def refresh():
    label.config(text=strftime("%H:%M:%S"))
    window.after(1000, refresh)


button = tk.Button(window,
                   text="Odśwież",
                   command=refresh,
                   font=("Tahoma", 36))

label.pack(side=tk.TOP)
button.pack(side=tk.BOTTOM)
refresh()
tk.mainloop()
