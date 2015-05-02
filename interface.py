import Tkinter
from PIL import Image, ImageTk
import main

def createGUI():
    #create window
    window = Tkinter.Tk()
    window.geometry("1296x810+50+10")
    window.title("Project name here");

    #background
    im = Image.open('bckg.jpg')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Tkinter.Label(window,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)

    #textbox
    v = Tkinter.StringVar()
    txtBox = Tkinter.Entry(window, textvariable = v, width = 33,relief = 'flat')
    txtBox.pack()
    txtBox.place(x=840, y=254)
    txtBox.focus_set()
    #event listener
    txtBox.bind('<Return>', lambda event:handleEvent(v))

    #run
    window.mainloop()

def handleEvent(v):
    username = v.get()
    print(username)

    #clearScreen() function that will destroy our bird
    #              and then present graphed data