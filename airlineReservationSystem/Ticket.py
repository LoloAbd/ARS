from tkinter import *  # to create GUI we will import tkinter
import re
from tkinter import messagebox  # to import message
import mysql.connector
import os
from tkinter import ttk


def Exitt():
    root.destroy()  # Close the main login window
    os.system('python customerMain.py')


def open_payment_window():
    flight_number = FliNumLab.cget("text")
    if csId.get() == '' or flight_number == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    else:
        payment_window = Toplevel(root)
        payment_window.title("Payment")
        payment_window.geometry('350x200+480+200')
        payment_window.resizable(False, False)

        # Payment form
        label_card_number = ttk.Label(payment_window, text="Card Number:", font=("times new roman", 13, 'bold'))
        label_card_number.place(x=10, y=20)
        entry_card_number = ttk.Entry(payment_window, font=("times new roman", 13, 'bold'), width=20)
        entry_card_number.place(x=130, y=20)

        label_expiry_date = ttk.Label(payment_window, text="Expiry Date:", font=("times new roman", 13, 'bold'))
        label_expiry_date.place(x=10, y=60)
        entry_expiry_date = ttk.Entry(payment_window, font=("times new roman", 13, 'bold'), width=20)
        entry_expiry_date.place(x=130, y=60)

        label_cvv = ttk.Label(payment_window, text="CVV:", font=("times new roman", 13, 'bold'))
        label_cvv.place(x=10, y=100)
        entry_cvv = ttk.Entry(payment_window, show="*", font=("times new roman", 13, 'bold'), width=20)
        entry_cvv.place(x=130, y=100)

        def process_payment():
            card_number = entry_card_number.get()
            expiry_date = entry_expiry_date.get()
            cvv = entry_cvv.get()

            # Validate credit card number
            if not re.match(r'^[0-9]{16}$', card_number):
                messagebox.showerror("Error", "Invalid card number")
                return

            # Validate expiry date
            if not re.match(r'^(0[1-9]|1[0-2])\/[0-9]{2}$', expiry_date):
                messagebox.showerror("Error", "Invalid expiry date. Use MM/YY format.")
                return

            # Validate CVV
            if not re.match(r'^[0-9]{3}$', cvv):
                messagebox.showerror("Error", "Invalid CVV")
                return

            # If all data is valid, proceed with payment processing
            messagebox.showinfo("Success", "Payment successful")
            payment_window.destroy()
            book_ticket()

        # Payment button
        button_pay = Button(payment_window, text='Pay', font=('times new roman', 14, 'bold'), bg='white',
                            fg='red',
                            activebackground='white', activeforeground='black', cursor='hand2', width=5, bd=3,
                            command=process_payment)
        button_pay.place(x=150, y=140)


def searchFlight():
    if srcChoosen.get() == '' or depChoosen.get() == '':
        messagebox.showerror('Error', 'Empty Source Or Departure')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "SELECT flight_id, fName, source, departure, date, depTime, arrTime, flightCharge FROM flight WHERE departure = %s AND source = %s"
            val = (depChoosen.get(), srcChoosen.get())
            cur.execute(query, val)
            rows = cur.fetchall()

            for item in table.get_children():
                table.delete(item)
            # Iterate over fetched rows and insert them into the Treeview table
            for row in rows:
                table.insert("", "end", values=row)

        except mysql.connector.Error as err:
            print("Error:", err)

        finally:
            if db.is_connected():
                cur.close()
                cur.close()


def findCustomer():
    if csId.get() == '':
        messagebox.showerror('Error', 'Empty ID')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()
            query = "SELECT fName,lName,passport FROM customer WHERE cs_id = %s"
            val = (csId.get(),)
            cur.execute(query, val)
            record = cur.fetchone()

            if record is None:
                messagebox.showinfo("Message", "Not Found ")
                csId.delete(0, 'end')
                FirstN.config(text='')
                LastN.config(text='')
                PassNum.config(text='')
            else:
                FirstN.config(text=record[0])
                LastN.config(text=record[1])
                PassNum.config(text=record[2])

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
        finally:
            if db.is_connected():
                cur.close()
                db.close()


def update_total_price(*args):
    # Assume 'current_base_price' holds the base price for one seat of the selected class
    # Check if the base price is a digit and get the number of seats
    if priceLab.cget("text"):
        current_base_price = int(priceLab.cget("text"))
        num_seats = int(seatsSpin.get())
        total_price = current_base_price * num_seats
        totalLab.config(text=total_price)
    else:
        totalLab.config(text="0")


def book_ticket():
    # Collect data
    flight_number = FliNumLab.cget("text")
    customer_id = csId.get()
    flight_class = clasChoosen.get()
    price = priceLab.cget("text")
    seats = seatsSpin.get()  # Assuming seatsSpin is your Spinbox for the number of seats
    date = Date.cget("text")

    if price:
        price = int(price)

    else:
        price = 0  # Default to 0 if there's an issue

    if csId.get() == '' or flight_number == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    else:
        try:
            db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
            cur = db.cursor()

            # Prepare SQL query to insert a record into the database.
            query = ("INSERT INTO ticket ( flight_id, cs_id, class, price, seats, date) "
                     "VALUES ( %s, %s, %s, %s, %s, %s)")
            values = (flight_number, customer_id, flight_class, price, seats, date)

            cur.execute(query, values)
            db.commit()

            messagebox.showinfo("Success", "Ticket booked successfully!")
            for item in table.get_children():
                table.delete(item)
            srcChoosen.delete(0, 'end')
            depChoosen.delete(0, 'end')
            clasChoosen.current(0)
            csId.delete(0, 'end')
            FirstN.config(text='')
            LastN.config(text='')
            PassNum.config(text='')
            FliNumLab.config(text="")
            FliNameLab.config(text="")
            depTimeLab.config(text="")
            Date.config(text="")
            priceLab.config(text="")
            totalLab.config(text="")
            tkNumEntry.config(text=autoId())

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to book ticket: {err}")
        finally:
            if db.is_connected():
                cur.close()
                db.close()


def book_and_update_price():
    # Update the total price first
    update_total_price()
    open_payment_window()


def on_flight_selected(event):
    FliNumLab.config(text="")
    FliNameLab.config(text="")
    depTimeLab.config(text="")
    Date.config(text="")
    priceLab.config(text="")

    for selected_item in table.selection():
        item = table.item(selected_item)
        flight_data = item['values']
        if flight_data:
            FliNumLab.config(text=flight_data[0])
            FliNameLab.config(text=flight_data[1])
            depTimeLab.config(text=flight_data[5])
            Date.config(text=flight_data[4])
            priceLab.config(text=flight_data[7])
            # Update other labels as needed


def update_price(event):
    # Sample prices for demonstration; you might retrieve these from the database or another source
    for selected_item in table.selection():
        item = table.item(selected_item)
        flight_data = item['values']
        if flight_data:
            price = int(flight_data[7])

    class_prices = {
        'Economy': 0,
        'Premium Economy': 50,
        'Business': 100,
        'First class': 200
    }
    selected_class = clasChoosen.get()  # Get the currently selected class from the Combobox
    appdatePrice = class_prices.get(selected_class,
                                    0) + price  # Get the price for the selected class, default to 0 if not found
    priceLab.config(text=appdatePrice)


def autoId():
    try:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='airline')
        cur = db.cursor()

        cur.execute("ALTER TABLE ticket AUTO_INCREMENT = 1")
        db.commit()

        cur.execute("SELECT MAX(tkNum) FROM ticket")
        rs = cur.fetchone()[0]
        if rs is None:
            tkNum = 1
            return tkNum
        else:
            num = rs + 1
            tkNum = num
            return tkNum

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if db.is_connected():
            cur.close()
            db.close()


root = Tk()
root.title("Book Tickets")
root.geometry('1540x780+0+0')  # use geometry method to set width 1350 and height 700 from x 0 and y 0
root.resizable(False, False)
root.configure(bg="sky blue")
# ************************************************************************************************
tkNum = Label(root, text="Ticket Num", font=("times new roman", 17, 'bold'), bg='sky blue', fg='black', anchor="w")
tkNum.place(x=70, y=20)

tkNumEntry = Label(root, text=autoId(), font=('times new roman', 22, 'bold'), bg='sky blue', fg='red', anchor=CENTER,
                   width=5)
tkNumEntry.place(x=70, y=50)
# ************************************************************************************************

head_frame = Frame(root, bg='#f0f0f0', bd=4, relief='ridge')
head_frame.place(x=228, y=20, width=600, height=300)

label1 = Label(head_frame, text="Select Country", font=('times new roman', 22, 'bold'), bg='#f0f0f0')
label1.place(x=190, y=30)

label2 = Label(head_frame, text="Source: ", font=('times new roman', 17), bg='#f0f0f0')
label2.place(x=70, y=100)

n = StringVar()
srcChoosen = ttk.Combobox(head_frame, font=('times new roman', 15), width=25, textvariable=n)

country_names = [
    'USA', 'UK', 'France', 'Germany', 'Japan', 'Australia', 'Canada',
    'Saudi Arabia', 'United Arab Emirates', 'Egypt', 'Jordan', 'Iraq', 'Kuwait', 'Qatar', 'Oman', 'Bahrain']
# Adding combobox drop down list
srcChoosen['values'] = country_names

srcChoosen.place(x=210, y=100)
srcChoosen.current()

label3 = Label(head_frame, text="Departure: ", font=('times new roman', 17), bg='#f0f0f0')
label3.place(x=70, y=150)

n1 = StringVar()
depChoosen = ttk.Combobox(head_frame, font=('times new roman', 15), width=25, textvariable=n1)

# Adding combobox drop down list
depChoosen['values'] = country_names

depChoosen.place(x=210, y=150)
depChoosen.current()

button = Button(head_frame, text="Search", font=('times new roman', 17, 'bold'), bg='#f7faf7', fg='black',
                activebackground='red', activeforeground='white', command=searchFlight)
button.place(x=390, y=210)

# *************************************  SECOND FRAME  *******************************************
head_frame1 = Frame(root, bg='#f0f0f0', bd=4, relief='ridge')
head_frame1.place(x=850, y=20, width=600, height=300)

# ************************************  CsId   ************************************************5***************
csId = Label(head_frame1, text='Customer ID ', font=('times new roman', 14, 'bold'), bg='#f0f0f0')
csId.grid(row=1, column=0, pady=15, padx=4)

csId = Entry(head_frame1, font=('times new roman', 15), bg="white", fg="red", bd=3, width=25)
csId.grid(row=1, column=1, pady=15, padx=4)

# **************************** First Name ***********************************************************************
FirstN = Label(head_frame1, text="First Name", bg="#f0f0f0", font=("times new roman", 14, 'bold'))
FirstN.grid(row=2, column=0, pady=15, padx=4)

FirstN = Label(head_frame1, font=('times new roman', 15), bg='#f0f0f0', bd=2, fg='black', width=20, anchor='w')
FirstN.grid(row=2, column=1, pady=15, padx=4)

# ************************************* Last Name *******************************************
LastN = Label(head_frame1, text="Last Name", bg="#f0f0f0", font=("times new roman", 14, 'bold'))
LastN.grid(row=3, column=0, pady=15, padx=4)

LastN = Label(head_frame1, font=('times new roman', 15), bg='#f0f0f0', bd=2, fg='black', width=20, anchor='w')
LastN.grid(row=3, column=1, pady=15, padx=4)
# ************************************* Passport Num *******************************************
PassNum = Label(head_frame1, text="Passport ", bg="#f0f0f0", font=("times new roman", 15, 'bold'))
PassNum.grid(row=4, column=0, pady=15, padx=4)

PassNum = Label(head_frame1, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=20, anchor='w')
PassNum.grid(row=4, column=1, pady=15, padx=4)

button1 = Button(head_frame1, text="Search", font=('times new roman', 16, 'bold'), bg='#f7faf7', fg='black',
                 activebackground='red', activeforeground='white', command=findCustomer)
button1.grid(row=1, column=4, padx=15, pady=20)

# *************************************  THIRD FRAME  *******************************************

table = ttk.Treeview(root, columns=(
    "flight_id", "fName", "source", "departure", "date", "depTime", "arrTime", "flightCharge"),
                     show="headings")
table.column("flight_id", width=70)
table.heading("flight_id", text="Flight Number")

table.column("fName", width=70)
table.heading("fName", text="Flight Name")

table.column("source", width=60)
table.heading("source", text="Source")

table.column("departure", width=60)
table.heading("departure", text="Departure")

table.column("date", width=60)
table.heading("date", text="Date")

table.column("depTime", width=70)
table.heading("depTime", text="Departure Time")

table.column("arrTime", width=60)
table.heading("arrTime", text="Arrival Time")

table.column("flightCharge", width=60)
table.heading("flightCharge", text="Charge $")
table.place(x=30, y=340, width=800, height=320)

table.bind('<<TreeviewSelect>>', on_flight_selected)

# ***********************************************************************************************************************
head_frame2 = Frame(root, bg='#f0f0f0', bd=4, relief='ridge')
head_frame2.place(x=850, y=340, width=600, height=320)

# ************************************  Flight Number   ***************************************************************
FliNum = Label(head_frame2, text='Flight Number', font=('times new roman', 14, 'bold'), bg='#f0f0f0')
FliNum.place(x=10, y=10)

FliNumLab = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=15
                  , anchor='w')
FliNumLab.place(x=140, y=10)

# ************************************  Flight Name   ***************************************************************
FliName = Label(head_frame2, text='Flight Name ', font=('times new roman', 14, 'bold'), bg='#f0f0f0')
FliName.place(x=10, y=50)

FliNameLab = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=15, anchor='w')
FliNameLab.place(x=140, y=50)

# ************************************* Last Name *******************************************
depTime = Label(head_frame2, text="Departure Time", bg="#f0f0f0", font=("times new roman", 14, 'bold'))
depTime.place(x=10, y=90)

depTimeLab = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=15, anchor='w')
depTimeLab.place(x=140, y=90)
# ************************************* Date *******************************************
Date = Label(head_frame2, text="Date", bg="#f0f0f0", font=("times new roman", 14, 'bold'))
Date.place(x=10, y=130)

Date = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=15, anchor='w')
Date.place(x=140, y=130)
# ************************************* Class *******************************************
clas = Label(head_frame2, text="Class ", font=('times new roman', 14, 'bold'), bg='#f0f0f0')
clas.place(x=10, y=170)

n = StringVar()
clasChoosen = ttk.Combobox(head_frame2, font=('times new roman', 14), width=22, textvariable=n)

claa_names = ['Economy', 'Premium Economy', 'Business', 'First class']
# Adding combobox drop down list
clasChoosen['values'] = claa_names

clasChoosen.place(x=140, y=170)
clasChoosen.current(0)

clasChoosen.bind('<<ComboboxSelected>>', update_price)
# ************************************* Price *******************************************
price = Label(head_frame2, text="Price", bg="#f0f0f0", font=("times new roman", 14, 'bold'))
price.place(x=10, y=220)

priceLab = Label(head_frame2, font=('times new roman', 14), bg='#f0f0f0', bd=2, fg='black', width=8, anchor='w')
priceLab.place(x=140, y=220)
# ************************************* Seats *******************************************
seats = Label(head_frame2, text="Seats", bg="#f0f0f0", font=("times new roman", 14, 'bold'))
seats.place(x=10, y=250)

seatsSpin = Spinbox(head_frame2, from_=1, to=4, font=('times new roman', 14), width=23)
seatsSpin.place(x=140, y=250)

# **************************************total***************************************************
total = Label(root, text="Total Price: ", bg='sky blue', font=("times new roman", 18, 'bold'), fg='red')
total.place(x=460, y=670)

totalLab = Label(root, bg='sky blue', font=("times new roman", 18, 'bold'), fg='red')
totalLab.place(x=590, y=670)

# *********************Button********************************************************************
bookButton = Button(root, text='Book', font=('times new roman', 15, 'bold'), bg='gray87', fg='red',
                    activebackground='white', activeforeground='black', cursor='hand2', width=8, bd=3,
                    command=book_and_update_price)

bookButton.place(x=1200, y=680)

BkButton = Button(root, text='Cancel', font=('times new roman', 15, 'bold'), bg='gray87', fg='black',
                  activebackground='white', activeforeground='black', cursor='hand2', width=8, bd=3,
                  command=Exitt)

BkButton.place(x=1340, y=680)

root.mainloop()
