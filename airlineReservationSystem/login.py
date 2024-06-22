from tkinter import *  # to create GUI we will import tkinter

from tkinter import messagebox  # to import message

import mysql.connector

from PIL import ImageTk  # to import jpg image in our code

import os


# Database

def login():
    if usernameEntry.get() == '' or passwdEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = 'SELECT * FROM admin WHERE LOWER(username) = %s AND password = %s'
            cur.execute(query, (usernameEntry.get().lower(), passwdEntry.get()))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Incorrect username or password')
                # Clear the username and password entry fields
                usernameEntry.delete(0, 'end')
                passwdEntry.delete(0, 'end')
            else:
                open_add_page()
        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error connecting to database: {e}')

        finally:
            if db.is_connected():
                cur.close()
                db.close()


def open_add_page():
    main.destroy()  # Close the main login window
    os.system('python adminMain.py')  # Open the addCustomer.py page


def show_password():
    if passwdEntry.cget('show') == '♡':
        passwdEntry.configure(show='')
    else:
        passwdEntry.configure(show='♡')


def Exitt():
    main.destroy()  # Close the main login window
    os.system('python welcome.py')  # Open the addCustomer.py page


main = Tk()  # create object from class Tk to create main

main.title('Admin login')  # set title
main.geometry('1540x780+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0

main.resizable(False, False)


backgroundImage = ImageTk.PhotoImage(file='img/plane2.tif')  # ImageTk.PhotoImage allows as to use image from type jpg

bgLabel = Label(main, image=backgroundImage)

bgLabel.place(x=0, y=0)  # to see the image in our window from x=0 and y=0

loginFrame = Frame(main, bg='#8EC9DB')  # inside frame, we keep our labels or buttons

loginFrame.place(x=410, y=190, width=600, height=350)

logoImage = PhotoImage(file='img/pick1.png')

logoLabel = Label(loginFrame, image=logoImage, bg='#8ecadc')

# row=0, column=0 because inside this login frame this is the first thing getting added, pady = padding in y-axis
logoLabel.grid(row=0, column=1, columnspan=3, pady=10)

unImage = PhotoImage(file='img/usernam.png')
unLabel = Label(loginFrame, image=unImage, text='Username:', compound=LEFT
                , font=('times new roman', 17, 'bold'), bg='#8ecadc')
# padx = padding in x-axis
unLabel.grid(row=2, column=1, pady=10, padx=5)

# To enter the username, bg = background image in hex, bd = border
usernameEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray85', bd=3, fg='midnight blue', width=30)
usernameEntry.grid(row=2, column=2, pady=10, padx=5)

passwdImage = PhotoImage(file='img/passwor.png')
# compound=LEFT to put the text in the left of the image
passwdLabel = Label(loginFrame, image=passwdImage, text='Password:', compound=LEFT
                    , font=('times new roman', 17, 'bold'), bg='#8ecadc')
passwdLabel.grid(row=3, column=1, pady=10, padx=5)

passwdEntry = Entry(loginFrame, show='♡', font=('times new roman', 15), bg='gray85', bd=3, fg='midnight blue', width=30)
passwdEntry.grid(row=3, column=2, pady=10, padx=5)

# **********************************Button ***********************************************
check = Checkbutton(loginFrame, text='Show Password', command=show_password, bg='#8ecadc', activebackground='#2596be')
check.grid(row=3, column=3)

loginButton = Button(loginFrame, text='Login', font=('times new roman', 15, 'bold'), bg='red', fg='white',
                     activebackground='gray87', activeforeground='black', cursor='hand2', width=7, bd=2, command=login)
loginButton.place(x=200, y=280)

BkButton = Button(loginFrame, text='Cancel', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=7, bd=2, command=Exitt)
BkButton.place(x=320, y=280)

# keep our main window on a loop
main.mainloop()