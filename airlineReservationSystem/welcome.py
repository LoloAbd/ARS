from tkinter import *
from PIL import ImageTk  # to import jpg image in our code
import os


def Exitt():
    main.destroy()


def Login():
    main.destroy()  # Close the main login window
    os.system('python login.py')

def add():
    main.destroy()  # Close the main login window
    os.system('python customerMain.py')

main = Tk()

main.title('Welcome')  # set title

main.geometry('1540x780+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0

main.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='img/airplane.jpg')

bgLabel = Label(main, image=backgroundImage)

bgLabel.place(x=0, y=0)  # to see the image in our window from x=0 and y=0


mainFrame = Frame(main, bg='#5586AE', bd=4, relief='ridge')  # Setting bg parameter to empty string creates a frame without any background color

mainFrame.place(x=450, y=150, width=615, height=375)

tLabel = Label(mainFrame, text='Welcome In Airline Reservation\n System', font=('times new roman', 20, 'bold'),
               bg='#5586AE')

# row=0, column=0 because inside this login frame this is the first thing getting added, pady = padding in y-axis
tLabel.place(x=100, y=20)

# ********************************Air Travel*******************************
airTrav = PhotoImage(file='img/airpor.png')
airTravLabel = Label(mainFrame, image=airTrav, bg='#5586AE')

airTravLabel.place(x=50, y=80)

airButton = Button(mainFrame, text='Air Travel', font=('times new roman', 15, 'bold', 'italic'), bg='#5586AE', fg='black',
                   activebackground='white', activeforeground='black', cursor='hand2', bd=3, width=12, command=add)
airButton.place(x=20, y=160)

# ********************************admin***************************************
adminLog = PhotoImage(file='img/admi.png')
adminLabel = Label(mainFrame, image=adminLog, bg='#5586AE')

adminLabel.place(x=470, y=80)

adminButton = Button(mainFrame, text='Admin Login', font=('times new roman', 15, 'bold', 'italic'), bg='#5586AE',
                     fg='black',
                     activebackground='white', activeforeground='black', cursor='hand2', bd=3, width=12, command=Login)
adminButton.place(x=440, y=160)

# **********************************Exit**************************************

Exit = PhotoImage(file='img/logou.png')
ExitLabel = Label(mainFrame, image=Exit, compound=BOTTOM, bg='#5586AE')

ExitLabel.place(x=250, y=220)

ExitButton = Button(mainFrame, text='Exit', font=('times new roman', 15, 'bold', 'italic'), bg='#5586AE', fg='black',
                     activebackground='white', activeforeground='black', cursor='hand2', bd=3, width=12,
                     command=Exitt)
ExitButton.place(x=220, y=300)


main.mainloop()
