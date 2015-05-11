import Tkinter
from PIL import Image, ImageTk
import main

#Globals
img = None

def createGUI():
    #create window
    window = Tkinter.Tk()
    window.geometry("1296x810+50+10")
    window.title("Twitter Profiler");

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
    txtBox.place(x=840, y=225)
    txtBox.focus_set()
    #event listener
    txtBox.bind('<Return>', lambda event:handleEventONLINE(v, window, txtBox))

    #run
    window.mainloop()

def createOfflineGUI():
    #create window
    window = Tkinter.Tk()
    window.geometry("1296x810+50+10")
    window.title("Twitter Profiler");

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
    txtBox.place(x=840, y=225)
    txtBox.focus_set()
    #event listener
    txtBox.bind('<Return>', lambda event:handleEventOFFLINE(window, txtBox))

    #run
    window.mainloop()

def handleEventONLINE(v, window, txtBox):
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

    #displayName(username, window)
    main.getUserData(username, window)

def handleEventOFFLINE(window, txtBox):
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

    main.getUserDataOFFLINE(window)

def displayName(username, window):
    name = Tkinter.Label(window, text= username, font=("arial", 28), bg = "#1a4d84", fg='white')
    name.place(x = 60, y = 40)

def showDataWarning(window):
    warning = Tkinter.Label(window,
                            text = "*User may not have enough tweets for an accurate profile",
                            font =("arial", 18),
                            bg = "#1a4d84",
                            fg = 'white')
    warning.place(x = 60, y = 60)

def displaySentScore(score, window):
    score = Tkinter.Label(window,
                            text ='Sentiment Score: '+ (str)(score),
                            font =("arial", 18),
                            bg = "#1a4d84",
                            fg = 'white')
    score.place(x = 60, y = 240)

def showBasicInfo(window, name, screenName, userID, location, accCreation, accAge):
    name = Tkinter.Label(window, text= name, font=("arial", 28), bg = "#1a4d84", fg='white')
    name.place(x = 60, y = 40)
    sc = Tkinter.Label(window, text=screenName, font=("arial", 18), bg="#1a4d84", fg="white")
    sc.place(x=60, y = 80)
    id = Tkinter.Label(window, text=userID, font=("arial", 18), bg="#1a4d84", fg="white")
    id.place(x=60, y = 110)
    loc = Tkinter.Label(window, text=location, font=("arial", 18), bg="#1a4d84", fg="white")
    loc.place(x=60, y = 140)
    accC = Tkinter.Label(window, text=accCreation, font=("arial", 18), bg="#1a4d84", fg="white")
    accC.place(x=60, y = 175)
    accA = Tkinter.Label(window, text=userID, font=("arial", 18), bg="#1a4d84", fg="white")
    accA.place(x=60, y = 205)

def displayGenInfo(window, freqTweet, freqCount, tags, sites):
    FT = Tkinter.Label(window, text= freqTweet, font=("arial", 18), bg = "#1a4d84", fg='white')
    FT.place(x = 60, y = 270)
    FQ = Tkinter.Label(window, text=freqCount, font=("arial", 18), bg="#1a4d84", fg="white")
    FQ.place(x=60, y = 300)
    tagText = Tkinter.Label(window, text=('Most used hashtags: '), font=("arial", 18), bg="#1a4d84", fg="white")
    tagText.place(x=60, y = 330)
    tag = Tkinter.Label(window, text=(tags), font=("arial", 18), bg="#1a4d84", fg="white")
    tag.place(x=320, y = 330)
    siteText = Tkinter.Label(window, text=('Most used URLs: '), font=("arial", 18), bg="#1a4d84", fg="white")
    siteText.place(x=60, y = 360)
    site = Tkinter.Label(window, text=(sites), font=("arial", 18), bg="#1a4d84", fg="white")
    site.place(x=280, y = 360)

def display(window):
    load = Image.open('wordcloud/cloud1.png')
    render =ImageTk.PhotoImage(load)
    img = Tkinter.Label(window,image = render)
    img.image = render
    img.place(x=5, y=500)

    load = Image.open('wordcloud/cloud2.png')
    render =ImageTk.PhotoImage(load)
    img = Tkinter.Label(window,image = render)
    img.image = render
    img.place(x=800, y=500)