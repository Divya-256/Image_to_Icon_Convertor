import imp
from sqlite3 import Row
from tkinter import *

App=Tk()
App.title('Icon Convertor')


def open_img():
    from PIL import Image
    from tkinter import filedialog
    global img
    App.img_dir=filedialog.askopenfilename(initialdir='C',title='Select your icon image',filetypes=(('PNG Images','*.png'),('JPEG images','*.jpg'),('all files','*.*')))

    img=Image.open(App.img_dir)





App.mainloop()