
from turtle import goto
from ReadWriteMemory import ReadWriteMemory
import tkinter as tk
import pymem
import time
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from os.path import dirname, join
import sys
import os

class PenumbraFovOvertureFovSlider:
    def __init__(self, parent):
        rwm = ReadWriteMemory()
        process_hooked = 0;
        try:
            self.process = rwm.get_process_by_name('Penumbra.exe')
            process_hooked = 1;
        except Exception as ex:
            if(type(ex).__name__ == "ReadWriteMemoryError"):
                process_hooked = 0
            else:
                sys.exit("Not expected error, contact the developer team!!!")

        if(process_hooked == 0):
            self.p_label = tk.Label(parent, text='Game process not found ! \n Run the game first !', font=('Microsoft Sans Serif', 12), bg='black', fg='red')
            self.p_label.place(relx=0.5, rely=.1, anchor="center")
            self.p_button = tk.Button(
                parent,text ="        OK        ",
                command = lambda : parent.quit(),
                font=('Microsoft Sans Serif', 12),
                bg='grey',
                fg='white', 
                borderwidth=2,
                relief="groove" ,
                cursor="hand2"  
            )
            self.p_button.place(relx=0.5, rely=0.5,anchor="center")    
            return
        

        self.process.open()
        handle = pymem.Pymem()
        handle.open_process_from_id(self.process.pid)

        base_address = handle.base_address
        self.targetFov = 70

        def timer():
            """This is the TIMER function that runs every 100 milliseconds and update the FOV"""

            #Main Fov Address
            self.offsetsFovMain = [0x1D8, 0x9C, 0x3A4, 0x10, 0x68, 0x14, 0x10]
            finalAdressFovMain = self.process.readInt(base_address + 0x29DE94)
            for offset in self.offsetsFovMain[:-1]:
                finalAdressFovMain = self.process.readInt(finalAdressFovMain + offset)
            finalAdressFovMain += self.offsetsFovMain[-1]
            self.process.writeFloat(finalAdressFovMain, convertToRadians(self.targetFov))

            #Crouch Fov Address
            self.offsetsFovCrouch = [0x188, 0x2C, 0x18C, 0x2C0, 0x38]
            finalAdressFovCrouch = self.process.readInt(base_address + 0x29DE94)
            for offset in self.offsetsFovCrouch[:-1]:
                finalAdressFovCrouch = self.process.readInt(finalAdressFovCrouch + offset)
            finalAdressFovCrouch += self.offsetsFovCrouch[-1]
            self.process.writeFloat(finalAdressFovCrouch, convertToRadians(self.targetFov))

            parent.after(100, timer)

        def on_slider_change(value):
            self.targetFov = float(value)

        # --- Slider (Scale) do Tkinter ---
        self.p_label = tk.Label(parent, text='FOV Value', font=('Microsoft Sans Serif', 12), bg='black', fg='white')
        self.p_label.place(relx=0.5, rely=.3, anchor="center")

        fov_slider = tk.Scale(parent,
            from_=70,
            to=120,
            resolution=1,
            orient=tk.HORIZONTAL,
            length=200,
            command=on_slider_change,
            font=('Microsoft Sans Serif', 10),
            bg='black',
            fg='white',
            troughcolor='gray',
            highlightthickness=0
        )

        fov_slider.set(self.targetFov) 
        fov_slider.place(relx=0.5, rely=0.5,anchor="center") 
        
        timer()

def convertToRadians(fov:float):
    return fov * (3.141592653589793238 / 180)

def convertToDegrees(fov_rad: float):
    return fov_rad * (180 / 3.141592653589793238)

def main():
    project_root = dirname(dirname(__file__))

    root = tk.Tk()
    w = 500
    h = 230
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    root.title('Penumbra - Overture - FOV slider'),
    root.wm_attributes('-toolwindow', 'False')
    root.configure(background='#000')
    root.iconbitmap("icon.ico")
    PenumbraFovOvertureFovSlider(root)
    root.mainloop()
    sys.exit(1)


if __name__ == '__main__':
    main()
