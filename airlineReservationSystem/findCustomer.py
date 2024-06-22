from tkinter import *  # to create GUI we will import tkinter

from tkinter import messagebox  # to import message

import mysql.connector

from PIL import ImageTk  # to import jpg image in our code

import os


def Exitt():
    main.destroy()  # Close the main login window
    os.system('python customerMain.py')


def sel():
    selection = str(var.get())
    if selection == '1':
        gander = 'Male'
    else:
        gander = 'Female'
    return gander


def find():
    FirstNEntry.delete(0, 'end')
    LastNEntry.delete(0, 'end')
    NICEntry.delete(0, 'end')
    PassportEntry.delete(0, 'end')
    AddressEntry.delete(0, 'end')
    dobEntry.delete(0, 'end')
    ContactEntry.delete(0, 'end')
    Gend1Entry.deselect()
    Gend2Entry.deselect()

    if csIdEntry.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "SELECT * FROM customer WHERE cs_id = %s"
            val = (csIdEntry.get(),)
            cur.execute(query, val)
            record = cur.fetchone()

            if record is None:
                messagebox.showinfo("Message", "Not Found ")
            else:
                FirstNEntry.insert(0, record[1])
                LastNEntry.insert(0, record[2])
                NICEntry.insert(0, record[3])
                PassportEntry.insert(0, record[4])
                AddressEntry.insert(0, record[5])
                dobEntry.insert(0, record[6])

                if record[7] == 'Male':
                    Gend1Entry.select()
                else:
                    Gend2Entry.select()

                ContactEntry.insert(0, record[8])

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
        finally:
            if db.is_connected():
                cur.close()
                db.close()


def delete():
    if csIdEntry.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
        if not confirmed:
            return
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "DELETE FROM customer WHERE cs_id = %s"
            val = (csIdEntry.get(),)
            cur.execute(query, val)
            db.commit()
            messagebox.showinfo("Success", "Record deleted successfully!")

            csIdEntry.delete(0, 'end')
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


def update():
    gnder = sel()

    if csIdEntry.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "UPDATE customer SET fName = %s, lName = %s, nic = %s, passport = %s, address = %s, dob = %s, gander = %s, phone = %s WHERE cs_id = %s"
            val = (FirstNEntry.get(), LastNEntry.get(), NICEntry.get(), PassportEntry.get(),
                   AddressEntry.get(), dobEntry.get(), gnder, ContactEntry.get(), csIdEntry.get())
            cur.execute(query, val)
            db.commit()  # Remember to commit the changes after an update operation
            messagebox.showinfo("Success", "Record Updated successfully!")

            csIdEntry.delete(0, 'end')
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


main = Tk()

main.title('Find Customer')

main.geometry('1540x780+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0

main.resizable(False, False)
backgroundImage = ImageTk.PhotoImage(file='img/plane2.tif')  # ImageTk.PhotoImage allows as to use image from type jpg

bgLabel = Label(main, image=backgroundImage)

bgLabel.place(x=0, y=0)

loginFrame = Frame(main, bg='powder blue')

loginFrame.place(x=150, y=210)
# *************************************Frame*******************************************
head_frame = Frame(main, bd=4, relief='ridge', bg="sky blue2")
head_frame.place(x=90, y=215, width=540, height=400)

head_frame2 = Frame(main, bd=4, relief='ridge', bg="sky blue2")
head_frame2.place(x=670, y=215, width=460, height=200)
# ************************************Admin ID*******************************************************
csId = Label(main, text='Customer ID ', compound=LEFT, font=('times new roman', 16, 'bold'), bg='#83BFD3')

csId.place(x=90, y=140)

csIdEntry = Entry(main, font=('times new roman', 15, 'bold'), bg='gray95', bd=3, fg='red',
                  width=30)

csIdEntry.place(x=225, y=140)

findButton = Button(main, text='Find', font=('times new roman', 13, 'bold'), bg='gray87', fg='black',
                    activebackground='white', activeforeground='black', cursor='hand2', width=8, bd=3, command=find)

findButton.place(x=540, y=139)

# ****************************First Name ***********************************************************************
empty = Label(head_frame, bg='sky blue2')

empty.grid(row=1, column=0, pady=15, padx=4)

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

# **********************************Gander********************************************
var = IntVar()
Gend = Label(head_frame2, text="Gender", bg="sky blue2", font=("times new roman", 15))
Gend.grid(row=2, column=0, pady=15, padx=4)

Gend1Entry = Radiobutton(head_frame2, text="Male", font=("times new roman", 12), bg='sky blue2', variable=var,
                         value='1',  command=sel)

Gend1Entry.place(x=120, y=75)

Gend2Entry = Radiobutton(head_frame2, text="Female", font=("times new roman", 12), bg='sky blue2', variable=var,
                         value='2', command=sel)

Gend2Entry.place(x=200, y=75)

# **********************************Contact********************************************
Contact = Label(head_frame2, text="Contact", bg="sky blue2", font=("times new roman", 15))
Contact.grid(row=3, column=0, pady=15, padx=4)

ContactEntry = Entry(head_frame2, font=('times new roman', 12), bg="white", width=35, bd=3)
ContactEntry.grid(row=3, column=1, pady=15, padx=4)


# ************************************* button ***************************************************
updateButton = Button(main, text='Update', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                      activebackground='white', activeforeground='black', cursor='hand2', width=7, bd=3, command=update)
updateButton.place(x=810, y=450)

deleteButton = Button(main, text='Delete', font=('times new roman', 15, 'bold'), bg='red', fg='white',
                      activebackground='white', activeforeground='black', cursor='hand2', width=7, bd=3, command=delete)

deleteButton.place(x=925, y=450)

BkButton = Button(main, text='Cancel', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=7, bd=3,
                  command=Exitt)

BkButton.place(x=1040, y=450)

main.mainloop()
