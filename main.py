import tkinter as tk
from tkinter import font
from header import *
from board import *


window = tk.Tk()

window.title("Nathan's paint")
window.configure(bg = "green")

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

font_size = int(width / 150)
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=font_size)
default_font.configure(family = "Arial")

window.geometry(f"{int(width*0.5)}x{int(height*0.5)}")

head = header(window)
head.pack()

canvas_board = board(window)
canvas_board.pack()

window.mainloop()