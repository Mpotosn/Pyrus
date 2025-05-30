import tkinter as tk
import time
import pyautogui
import os, sys
from PIL import Image, ImageTk
import winsound

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(dir)

run = False

def donothing():
    pass


def begin(*args):
    global run
    if run == False:
        run = True
        time.sleep(1)
        updateimg(1,2)
        updateimg(2,1)
        updateimg(3,2)
        updateimg(4,4)
        updateimg(5,5)
        updateimg(6,2)
        updateimg(7,6)
        time.sleep(2)
        winsound.PlaySound("Xina", winsound.SND_ASYNC)
        updateimg(8,2)




def updateimg(num,sleepTime):
    imgName = dir + "/bsod" + str(num) + ".png"
    img = Image.open(imgName).resize((screen.winfo_screenwidth(),screen.winfo_screenheight()),Image.LANCZOS)
    bg1 = ImageTk.PhotoImage(img)
    bgimage.configure(image=bg1, cursor="none")
    bgimage.image = bg1
    screen.update()
    time.sleep(sleepTime)



time.sleep(7)

pyautogui.hotkey("win", "d")
time.sleep(1)
img = pyautogui.screenshot('desktop.png')

screen  = tk.Tk()
screen.geometry("{}x{}+0+0".format(screen.winfo_screenwidth(),screen.winfo_screenheight()))

bg = tk.PhotoImage(file = "desktop.png")
bgimage = tk.Label(screen, image = bg,width=screen.winfo_screenwidth() , height=screen.winfo_screenheight())

bgimage.pack()
screen.bind('<Escape>', donothing)
screen.protocol("WM_DELETE_WINDOW", donothing)
bgimage.bind('<Button-1>', begin)
screen.attributes("-fullscreen", True)

screen.attributes("-topmost", True )




screen.mainloop()
