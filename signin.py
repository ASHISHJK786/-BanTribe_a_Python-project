from tkinter import *
from PIL import ImageTk


# functionPart

def on_enter():
        if usernameEntry.get=='Username':
            usernameEntry.delete(0, END)


# GUI part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0, 0)
login_window.title('BandTRIBE-LoginPage')

bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_window, image=bgImage)
# bgLabel.pack()
bgLabel.place(x=0, y=0)

heading1 = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white',
                 fg='firebrick1')
heading1.place(x=605, y=120)

heading2 = Label(login_window, text='BandTRIBE', font=('Microsoft Yahei UI Light', 40, 'bold'), bg='lightyellow',
                 fg='firebrick3')
heading2.place(x=190, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', on_enter)


frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

login_window.mainloop()
