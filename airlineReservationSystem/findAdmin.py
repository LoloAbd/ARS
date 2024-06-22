from tkinter import *  # to create GUI we will import tkinter

from tkinter import messagebox  # to import message

import mysql.connector

from PIL import ImageTk  # to import jpg image in our code

import os


def Exitt():
    main.destroy()  # Close the main login window
    os.system('python adminMain.py')


def find():
    fNameEntry.delete(0, 'end')
    lNameEntry.delete(0, 'end')
    unameEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')

    if adminIdEntry.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "SELECT * FROM admin WHERE admin_id = %s"
            val = (adminIdEntry.get(),)
            # cur.execute("SELECT * FROM admin WHERE admin_id = %s", (adminIdEntry.get(),))
            cur.execute(query, val)
            record = cur.fetchone()

            if record is None:
                messagebox.showinfo("Message", "Not Found ")
            else:
                fNameEntry.insert(0, record[1])
                lNameEntry.insert(0, record[2])
                unameEntry.insert(0, record[3])
                passwordEntry.insert(0, record[4])

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
        finally:
            if db.is_connected():
                cur.close()
                db.close()


def delete():
    if adminIdEntry.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
        if not confirmed:
            return
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "DELETE FROM admin WHERE admin_id = %s"
            val = (adminIdEntry.get(),)
            cur.execute(query, val)
            db.commit()
            messagebox.showinfo("Success", "Record deleted successfully!")

            adminIdEntry.delete(0, 'end')
            fNameEntry.delete(0, 'end')
            lNameEntry.delete(0, 'end')
            unameEntry.delete(0, 'end')
            passwordEntry.delete(0, 'end')
        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
        finally:
            if db.is_connected():
                cur.close()
                db.close()


def update():
    if adminIdEntry.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "UPDATE admin SET fName = %s, lName = %s, username = %s, password = %s WHERE admin_id = %s"
            val = (fNameEntry.get(), lNameEntry.get(), unameEntry.get(), passwordEntry.get(),
                   adminIdEntry.get())
            cur.execute(query, val)
            db.commit()  # Remember to commit the changes after an update operation
            messagebox.showinfo("Success", "Record Updated successfully!")

            adminIdEntry.delete(0, 'end')
            fNameEntry.delete(0, 'end')
            lNameEntry.delete(0, 'end')
            unameEntry.delete(0, 'end')
            passwordEntry.delete(0, 'end')

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
        finally:
            if db.is_connected():
                cur.close()
                db.close()


main = Tk()

main.title('Find Admin')

main.geometry('1540x780+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0

main.resizable(False, False)
backgroundImage = ImageTk.PhotoImage(file='img/plane2.tif')  # ImageTk.PhotoImage allows as to use image from type jpg

bgLabel = Label(main, image=backgroundImage)

bgLabel.place(x=0, y=0)

loginFrame = Frame(main, bg='sky blue2', bd=4, relief='ridge')

loginFrame.place(x=165, y=180, width=530, height=400)

# ************************************Admin ID*******************************************************
adminId = Label(main, text='Admin ID ', compound=LEFT, font=('times new roman', 17, 'bold'), bg='#83BED2')

adminId.place(x=165, y=100)

adminIdEntry = Entry(main, font=('times new roman', 15, 'bold'), bg='gray95', bd=3, fg='red',
                     width=30)

adminIdEntry.place(x=283, y=100)

findButton = Button(main, text='Find', font=('times new roman', 13, 'bold'), bg='gray87', fg='black',
                    activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3, command=find)

findButton.place(x=600, y=100)

empty = Label(loginFrame, bg='sky blue2')
empty.grid(row=1, column=0, pady=15, padx=5)
# ************************************First Name*******************************************************
fName = Label(loginFrame, text='First Name ', compound=LEFT, font=('times new roman', 15), bg='sky blue2')

fName.grid(row=2, column=1, pady=15, padx=5)

fNameEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray95', bd=3, fg='black', width=30)

fNameEntry.grid(row=2, column=2, pady=15, padx=5)

# ************************************Last Name*******************************************************
lName = Label(loginFrame, text='Last Name ', compound=LEFT, font=('times new roman', 15), bg='sky blue2')

lName.grid(row=3, column=1, pady=15, padx=5)

lNameEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray95', bd=3, fg='black', width=30)

lNameEntry.grid(row=3, column=2, pady=15, padx=5)

# ************************************Username*******************************************************
uname = Label(loginFrame, text='Username ', compound=LEFT, font=('times new roman', 15), bg='sky blue2')

uname.grid(row=4, column=1, pady=15, padx=5)

unameEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray95', bd=3, fg='black', width=30)

unameEntry.grid(row=4, column=2, pady=15, padx=5)

# ************************************password*******************************************************
password = Label(loginFrame, text='Password ', compound=LEFT, font=('times new roman', 15), bg='sky blue2')

password.grid(row=5, column=1, pady=15, padx=5)

passwordEntry = Entry(loginFrame, font=('times new roman', 15), bg='gray95', bd=3, fg='black', width=30)

passwordEntry.grid(row=5, column=2, pady=15, padx=5)

# ************************************* button ***************************************************
updateButton = Button(loginFrame, text='Update', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                      activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3, command=update)

updateButton.place(x=143, y=310)

deleteButton = Button(loginFrame, text='Delete', font=('times new roman', 15, 'bold'), bg='red', fg='white',
                      activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3, command=delete)

deleteButton.place(x=243, y=310)

BkButton = Button(loginFrame, text='Cancel', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=6, bd=3,
                  command=Exitt)

BkButton.place(x=343, y=310)

main.mainloop()
