import Tkinter
from PIL import Image, ImageTk
import main

#Globals
img = None

def createGUI():
    #create window
    window = Tkinter.Tk()
    window.geometry("1296x810+50+10")
    window.title("Project name here");

    #background
    global img
    load = Image.open('bckg.jpg')
    render =ImageTk.PhotoImage(load)
    img = Tkinter.Label(window,image = render)
    img.image = render
    img.place(x=0, y=0, relwidth=1, relheight=1)

    #textbox
    v = Tkinter.StringVar()
    txtBox = Tkinter.Entry(window, textvariable = v, width = 33,relief = 'flat')
    txtBox.pack()
    txtBox.place(x=840, y=254)
    txtBox.focus_set()
    #event listener
    txtBox.bind('<Return>', lambda event:handleEvent(v, window, txtBox))

    #run
    window.mainloop()

def handleEvent(v, window, txtBox):
    #grab username
    username = v.get()
    #destroy textbox
    txtBox.pack_forget()
    txtBox.unbind('<Return>')
    #change background
    global img
    img.destroy()
    load = Image.open('back2.png')
    render =ImageTk.PhotoImage(load)
    img = Tkinter.Label(window,image = render)
    img.image = render
    img.place(x=0, y=0, relwidth=1, relheight=1)

    displayName(username, window)
    main.getUserData(username)

def displayName(username, window):
    name = Tkinter.Label(window, text= username, font=("arial", 28), bg = "#1a4d84", fg='white')
    name.place(x = 60, y = 40)