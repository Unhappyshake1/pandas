"""
    File name: main.py

    main.py will be the initial class where the starting screen and the GUI window will be created. Testing
"""
import tkinter as tk
from tkinter import font as tkfont
from StartFrame import StartFrame
from outputFrame import outputFrame


# show frame
def show_frame(frame):
    frame.tkraise()


class MainProgram(tk.Tk):
    def __init__(self,  *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for frame in (StartFrame, outputFrame):
            page_name = frame.__name__
            current_frame = frame(parent=container, controller=self)
            self.frames[page_name] = current_frame

            current_frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartFrame")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def get_page(self, frame_name):
        return self.frames[frame_name]


if __name__ == "__main__":
    main = MainProgram()
    main.geometry("900x800")
    main.mainloop()
