import tkinter as tk

class header():

    def __init__(self,window:tk.Tk):
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        self.frame1 = tk.Frame(window, height= 0.025*height,bg = "#fefffe")
        self.frame2 = tk.Frame(window, height= 0.1*height,bg = "#f4f7f8")
        self.add_menu_bar()

    
    def pack(self):
        self.frame1.pack(fill = tk.BOTH, anchor=tk.N)
        self.frame2.pack(fill=tk.BOTH, anchor=tk.N)
        self.file_button.pack(fill = tk.Y, side = tk.LEFT)
        self.home_button.pack(fill = tk.Y, side = tk.LEFT)
        self.view_button.pack(fill = tk.Y, side = tk.LEFT)

    def add_menu_bar(self):
        self.file_button = tk.Button(self.frame1,text="File",relief=tk.FLAT,overrelief=tk.RIDGE
                                     ,bg = "#1b78ca",fg = "#ffffff",borderwidth=0)
        self.home_button = tk.Button(self.frame1,text="Home",relief=tk.FLAT,overrelief=tk.RIDGE
                                     ,bg = "#f4f7f8",borderwidth=0)
        self.view_button = tk.Button(self.frame1,text="View",relief=tk.FLAT,overrelief=tk.RIDGE
                                     ,borderwidth=0)
        
    def home(self):
        pass

    def clipboard(self):
        pass
    
    def images(self):
        pass
    
    def tools(self):
        pass

    def shapes(self):
        pass

    def colours(self):
        pass

    def view(self):
        pass

    def zoom(self):
        pass

    def show_or_hide(self):
        pass

    def dislay(self):
        pass

    def file(self):
        pass

class Home():
    
    def __init__(self, frame:tk.Frame):
        self.clipboard()
        self.images()
        self.tools()
        self.shapes()
        self.colours()

    def clipboard(self):
        pass
    
    def images(self):
        pass
    
    def tools(self):
        pass

    def shapes(self):
        pass

    def colours(self):
        pass
