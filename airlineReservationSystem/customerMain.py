from tkinter import *  # to create GUI we will import tkinter
from PIL import ImageTk  # to import jpg image in our code
import os


def Exitt():
    main.destroy()  # Close the main login window
    os.system('python welcome.py')  # Open the addCustomer.py page


def addCustomer():
    main.destroy()
    os.system('python addCustomer.py')

def findCustomer():
    main.destroy()
    os.system('python findCustomer.py')

def bookTickets():
    main.destroy()
    os.system('python Ticket.py')


main = Tk()
main.title('Customer Main')
main.geometry('1540x780+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0
main.resizable(False, False)

main.configure(bg='sky blue2')

# backgroundImage = ImageTk.PhotoImage(file='img/pln.jpg')  # ImageTk.PhotoImage allows as to use image from type jpg

# bgLabel = Label(main, image=backgroundImage, bd='0')

# bgLabel.place(x=150, y=100)

# ********************define image for each menu****************************************
addCustomerImage = PhotoImage(file='img/customer.png')
findCustomerImage = PhotoImage(file='img/findCustomer.png')
ticketImage = PhotoImage(file='img/airplane-ticket.png')

# ********************************Create Setting menu bar*************************************
menubar = Menu(main)
main.config(menu=menubar)

custMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Customer", menu=custMenu)
custMenu.add_command(label='Sign Up', font=('times new roman', 10), image=addCustomerImage, compound=LEFT,
                     command=addCustomer)

custMenu.add_command(label='Find Customer', font=('times new roman', 10), image=findCustomerImage, compound=LEFT,
                        command=findCustomer)

bookTktMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tickets", menu=bookTktMenu)
bookTktMenu.add_command(label='Book Tickets', font=('times new roman', 10), image=ticketImage, compound=LEFT,
                        command=bookTickets)

# **********************************Cancel******************************************************
BkButton = Button(main, text='Cancel', font=('times new roman', 16, 'bold'), bg='gray85', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=9, bd=2,
                  command=Exitt)
BkButton.place(x=1300, y=650)

main.mainloop()
