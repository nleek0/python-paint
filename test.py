import tkinter as tk

def file_new():
    print("File > New")

def file_open():
    print("File > Open")

def edit_cut():
    print("Edit > Cut")

def edit_copy():
    print("Edit > Copy")

def edit_paste():
    print("Edit > Paste")

root = tk.Tk()
root.title("Tkinter Menu Example")

# Create a Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu and add items
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Create an "Edit" menu and add items
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=edit_copy)
edit_menu.add_command(label="Paste", command=edit_paste)

# Your main content goes here...

root.mainloop()