from pyzbar.pyzbar import decode
from PIL import Image
from tkinter import *
#read image
img = Image.open("myqr.png");
content = decode(img);
print(content[0].data.decode());
#creating gui
root = Tk() #main window
root.title("Google Search")
root.geometry("400x500")
font = ("Helvetica", 22, "bold")

textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)


root.mainloop()

