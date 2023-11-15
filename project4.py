from tkinter import *
from tkinter.messagebox import *
from pymongo import MongoClient
from tkinter.scrolledtext import *
import matplotlib.pyplot as plt
import re
from requests import *


def temperauture5():
    url = "https://api.openweathermap.org/data/2.5/weather?q=kalyan&appid=b64af53b051f87a4e6457582c489b950"
    try:
       res = get(url)
       data = res.json()
       temper =  data['main']['temp']
       temper2 = temper - 273.15
       temperature01.configure(text=f"{temper2:.2f}°C")
    
    except Exception as e:
        showerror("Issue", e)
       
def loc():
    try:
        url = "https://ipinfo.io"
        res = get(url)
        data = res.json()
        city_name = data["city"]
        location_info = f"{city_name}"
        location1.configure(text=location_info)

    except Exception as e:
        showerror("Issue", e)

def vw():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["33oct"]
        col = db["employe"]
        data = col.find()
        view_emp_data.delete(1.0, END)
        view_emp_data.focus()

        for d in data:
            view_emp_data.insert(END, f"Employee ID: {d['_id']}\n")
            view_emp_data.insert(END, f"Employee Name: {d['name']}\n")
            view_emp_data.insert(END, f"Salary: {d['salary']}\n \n")
    except Exception as e:
        showerror("Error", e)
    finally:
        if con is not None:
            con.close()

def delete_1():
    try:
        con = MongoClient("localhost", 27017)
        db = con["33oct"]
        coll = db["employe"]
        emp_id1 = emp_id_btn123.get()

        if emp_id1 == "":
            showerror("Issue", "Do not keep the employee ID empty")
        elif any(char in "!@#$%^&*()/|" for char in emp_id1):
            showerror("Issue", "Do not enter the special characters in employee ID")
        elif not emp_id1.isdigit():
            showerror("Issue", "Do not enter alphabets in employee ID")
        else:
            count = coll.count_documents({"_id": emp_id1})
            if count == 1:
                coll.delete_one({"_id": emp_id1})
                showinfo("Info", "Employee Deleted")
            else:
                showinfo("Issue", "Employee with this ID not found")
        emp_id_btn123.delete(0, END)
        emp_id_btn123.focus()
    except Exception as e:
        showerror("Error", e)
    finally:
        if con is not None:
            con.close()

def adde():
    try:
        con = MongoClient("localhost", 27017)
        db = con["33oct"]
        coll = db["employe"]
        emp_id1 = emp_id_btnt.get()
        emp_name_btn1 = emp_name_btn.get()
        emp_salary_btn1 = emp_salary_btn.get()

        if emp_id1 == "":
            showerror("Issue", "Do not leave the employee ID empty")
        elif emp_name_btn1 == "":
            showerror("Issue", "Do not leave the employee name empty")
        elif emp_salary_btn1 == "":
            showerror("Issue", "Do not leave the employee salary empty")
        elif re.search(r'[!@#$%^&*()]', emp_id1):
            showerror("Issue", "Special characters are not allowed in employee ID")
        elif not emp_id1.isdigit():
            showerror("Issue", "Do not enter alphabets in employee ID")
        elif re.search(r'[!@#$%^&*()/|]', emp_name_btn1):
            showerror("Issue", "Special characters are not allowed in employee name")
        elif re.search(r'[!@#$%^&*()/|]', emp_salary_btn1):
            showerror("Issue", "Special characters are not allowed in employee salary")
        elif not emp_salary_btn1.isdigit():
            showerror("Issue", "Do not enter alphabets in the employee salary")
        elif emp_name_btn1.isdigit():
            showerror("Issue", "Employee Name should not contain numbers")
        elif coll.find_one({"_id": emp_id1}):
            showinfo("Employee Exists", "Employee already exists")
        else:
            doc = {"_id": emp_id1, "name": emp_name_btn1, "salary": emp_salary_btn1}
            coll.insert_one(doc)
            showinfo("Created", "Record Created")

        emp_id_btnt.delete(0, END)
        emp_name_btn.delete(0, END)
        emp_salary_btn.delete(0, END)
        emp_id_btnt.focus()

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

def f1():
    root.withdraw()
    add.deiconify()

def f2():
    root.withdraw()
    view.deiconify()

def f3():
    root.withdraw()
    update.deiconify()

def f4():
    root.withdraw()
    delete.deiconify()

def f6():
    add.withdraw()
    root.deiconify()

def f7():
    view.withdraw()
    root.deiconify()

def f8():
    update.withdraw()
    root.deiconify()

def f9():
    delete.withdraw()
    root.deiconify()

def f10():
    root.withdraw()
    chart.deiconify()

root = Tk()
root.title("Employee Management")
root.geometry("1000x1000+50+50")
f = ("Arial", 30, "bold")

add_btn = Button(root, text="ADD", font=f, command=f1)
add_btn.pack(pady=5)
view_btn = Button(root, text="View", font=f, command=f2)
view_btn.pack(pady=5)
update_btn = Button(root, text="Update", font=f, command=f3)
update_btn.pack(pady=5)
delete_btn = Button(root, text="Delete", font=f, command=f4)
delete_btn.pack(pady=5)
chart_btn = Button(root, text="Charts", font=f, command=f10)
chart_btn.pack(pady=5)
location = Label(root, text="Location:", font=f)
location.place(y=550, x=20)
location1 = Label(root, font=f, wraplength=500)
location1.place(y=550, x=220)
loc()
temperature00 = Label(root, text="Temperature:", font=f)
temperature00.place(y=550, x=500)
temperature01 = Label(root, font=f, wraplength=500)
temperature01.place(y=550, x=760)
temperauture5()


add = Tk()
add.title("Add Employee")
add.geometry("600x600+50+50")

emp_id = Label(add, text="Enter the employee id", font=f)
emp_id_btnt = Entry(add, font=f)
emp_name = Label(add, text="Enter employee name", font=f)
emp_name_btn = Entry(add, font=f)
emp_salary = Label(add, text="Enter employee salary (in LPA)", font=f)
emp_salary_btn = Entry(add, font=f)
add1 = Button(add, text="Save", font=f, command=adde)
backa = Button(add, text="Back", font=f, command=f6)
emp_id.pack(pady=5)
emp_id_btnt.pack(pady=5)
emp_name.pack(pady=5)
emp_name_btn.pack(pady=5)
emp_salary.pack(pady=5)
emp_salary_btn.pack(pady=5)
add1.pack(pady=5)
backa.pack(pady=5)
add.withdraw()

view = Tk()
view.title("View Employee")
view.geometry("600x700+50+50")

view_emp_data = ScrolledText(view, font=f, width=30, height=8)
view_btnllp = Button(view, text="View", font=f, command=vw)
backb = Button(view, text="Back", font=f, command=f7)
view_emp_data.pack(pady=5)
view_btnllp.pack(pady=5)
backb.pack(pady=5)
view.withdraw()

update = Tk()
update.title("Update Employee")
update.geometry("600x600+50+50")

def update_emp():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["33oct"]
        col = db["employe"]

        empid = emp_id_btn66.get()
        empname = emp_nameooo_btn.get()
        empsalary = emp_salary_btnc.get()

        if empid == "":
            showerror("Issue", "Do not leave the employee Id empty")
        elif empname == "":
            showerror("Issue", "Do not leave the employee name empty")
        elif empsalary == "":
            showerror("Issue", "Do not leave the employee salary empty")
        elif (empid == "") or (empname == "") or (empsalary == ""):
            showerror("Issue", "Do not leave any of the employee details empty")
        elif any(char in "!@#$%^&*()" for char in empsalary):
            showerror("Issue", "Do not enter special characters in employee salary")
        elif any(char in "!@#$%^&*()" for char in empname):
            showerror("Issue", "Do not enter special characters in employee name")
        elif any(char in "!@#$%^&*()" for char in empid):
            showerror("Issue", "Do not enter special characters in employee ID")
        elif not empid.isdigit():
            showerror("Issue", "Do not enter alphabets in employee ID")
        elif not empname.isalpha():
            showerror("Issue", "Do not enter numbers in employee name")
        elif not empsalary.isdigit():
            showerror("Issue", "Do not enter alphabets in the employee salary")
        else:
            existing_employee = col.find_one({"_id": empid})
            if existing_employee:
                col.update_one({"_id": empid}, {"$set": {"name": empname, "salary": empsalary}})
                showinfo("Updated", "Employee details updated successfully")
            else:
                showinfo("Issue", "Employee not found")

        emp_id_btn66.delete(0, END)
        emp_nameooo_btn.delete(0, END)
        emp_salary_btnc.delete(0, END)
        emp_id_btn66.focus()
    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

emp_id = Label(update, text="Enter the employee id", font=f)
emp_id_btn66 = Entry(update, font=f)
emp_nameooo = Label(update, text="Enter employee name", font=f)
emp_nameooo_btn = Entry(update, font=f)
emp_salary = Label(update, text="Enter employee salary (in LPA)", font=f)
emp_salary_btnc = Entry(update, font=f)
update1 = Button(update, text="Update", font=f, command=update_emp)
backc = Button(update, text="Back", font=f, command=f8)
emp_id.pack()
emp_id_btn66.pack()
emp_nameooo.pack(pady=5)
emp_nameooo_btn.pack(pady=5)
emp_salary.pack()
emp_salary_btnc.pack()
update1.pack()
backc.pack(pady=5)
update.withdraw()

delete = Tk()
delete.title("Delete Employee")
delete.geometry("600x300+50+50")

emp_id_label = Label(delete, text="Enter the employee id", font=f)
emp_id_btn123 = Entry(delete, font=f)
emp_delete = Button(delete, text="Delete", font=f, command=delete_1)
backd = Button(delete, text="Back", font=f, command=f9)
emp_id_label.pack(pady=5)
emp_id_btn123.pack(pady=5)
emp_delete.pack(pady=5)
backd.pack(pady=5)
delete.withdraw()

def generate_chart():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["33oct"]
        col = db["employe"]
        top_employees = list(col.find().sort('salary', -1).limit(5))
        employee_names = [employee["name"] for employee in top_employees]
        employee_salaries = [int(employee["salary"]) for employee in top_employees]

        plt.bar(employee_names, employee_salaries)
        plt.xlabel("Employee Names")
        plt.ylabel("Salaries (in LPA)")
        plt.title("Top 5 Salaried Employees")
        plt.grid()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        showerror("Error:", e)
    finally:
        if con is not None:
            con.close()

def charts_back():
    chart.withdraw()
    root.deiconify()

chart = Tk()
chart.title("Top five salaried Employees")
chart.geometry("600x600+50+50")

show = Button(chart, text="Show Chart", font=f, command=generate_chart)
back121 = Button(chart, text="Back", font=f, command=charts_back)
show.pack(pady=5)
back121.pack(pady=5)
chart.withdraw()

def close():
    if askokcancel("Quit", "Do you want to exit?"):
        root.destroy()
        add.destroy()
        view.destroy()
        delete.destroy()
        update.destroy()
        chart.destroy()

root.protocol("WM_DELETE_WINDOW", close)
add.protocol("WM_DELETE_WINDOW", close)
view.protocol("WM_DELETE_WINDOW", close)
delete.protocol("WM_DELETE_WINDOW", close)
update.protocol("WM_DELETE_WINDOW", close)
chart.protocol("WM_DELETE_WINDOW", close)

root.mainloop()
