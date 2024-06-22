from tkinter import *  # to create GUI we will import tkinter
from PIL import ImageTk  # to import jpg image in our code
import os


def Exitt():
    main.destroy()  # Close the main login window
    os.system('python welcome.py')  # Open the addCustomer.py page


def addAdmin():
    main.destroy()
    os.system('python addAdmin.py')


def findAdmin():
    main.destroy()
    os.system('python findAdmin.py')



def addFlight():
    main.destroy()
    os.system('python addFlight.py')


def findFlight():
    main.destroy()
    os.system('python findFlight.py')


def ticketsReport():
    main.destroy()
    os.system('python ticketsReport.py')


main = Tk()
main.title('Admin Main')
main.geometry('1540x780+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0

main.resizable(False, False)

main.configure(bg='sky blue2')

# ********************define image for each menu****************************************
addAdminImage = PhotoImage(file='img/addAdmin.png')
findAdminImage = PhotoImage(file='img/search-profile.png')


# ********************************Create Setting menu bar*************************************
menubar = Menu(main)
main.config(menu=menubar)

SettingMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Admin", menu=SettingMenu)
SettingMenu.add_command(label='Admin Sign Up', font=('times new roman', 10), image=addAdminImage, compound=LEFT,
                        command=addAdmin)
SettingMenu.add_command(label='Find Admin', font=('times new roman', 10), image=findAdminImage, compound=LEFT,
                        command=findAdmin)

# ********************define image for each menu****************************************
addFlightImage = PhotoImage(file='img/addFlight.png')
findFlightImage = PhotoImage(file='img/search.png')

# ********************************Create flight menu bar *************************************

flightMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Flight", menu=flightMenu)
flightMenu.add_command(label='Add Flight', font=('times new roman', 10), image=addFlightImage, compound=LEFT,
                       command=addFlight)
flightMenu.add_command(label='Find Flight', font=('times new roman', 10), image=findFlightImage, compound=LEFT,
                       command=findFlight)

# ********************define image for each menu****************************************
ticketImage = PhotoImage(file='img/airplane-ticket.png')

# ********************************Create Setting Bar menu *************************************

tktReportMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Report", menu=tktReportMenu)
tktReportMenu.add_command(label='Tickets Report', font=('times new roman', 10), image=ticketImage, compound=LEFT,
                          command=ticketsReport)

# **********************************Cancel******************************************************
BkButton = Button(main, text='Cancel', font=('times new roman', 16, 'bold'), bg='gray85', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=9, bd=2,
                  command=Exitt)
BkButton.place(x=1300, y=650)

main.mainloop()
