from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
from datetime import date
import mysql.connector as mysql

today = date.today()

class Payroll:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll System")
        self.root.geometry("1366x768+0+0")

        self.root.config(bg = "powderblue")
        label_1 = Label(self.root, text = "Payroll Management System", font = ("Elephant", 27), bg = "orange").place(x = 0, y = 0, relwidth = 1)

        frame2 = Frame(self.root, relief=RIDGE, bg = "light green", bd=5)
        frame2.place(x = 20, y = 70, width = 620, height = 570)

        label = Label(self.root, text = "Employee Details", font = ("times new roman", 32, "italic", "bold"), bg = "honeydew3").place(x = 165, y = 100, relwidth = 0.25)

        empid = Label(self.root, text = "Employee ID", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        empid.place(x = 60, y =180, relheight = 0.06)
        self.txt_empid = Entry(self.root, width = 8, font = ("calibri", 18))
        self.txt_empid.place(x = 219, y =180, relheight = 0.055)

        doj = Label(self.root, text = "DOJ", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        doj.place(x = 400, y =180, relheight = 0.06)
        self.txt_doj = Entry(self.root, width = 10, font = ("calibri", 18))
        self.txt_doj.place(x = 465, y =180, relheight = 0.055)

        name = Label(self.root, text = "Name", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        name.place(x = 60, y =245, relheight = 0.06)
        self.txt_name = Entry(self.root, width = 18, font = ("calibri", 18))
        self.txt_name.place(x = 138, y =245, relheight = 0.055)

        dob = Label(self.root, text = "DOB", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        dob.place(x = 400, y =245, relheight = 0.06)
        self.txt_dob = Entry(self.root, width = 10, font = ("calibri", 18))
        self.txt_dob.place(x = 469, y =245, relheight = 0.055)

        age = Label(self.root, text = "Age", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        age.place(x = 60, y =315, relheight = 0.06)
        self.txt_age = Entry(self.root, width = 3, font = ("calibri", 18))
        self.txt_age.place(x = 115, y =315, relheight = 0.055)

        exp = Label(self.root, text = "Experience", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        exp.place(x = 300, y =315, relheight = 0.06)
        self.txt_exp = Entry(self.root, width = 13, font = ("calibri", 18))
        self.txt_exp.place(x = 439, y =315, relheight = 0.055)

        gender = Label(self.root, text = "Gender", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        gender.place(x = 60, y =385, relheight = 0.06)
        self.txt_gender = Entry(self.root, width = 6, font = ("calibri", 18))
        self.txt_gender.place(x = 155, y =385, relheight = 0.055)

        proof = Label(self.root, text = "Proof ID", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        proof.place(x = 400, y =385, relheight = 0.06)
        self.txt_proof = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_proof.place(x = 513, y =385, relheight = 0.055)

        email = Label(self.root, text = "Email", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        email.place(x = 60, y =455, relheight = 0.06)
        self.txt_email = Entry(self.root, width = 15, font = ("calibri", 18))
        self.txt_email.place(x = 140, y =455, relheight = 0.055)

        contact = Label(self.root, text = "Contact No", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        contact.place(x = 350, y =455, relheight = 0.06)
        self.txt_contact = Entry(self.root, width = 10, font = ("calibri", 18))
        self.txt_contact.place(x = 491, y =455, relheight = 0.055)

        addr = Label(self.root, text = "Address", bg = "orange", fg = "black", font = ("times new roman", 20, "italic", "bold"))
        addr.place(x = 60, y =525, relheight = 0.06)
        self.txt_addr = Entry(self.root, width = 38, font = ("calibri", 18))
        self.txt_addr.place(x = 162, y =525, relheight = 0.055, height = 70)

        def clear():
            self.txt_empid.delete(0, "end")
            self.txt_doj.delete(0, "end")
            self.txt_name.delete(0, "end")
            self.txt_hour.delete(0, "end")
            self.txt_days.delete(0, "end") 
            self.txt_basic.delete(0, "end")
            self.txt_gross.delete(0, "end")
            self.txt_medical.delete(0, "end")
            self.txt_bonus.delete(0, "end")
            self.txt_tax.delete(0, "end")
            self.txt_salary.delete(0, "end")

        def calculate():
            self.txt_basic.insert(0, int(self.txt_hour.get())*int(self.txt_gross.get()))
            self.txt_salary.insert(0, int(self.txt_basic.get())-int(self.txt_medical.get())-(int(self.txt_basic.get())*(int(self.txt_tax.get())/100))+int(self.txt_bonus.get()))

        frame3 = Frame(self.root, relief=RIDGE, bg = "light pink", bd=5)
        frame3.place(x = 660, y = 70, width = 605, height = 300)

        hour = Label(self.root, text = "Hour", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        hour.place(x = 690, y =100, relheight = 0.045)
        self.txt_hour = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_hour.place(x = 755, y =100, relheight = 0.04)

        days = Label(self.root, text = "Days", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        days.place(x = 865, y =100, relheight = 0.045)
        self.txt_days = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_days.place(x = 925, y =100, relheight = 0.04)

        basic = Label(self.root, text = "Basic Salary", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        basic.place(x = 1045, y =100, relheight = 0.045)
        self.txt_basic = Entry(self.root, width = 6, font = ("calibri", 18))
        self.txt_basic.place(x = 1181, y =100, relheight = 0.04)

        gross = Label(self.root, text = "Gross Pay Rate/Hour", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        gross.place(x = 690, y =140, relheight = 0.045)
        self.txt_gross = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_gross.place(x = 915, y =140, relheight = 0.04)

        medical = Label(self.root, text = "Medical", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        medical.place(x = 730, y =200, relheight = 0.045)
        self.txt_medical = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_medical.place(x = 823, y =200, relheight = 0.04)

        bonus = Label(self.root, text = "Bonus", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        bonus.place(x = 990, y =200, relheight = 0.045)
        self.txt_bonus = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_bonus.place(x = 1065, y =200, relheight = 0.04)

        tax = Label(self.root, text = "Tax(%)", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        tax.place(x = 730, y =250, relheight = 0.045)
        self.txt_tax = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_tax.place(x = 815, y =250, relheight = 0.04)

        salary = Label(self.root, text = "Net Salary", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        salary.place(x = 990, y =250, relheight = 0.045)
        self.txt_salary = Entry(self.root, width = 8, font = ("calibri", 18))
        self.txt_salary.place(x = 1106, y =250, relheight = 0.04)

        button_1 = Button(self.root, text = "Calculate", font = ("times new roman", 20), bg = "yellow", activebackground = "magenta", bd = 5, command = calculate)
        button_1.place(x = 790, y = 300, width = 140, height = 40, relheight = 0)
        
        button_2 = Button(self.root, text = "Clear", font = ("times new roman", 20), bg = "yellow", activebackground = "magenta", bd = 5, command = clear)
        button_2.place(x = 990, y = 300, width = 140, height = 40, relheight = 0)

        def printreceipt():
            sample = f'''\t\t        Company name: Payroll Management\n\t\t        Address: LPU, Phagwara, Punjab
----------------------------------------------------------------------------------
  Employee ID\t\t :{self.txt_empid.get()}
  Employee Name\t\t :{self.txt_name.get()}
  Generated On\t\t :{today}
----------------------------------------------------------------------------------
  Basic Salary\t\t :{self.txt_basic.get()}
  Total Days\t\t :{self.txt_days.get()}
  Medical\t\t :{self.txt_medical.get()}
  Bonus\t\t :{self.txt_bonus.get()}
  Tax\t\t :{self.txt_tax.get()}%
----------------------------------------------------------------------------------
  Net Salary\t\t :{self.txt_salary.get()}'''

            scroll_y = Scrollbar(frame4, orient = VERTICAL)
            scroll_y.pack(fill=Y, side=RIGHT)

            self.txt_sal_receipt = Text(frame4, font = ("times new roman", 15), bg = "lightyellow")
            self.txt_sal_receipt.pack(fill = BOTH, expand=1)
            scroll_y.config(command = self.txt_sal_receipt.yview)
            self.txt_sal_receipt.insert(END, sample)

            try:
                mysql_con = mysql.connect(host = 'localhost', user = 'root', password = 'rajesh123', database = 'payroll')
                if mysql_con.is_connected():
                    print("Successfully Connected to MySQL Database")
                cur = mysql_con.cursor()
                qr1 = "Insert into payroll(empid, name, doj, basic, medical, bonus, tax, salary)"
                qr2 = "values({}, '{}', '{}', {}, {}, {}, {}, {})".format(self.txt_empid.get(), self.txt_name.get(), self.txt_doj.get(), self.txt_basic.get(), self.txt_medical.get(), self.txt_bonus.get(), self.txt_tax.get(), self.txt_salary.get())
                qr = qr1+qr2
                cur.execute(qr)
                mysql_con.commit()
                messagebox.showinfo("Save", "Record Successfully Saved", parent = self.root)
                mysql_con.close()

            except:
                messagebox.showinfo("Error", "MySQL Data write error!!!", parent = self.root)

        frame4 = Frame(self.root, relief=RIDGE, bg = "light yellow", bd=5)
        frame4.place(x = 660, y = 410, width = 605, height = 225)

        sal = Label(self.root, text = "Salary Details", bg = "red", fg = "black", font = ("times new roman", 25, "italic", "bold"))
        sal.place(x = 870, y =375, relheight = 0.048)

        button_3 = Button(self.root, text = "Print Receipt", font = ("times new roman", 17), bg = "blueviolet", activebackground = "magenta", bd = 3, command = printreceipt)
        button_3.place(x = 1110, y = 372, width = 150, height = 35, relheight = 0)

        button_4 = Button(self.root, text = "Update", font = ("times new roman", 17), bg = "blueviolet", activebackground = "magenta", bd = 3, command = self.update)
        button_4.place(x = 670, y = 372, width = 150, height = 35, relheight = 0)

    def update(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Updation of Salary")

        self.root.config(bg = "powderblue")
        label1 = Label(self.root, text = "Update Salary", bg = "pink", fg = "black", font = ("times new roman", 35, "bold")).place(x=0, y=0, relwidth = 1)

        frame2 = Frame(self.root, relief=RIDGE, bd=3)
        frame2.place(x = 20, y = 80, width = 770, height = 350)

        def find_rec():
            try:
                mysql_con = mysql.connect(host = 'localhost', user = 'root', passwd = 'rajesh123', database = 'payroll')
                if mysql_con.is_connected():
                    print("Successfully Connected to MySQL Database")
                cur = mysql_con.cursor()
                qr = "Select * from payroll where empid = {}".format(self.txt_empid.get())
                cur.execute(qr)
                rows = cur.fetchall()
                f = ('calibri', 15, 'bold')

                for row in rows:
                    self.txt_empid.insert(0, row[0])
                    self.txt_name.insert(0, row[1])
                    self.txt_doj.insert(0, row[2])
                    self.txt_basic.insert(0, row[3])
                    self.txt_medical.insert(0, row[4])
                    self.txt_bonus.insert(0, row[5])
                    self.txt_tax.insert(0, row[6])
                    self.txt_salary.insert(0, row[7])

            except:
                messagebox.showinfo("Error", "MySQL Data write error!!!", parent = self.root)

        def save_rec():
            try:
                mysql_con = mysql.connect(host = 'localhost', user = 'root', passwd = 'rajesh123', database = 'payroll')
                if mysql_con.is_connected():
                    print("Successfully Connected to MySQL Database")
                cur = mysql_con.cursor()
                qr = "Update payroll set empid = {}, name = '{}', doj = '{}', basic = {}, medical = {}, bonus = {}, tax = {}, salary = {} where empid = {};".format(self.txt_empid.get(), self.txt_name.get(), self.txt_doj.get(), self.txt_basic.get(), self.txt_medical.get(), self.txt_bonus.get(), self.txt_tax.get(), self.txt_salary.get(), self.txt_empid.get())
                cur.execute(qr)
                mysql_con.commit()
                messagebox.showinfo("Saved", "Record Successfully Updated", parent = self.root)

            except:
                messagebox.showinfo("Error", "Error in updation", parent = self.root)

        def delete_rec():
            try:
                mysql_con = mysql.connect(host = 'localhost', user = 'root', passwd = 'rajesh123', database = 'payroll')
                if mysql_con.is_connected():
                    print("Successfully Connected to MySQL Database")
                cur = mysql_con.cursor()
                qr = "Delete from payroll where empid = {};".format(self.txt_empid1.get())
                cur.execute(qr)
                mysql_con.commit()
                messagebox.showinfo("Delete", "Record Successfully Deleted", parent = self.root)

            except:
                messagebox.showinfo("Error", "Error in deletion", parent = self.root)

        update = Label(self.root, text = "Update Record from here", bg = "red", fg = "black", font = ("times new roman", 23, "bold"))
        update.place(x = 50, y =95, relheight = 0.048)

        empid = Label(self.root, text = "Employee ID", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        empid.place(x = 50, y =150, relheight = 0.045)
        self.txt_empid = Entry(self.root, width = 8, font = ("calibri", 18))
        self.txt_empid.place(x = 190, y =150, relheight = 0.04)

        doj = Label(self.root, text = "DOJ", bg = "orange", fg = "black", font = ("times new roman", 18, "italic","bold"))
        doj.place(x = 350, y =150, relheight = 0.045)
        self.txt_doj = Entry(self.root, width = 9, font = ("calibri", 18))
        self.txt_doj.place(x = 405, y =150, relheight = 0.04)

        name = Label(self.root, text = "Name", bg = "orange", fg = "black", font = ("times new roman", 18, "italic","bold"))
        name.place(x = 50, y =205, relheight = 0.045)
        self.txt_name = Entry(self.root, width = 18, font = ("calibri", 18))
        self.txt_name.place(x = 118, y =205, relheight = 0.04)

        basic = Label(self.root, text = "Basic Salary", bg = "orange", fg = "black", font = ("times new roman", 18,"italic", "bold"))
        basic.place(x = 560, y =150, relheight = 0.045)
        self.txt_basic = Entry(self.root, width = 6, font = ("calibri", 18))
        self.txt_basic.place(x = 700, y =150, relheight = 0.04)

        medical = Label(self.root, text = "Medical", bg = "orange", fg = "black", font = ("times new roman", 18,"italic", "bold"))
        medical.place(x = 370, y =205, relheight = 0.045)
        self.txt_medical = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_medical.place(x = 463, y =205, relheight = 0.04)

        bonus = Label(self.root, text = "Bonus", bg = "orange", fg = "black", font = ("times new roman", 18,"italic", "bold"))
        bonus.place(x = 600, y =205, relheight = 0.045)
        self.txt_bonus = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_bonus.place(x = 675, y =205, relheight = 0.04)

        tax = Label(self.root, text = "Tax(%)", bg = "orange", fg = "black", font = ("times new roman", 18,"italic", "bold"))
        tax.place(x = 50, y =260, relheight = 0.045)
        self.txt_tax = Entry(self.root, width = 5, font = ("calibri", 18))
        self.txt_tax.place(x = 135, y =260, relheight = 0.04)

        salary = Label(self.root, text = "Net Salary", bg = "orange", fg = "black", font = ("times new roman", 18,"italic", "bold"))
        salary.place(x = 300, y =260, relheight = 0.045)
        self.txt_salary = Entry(self.root, width = 8, font = ("calibri", 18))
        self.txt_salary.place(x = 416, y =260, relheight = 0.04)

        button_5 = Button(self.root, text = "Find Record", font = ("times new roman", 17), bg = "blueviolet", activebackground = "magenta", bd = 3, command = find_rec)
        button_5.place(x = 200, y = 340, width = 150, height = 35, relheight = 0)

        button_6 = Button(self.root, text = "Update Record", font = ("times new roman", 17), bg = "blueviolet", activebackground = "magenta", bd = 3, command = save_rec)
        button_6.place(x = 400, y = 340, width = 150, height = 35, relheight = 0)

        frame3 = Frame(self.root, relief=RIDGE, bd=3)
        frame3.place(x = 20, y = 450, width = 770, height = 130)

        delete = Label(self.root, text = "Delete Record from here", bg = "red", fg = "black", font = ("times new roman", 23, "bold"))
        delete.place(x = 50, y =465, relheight = 0.048)

        empid1 = Label(self.root, text = "Employee ID", bg = "orange", fg = "black", font = ("times new roman", 18, "italic", "bold"))
        empid1.place(x = 50, y =520, relheight = 0.045)
        self.txt_empid1 = Entry(self.root, width = 8, font = ("calibri", 18))
        self.txt_empid1.place(x = 190, y =520, relheight = 0.04)

        button_7 = Button(self.root, text = "Delete Record", font = ("times new roman", 17), bg = "blueviolet", activebackground = "magenta", bd = 3, command = delete_rec)
        button_7.place(x = 500, y = 520, width = 150, height = 35, relheight = 0)
                   
#Class call
root = Tk()
obj=Payroll(root)
root.mainloop()

