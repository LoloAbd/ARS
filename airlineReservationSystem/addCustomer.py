from tkinter import *  # to create GUI we will import tkinter
from tkcalendar import *

from tkinter import messagebox  # to import message

import mysql.connector

from PIL import ImageTk  # to import jpg image in our code

import os


def sel():
    selection = str(var.get())
    if selection == '1':
        gander = 'Male'
    else:
        gander = 'Female'
    return gander


def Exitt():
    root.destroy()  # Close the main login window
    os.system('python customerMain.py')


def pick_date(event):
    global cal, date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title('Choose date of birth')
    date_window.geometry('250x230+650+150')
    date_window.resizable(False, False)
    cal = Calendar(date_window, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.place(x=0, y=0)
    submit = Button(date_window, text='Submit', font=("times new roman", 12, 'bold'), command=grab_date, bg='red',
                    fg='white',
                    activebackground='white', activeforeground='black', cursor='hand2', bd=2)
    submit.place(x=100, y=190)


def grab_date():
    dobEntry.delete(0, END)
    dobEntry.insert(0, cal.get_date())
    date_window.destroy()


def autoId():
    try:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
        cur = db.cursor()

        # Reset the auto-increment value to the next available ID
        cur.execute("ALTER TABLE customer AUTO_INCREMENT = 1")
        db.commit()

        # Get the maximum ID value after deletion
        cur.execute("SELECT MAX(cs_id) FROM customer")
        max_id = cur.fetchone()[0]

        # If there are no existing IDs, start from a predefined value
        if max_id is None:
            csId = 20001
        else:
            # Increment the maximum ID by 1 to get the next available ID
            csId = max_id + 1

        return csId

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if db.is_connected():
            cur.close()
            db.close()


def add():
    gnder = sel()
    if (FirstNEntry.get() == '' or LastNEntry.get() == '' or PassportEntry.get() == '' or AddressEntry.get() == ''
            or dobEntry.get() == '' or ContactEntry.get() == '' or NICEntry.get() == '' or gnder == ''):
        messagebox.showerror('Error', 'Fields cannot be empty')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "INSERT INTO customer (fName, lName, nic, passport, address, dob, gander, phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (FirstNEntry.get(), LastNEntry.get(), NICEntry.get(), PassportEntry.get(), AddressEntry.get(),
                   dobEntry.get(),
                   gnder, ContactEntry.get())
            cur.execute(query, val)
            db.commit()
            messagebox.showinfo('Success', 'Record inserted successfully')
            csIdEntry.configure(text=autoId())
            FirstNEntry.delete(0, 'end')
            LastNEntry.delete(0, 'end')
            NICEntry.delete(0, 'end')
            PassportEntry.delete(0, 'end')
            AddressEntry.delete(0, 'end')
            dobEntry.delete(0, 'end')
            ContactEntry.delete(0, 'end')
            Gend1Entry.deselect()
            Gend2Entry.deselect()

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')

        finally:
            if db.is_connected():
                cur.close()
                db.close()


root = Tk()
root.title("Customer Sign Up")
root.geometry('1540x780+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0

root.resizable(False, False)

root.configure(bg="sky blue")
backgroundImage = ImageTk.PhotoImage(file='img/plane2.tif')  # ImageTk.PhotoImage allows as to use image from type jpg

bgLabel = Label(root, image=backgroundImage)

bgLabel.place(x=0, y=0)

# *************************************Frame*******************************************
head_frame = Frame(root, bd=4, relief='ridge', bg="sky blue2")
head_frame.place(x=90, y=140, width=540, height=400)

head_frame2 = Frame(root, bd=4, relief='ridge', bg="sky blue2")
head_frame2.place(x=670, y=140, width=460, height=200)

# ************************************Admin ID*******************************************************
csId = Label(head_frame, text='Customer ID ', compound=LEFT, font=('times new roman', 15, 'bold'), bg='sky blue2')

csId.grid(row=1, column=0, pady=15, padx=4)

csIdEntry = Label(head_frame, text=autoId(), font=('times new roman', 15, 'bold'), bg='sky blue2', fg='red',
                  width=30)

csIdEntry.grid(row=1, column=1, pady=15, padx=4)

# ****************************First Name ***********************************************************************
FirstN = Label(head_frame, text="First Name", bg="sky blue2", font=("times new roman", 15))
FirstN.grid(row=2, column=0, pady=15, padx=4)

FirstNEntry = Entry(head_frame, font=('times new roman', 12), bg="white", width=40, bd=3)
FirstNEntry.grid(row=2, column=1, pady=15, padx=4)

# *************************************Last Name*******************************************
LastN = Label(head_frame, text="Last Name", bg="sky blue2", font=("times new roman", 15))
LastN.grid(row=3, column=0, pady=15, padx=4)

LastNEntry = Entry(head_frame, font=('times new roman', 12), bg="white", width=40, bd=3)
LastNEntry.grid(row=3, column=1, pady=15, padx=4)

# *************************************NIC*******************************************
NIC = Label(head_frame, text="NIC", bg="sky blue2", font=("times new roman", 15))
NIC.grid(row=4, column=0, pady=15, padx=4)

NICEntry = Entry(head_frame, font=('times new roman', 12), bg="white", width=40, bd=3)
NICEntry.grid(row=4, column=1, pady=15, padx=4)

# *************************************Passport*******************************************
Passport = Label(head_frame, text="Passport", bg="sky blue2", font=("times new roman", 15))
Passport.grid(row=5, column=0, pady=15, padx=4)

PassportEntry = Entry(head_frame, font=('times new roman', 12), bg="white", width=40, bd=3)
PassportEntry.grid(row=5, column=1, pady=15, padx=4)

# *************************************Address*******************************************
Address = Label(head_frame, text="Address", bg="sky blue2", font=("times new roman", 15))
Address.grid(row=6, column=0, pady=15, padx=4)

AddressEntry = Entry(head_frame, font=('times new roman', 12), bg="white", width=40, bd=3)
AddressEntry.grid(row=6, column=1, pady=15, padx=4)

# **********************************Date Of Birth********************************************
DOB = Label(head_frame2, text="Date of birth", bg="sky blue2", font=("times new roman", 15))
DOB.grid(row=1, column=0, pady=15, padx=4)

dobEntry = Entry(head_frame2, font=('times new roman', 12), bg="white", width=35, bd=3)
dobEntry.grid(row=1, column=1, pady=15, padx=4)
dobEntry.bind('<1>', pick_date)
# **********************************Gander********************************************
var = IntVar()
Gend = Label(head_frame2, text="Gender", bg="sky blue2", font=("times new roman", 15))
Gend.grid(row=2, column=0, pady=15, padx=4)

Gend1Entry = Radiobutton(head_frame2, text="Male", font=("times new roman", 12), bg='sky blue2', variable=var,
                         value='1', command=sel)

Gend1Entry.place(x=120, y=75)

Gend2Entry = Radiobutton(head_frame2, text="Female", font=("times new roman", 12), bg='sky blue2', variable=var,
                         value='2', command=sel)

Gend2Entry.place(x=200, y=75)

# **********************************Contact********************************************
Contact = Label(head_frame2, text="Contact", bg="sky blue2", font=("times new roman", 15))
Contact.grid(row=3, column=0, pady=15, padx=4)

ContactEntry = Entry(head_frame2, font=('times new roman', 12), bg="white", width=35, bd=3)
ContactEntry.grid(row=3, column=1, pady=15, padx=4)

# **********************************Button ***********************************************
confirmButton = Button(text='Confirm', font=('times new roman', 15, 'bold'), bg='red', fg='white',
                       activebackground='white', activeforeground='black', cursor='hand2', width=8, bd=2, command=add)
confirmButton.place(x=890, y=383)

CancelButton = Button(text='Cancel', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                      activebackground='white', activeforeground='black', cursor='hand2', width=8, bd=3,
                      command=Exitt)
CancelButton.place(x=1020, y=383)

root.mainloop()
