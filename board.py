import tkinter as tk


class board():
    
    def __init__(self,window:tk.Tk):
        height = window.winfo_screenheight()
        width = window.winfo_screenwidth()
        self.frame = tk.Frame(window,height = 0.25*height ,bg = "#cfd6e6")
        self.canvas = tk.Canvas(self.frame, height = 800, width = 800, bg = "#fefffe")

        self.resize_up = tk.Canvas(self.frame,height = 10, width = 10,bg = "#fefffe", bd = 2, relief = tk.RIDGE)
        self.resize_right = tk.Frame(self.frame,height = 10, width = 10,bg = "#fefffe", bd = 2, relief = tk.RIDGE)
        self.resize_both = tk.Frame(self.frame,height = 10, width = 10,bg = "#fefffe", bd = 2, relief = tk.RIDGE)

        self.start_x = 0
        self.start_y = 0

    def pack(self):
        #Main Board
        self.frame.pack(fill = tk.BOTH, expand = True)
        self.canvas.pack(anchor = tk.NW,padx=10, pady=10)
        self.canvas.bind("<Button-1>",self.get_coords)
        self.canvas.bind("<B1-Motion>", self.draw)

        #Resizing the canvas
        self.resize_up.pack()
        self.resize_right.pack()
        self.resize_both.pack()
        #self.resize_up.place(x=self.canvas.winfo_reqwidth()/2, y=self.canvas.winfo_reqheight())
        self.resize_up.place(x=1000, y=500)
        self.resize_right.place(x=self.canvas.winfo_reqwidth(), y=self.canvas.winfo_reqheight()/2)
        self.resize_both.place(x=self.canvas.winfo_reqwidth(), y=self.canvas.winfo_reqheight())

        self.resize_up.bind("<B1-Motion>",self.resize_vert)

    def get_coords(self,event):
        self.start_x = event.x
        self.start_y = event.y

    def draw(self,event):
        
        x, y = event.x, event.y
        
        self.canvas.create_line(self.start_x, self.start_y, x, y, width=2, fill="black")
        self.start_x = x
        self.start_y = y

    def resize_vert(self,event):
        new_y =event.y

        self.resize_up.place(y = new_y)
        #self.canvas.config(height=y+self.canvas.winfo_reqheight())
        
    