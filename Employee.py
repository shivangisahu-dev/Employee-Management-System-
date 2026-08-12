from tkinter import *
from add_employee import Employee_manager
from delete_page import Delete_employee
from searching_profile  import Searching_employee
from salary import Employee_Salary
from updating_profile import update_employee
from view_profile import view_all_employee
from PIL import Image,ImageTk
def Employee_dashboard(root):
    root.withdraw()
    root1=Toplevel(root)
    root1.title("Employee Management System")
    root1.geometry("1280x720")
    root1.config(bg="#EEF4FA")
    root1.resizable(False, False)

#     # ================= HEADER =================

    Label(
        root1,
        text="EMPLOYEE MANAGEMENT SYSTEM",
        font=("Segoe UI", 22, "bold"),
        bg="#1F4E79",
        fg="white",
        pady=15
    ).pack(fill=X)

    Label(
        root1,
        text="Employee Dashboard",
        font=("Segoe UI", 12),
        bg="#EEF4FA",
        fg="#5A6C7D"
    ).pack(pady=15)

    # ================= FUNCTIONS =================
    emp_manager=Employee_manager()
    emp1_manager=update_employee()
    emp2_manager=Searching_employee()
    emp3_manager=Delete_employee()
    emp4_manager=Employee_Salary()

    def add_func():
        emp_manager.add_employees(root1)

    def update_func():
        emp1_manager.update_employe(root1)

    def search_func():
        
        emp2_manager.searching_page(root1)

    def delete_func():
        emp3_manager.delete_page(root1)

    def salary_func():
        emp4_manager.salary_page(root1)

    def view_func():
        view_all_employee(root1)

    # ================= CARD FUNCTION =================

    def create_card(text, x, y, command):

        card = Frame(
            root1,
            bg="white",
            width=260,
            height=130,
            highlightbackground="#D6E0EA",
            highlightthickness=1
        )

        card.place(x=x, y=y)
        card.pack_propagate(False)

        btn = Button(
            card,
            text=text,
            font=("Segoe UI", 13, "bold"),
            bg="white",
            fg="#1F4E79",
            activebackground="#F5F9FF",
            activeforeground="#1F4E79",
            bd=0,
            cursor="hand2",
            command=command
        )

        btn.pack(expand=True, fill="both")

    # ================= DASHBOARD CARDS =================

    create_card("Add Employee",      180, 140, add_func)
    create_card("Update Employee",   500, 140, update_func)

    create_card("Search Employee",   180, 310, search_func)
    create_card("Delete Employee",   500, 310, delete_func)

    create_card("View All\nemployees",  180, 480, view_func)
    create_card("Calculate Salary",     500,480,  salary_func)
    #===================IMAGE========================
    photo=Image.open(r"C:\Users\DELL\Desktop\python\Employye\omg.jpg")
    photo=photo.resize((470,480),Image.LANCZOS)
    photo1=ImageTk.PhotoImage(photo)

    l1=Label(root1,
          image=photo1,
          bg="#EEF4FA")
    l1.image=photo1
    l1.place(x=770,y=130)

    # ================= FOOTER ================= 

    Label(
        root1,
        text="Employee Management System © 2025",
        font=("Segoe UI", 9),
        bg="#EEF4FA",
        fg="gray"
    ).place(x=520, y=685)