from tkinter import *  # to create GUI we will import tkinter
from PIL import ImageTk  # to import jpg image in our code
import os
import mysql.connector
from tkinter import ttk

def Exitt():
    main.destroy()  # Close the main login window
    os.system('python adminMain.py')  # Open the addCustomer.py page



main = Tk()
main.title('Tickets  Report')
main.geometry('1540x780+0+0') # use geometry method to set width 1350 and height 700 from x 0 and y 0
main.resizable(False, False)
main.configure(bg='white')

backgroundImage = ImageTk.PhotoImage(file='img/plane2.tif')  # ImageTk.PhotoImage allows as to use image from type jpg

bgLabel = Label(main, image=backgroundImage)

bgLabel.place(x=0, y=0)
# *******************************************************************************************************
frame = Frame(main, bd=7, relief='raised')
frame.place(x=80, y=60, width=970, height=520)

table = ttk.Treeview(frame, columns=("tkNum", "flight_id", "cs_id", "class", "price", "seats", "date"), show="headings")

table.column("tkNum", width=50)
table.heading("tkNum", text="Ticket Number")

table.column("flight_id", width=50)
table.heading("flight_id", text="Flight Number")

table.column("cs_id", width=50)
table.heading("cs_id", text="Customer ID")

table.column("class", width=50)
table.heading("class", text="Class")

table.column("price", width=50)
table.heading("price", text="Price")

table.column("seats", width=50)
table.heading("seats", text="Seats")

table.column("date", width=50)
table.heading("date", text="date")


# Create a vertical scrollbar and associate it with the Treeview
vsb = Scrollbar(frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")

table.pack(expand=True, fill="both")
# ******************************************************************************************************

try:
    db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
    cur = db.cursor()
    cur.execute("SELECT * FROM ticket")
    # Fetch all rows
    rows = cur.fetchall()

    # Iterate over fetched rows and insert them into the Treeview table
    for row in rows:
        table.insert("", "end", values=row)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if db.is_connected():
        cur.close()
        cur.close()

# *******************************************Total**************************************************

total = Label(main, text="Total number of  tickets: ", bg='#8BC8DA', font=("times new roman", 18, 'bold'), fg='red')
total.place(x=80, y=600)

totalLab = Label(main, bg='#8BC8DA', font=("times new roman", 18, 'bold'), fg='red')
totalLab.place(x=370, y=600)

try:
    # Establish MySQL connection
    db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
    cur = db.cursor()

    # Execute SQL query to count total number of tickets
    cur.execute("SELECT COUNT(*) FROM ticket")
    total_tickets = cur.fetchone()[0]  # Fetch the count from the result
    totalLab.config(text=total_tickets)

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if db.is_connected():
        cur.close()
        db.close()
# *******************************************Total**************************************************

revenues = Label(main, text="Incoming revenues: ", bg='#8BC8DA', font=("times new roman", 18, 'bold'), fg='red')
revenues.place(x=80, y=640)

revenuesLab = Label(main, bg='#8BC8DA', font=("times new roman", 18, 'bold'), fg='red')
revenuesLab.place(x=370, y=640)

try:
    # Establish MySQL connection
    db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
    cur = db.cursor()

    # Execute SQL query to calculate total revenue
    cur.execute("SELECT SUM(price * seats) AS total_revenue FROM ticket")
    total_revenue = cur.fetchone()[0]  # Fetch the total revenue from the result
    revenuesLab.config(text=f"{total_revenue:.2f} $")


except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if db.is_connected():
        cur.close()
        db.close()

# ************************************* Cancel button ***************************************************

BkButton = Button(main, text='Cancel', font=('times new roman', 16, 'bold'), bg='gray85', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=8, bd=2,
                  command=Exitt)
BkButton.place(x=940, y=600)

main.mainloop()
