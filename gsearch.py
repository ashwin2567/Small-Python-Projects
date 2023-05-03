from googlesearch import search as s
from tkinter import *
from tkinter.messagebox import showinfo
import webbrowser

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

def btn_click():
    Keyword = textinput.get();
    results = s(Keyword, 5);
    for i in results:
        textoutput = Label(root, text=i)
        textoutput.pack(fill=X)
        textoutput.bind("<Button-1>", lambda e:
        callback(i))
    

#creating gui
root = Tk() #main window
root.title("Google Search")
root.geometry("400x500")
font = ("Helvetica", 22, "bold")

textinput = Entry(root, font=font)
textinput.pack(fill=X, pady=20)
btn = Button(root, text = "Search", command=btn_click)
btn.pack()



root.mainloop()