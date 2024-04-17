from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.constants import *
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def button_clicked():
    label.config(text="Hello World!")

def select_file():
    filetypes = (
        ('jpg', '*.jpg'),
        ('png', '*.png')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    showinfo(
        title='Selected File',
        message=filename
    )

    etext = watermarktext.get()
    im = Image.open(filename)
    width, height = im.size
    draw = ImageDraw.Draw(im)

    font = ImageFont.truetype('arial.ttf', 100)
    textwidth, textheight = draw.textsize(etext, font)

    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y),etext, font=font)
    im.show()

    #Save watermarked image
    im.save('watermark.jpg')



    
 
    

window = Tk()
window.title("Image WaterMark")
window.minsize(width=500, height=500)
window.resizable(width=False, height=False)

label = Label(text="Input the Watermark Message", font=("Arial", 14, "bold"))
label.grid(column=0,row=0)
label.config(padx=10, pady=10)

watermarktext = Entry(width=20)
watermarktext.grid(column=0,row=1)

button = Button(text="Selected Images", font=("Arial", 14, "bold"), padx=5, pady=5, command=select_file)
button.grid(column=0,row=2)
button.config(padx=10, pady=10)



window.mainloop()