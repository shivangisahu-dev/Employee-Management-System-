from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Employee_Salary:

    def __init__(self):
        self.create_Database()


    # =========================================================
    # DATABASE
    # =========================================================

    def create_Database(self):

        try:

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employeedb"
            )

            cursor = conn.cursor()

            # ================= SALARY TABLE =================

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS salary(
                    EMPLOYEE_ID INT PRIMARY KEY,
                    BASIC FLOAT DEFAULT 0,
                    HRA FLOAT DEFAULT 0,
                    OTHER_ALLOWENCE FLOAT DEFAULT 0,
                    OVERTIME FLOAT DEFAULT 0,
                    PF FLOAT DEFAULT 0,
                    TAX FLOAT DEFAULT 0,
                    DEDUCTIONS FLOAT DEFAULT 0,
                    GROSS FLOAT DEFAULT 0,
                    NET FLOAT DEFAULT 0,

                    FOREIGN KEY(EMPLOYEE_ID)
                    REFERENCES employee(EMPLOYEE_ID)
                    ON DELETE CASCADE
                )
            """)

            # =================================================
            # Agar salary table pehle se bana hua hai aur TAX
            # column nahi hai, to TAX column add karega
            # =================================================

            try:

                cursor.execute("""
                    ALTER TABLE salary
                    ADD COLUMN TAX FLOAT DEFAULT 0
                """)

            except mysql.connector.Error:
                # Column already exists
                pass

            conn.commit()

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:

            messagebox.showerror(
                "Database Error",
                f"Error:\n{err}"
            )


    # =========================================================
    # SALARY PAGE
    # =========================================================

    def salary_page(self, root1):

        root1.withdraw()

        sal_win = Toplevel(root1)

        sal_win.title("Update Salary Record")
        sal_win.geometry("1280x720")
        sal_win.configure(bg="#EEF4FB")
        sal_win.resizable(False, False)


        # =====================================================
        # HEADER
        # =====================================================

        self.header = Frame(
            sal_win,
            bg="#0B5ED7",
            height=90
        )

        self.header.pack(fill=X)


        Label(
            self.header,
            text="Update Salary Record",
            font=("Segoe UI", 24, "bold"),
            bg="#0B5ED7",
            fg="white"
        ).place(x=40, y=10)


        Label(
            self.header,
            text="Employee Salary Management System",
            font=("Segoe UI", 11),
            bg="#0B5ED7",
            fg="white"
        ).place(x=42, y=58)


        # =====================================================
        # MAIN
        # =====================================================

        self.main = Frame(
            sal_win,
            bg="#EEF4FB"
        )

        self.main.pack(
            fill=BOTH,
            expand=True,
            padx=20,
            pady=20
        )


        # =====================================================
        # LEFT PANEL - EMPLOYEE DETAILS
        # =====================================================

        self.left = LabelFrame(
            self.main,
            text="Employee Details",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            padx=15,
            pady=10
        )

        self.left.place(
            x=0,
            y=0,
            width=360,
            height=560
        )


        Label(
            self.left,
            text="Employee ID",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=4)


        self.id1 = Entry(
            self.left,
            font=("Segoe UI", 10),
            bg="white",
            fg="black",
            width=20
        )

        self.id1.place(
            x=110,
            y=4
        )


        self.btn = Button(
            self.left,
            text="Search",
            font=("Segoe UI", 10, "bold"),
            bg="#0B5ED7",
            fg="white",
            padx=5,
            cursor="hand2",
            command=lambda: self.view_emp_record(sal_win)
        )

        self.btn.place(
            x=270,
            y=2
        )


        # ================= EMPLOYEE LIST =================

        self.listbox = Listbox(
            self.left,
            fg="#1F4E79",
            bg="white",
            font=("Segoe UI", 10),
            width=40,
            height=29
        )

        self.listbox.place(
            x=5,
            y=40
        )


        # =====================================================
        # CENTER PANEL - SALARY DETAILS
        # =====================================================

        self.center = LabelFrame(
            self.main,
            text="Salary Details",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            padx=15,
            pady=10
        )

        self.center.place(
            x=380,
            y=0,
            width=420,
            height=560
        )


        # =====================================================
        # SALARY VARIABLES
        # =====================================================

        self.salary_val = {

            "Basic": StringVar(),
            "Hra": StringVar(),
            "Other": StringVar(),
            "Over": StringVar(),
            "Pf": StringVar(),
            "Tax": StringVar(),
            "Deductions": StringVar(),
            "Gross": StringVar(),
            "Net": StringVar()

        }


        # =====================================================
        # BASIC
        # =====================================================

        Label(
            self.center,
            text="Basic",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=0)


        self.basic = Entry(
            self.center,
            font=("Segoe UI", 10),
            fg="black",
            bg="white",
            width=30,
            textvariable=self.salary_val["Basic"]
        )

        self.basic.place(
            x=170,
            y=0
        )


        # =====================================================
        # HRA
        # =====================================================

        Label(
            self.center,
            text="HRA",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=50)


        self.hra = Entry(
            self.center,
            font=("Segoe UI", 10),
            fg="black",
            bg="white",
            width=30,
            textvariable=self.salary_val["Hra"]
        )

        self.hra.place(
            x=170,
            y=50
        )


        # =====================================================
        # OTHER ALLOWANCES
        # =====================================================

        Label(
            self.center,
            text="Other Allowances",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=100)


        self.other = Entry(
            self.center,
            font=("Segoe UI", 10),
            fg="black",
            bg="white",
            width=30,
            textvariable=self.salary_val["Other"]
        )

        self.other.place(
            x=170,
            y=100
        )


        # =====================================================
        # OVERTIME
        # =====================================================

        Label(
            self.center,
            text="Overtime",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=150)


        self.over = Entry(
            self.center,
            font=("Segoe UI", 10),
            fg="black",
            bg="white",
            width=30,
            textvariable=self.salary_val["Over"]
        )

        self.over.place(
            x=170,
            y=150
        )


        # =====================================================
        # PF
        # =====================================================

        Label(
            self.center,
            text="PF",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=200)


        self.pf = Entry(
            self.center,
            font=("Segoe UI", 10),
            fg="black",
            bg="white",
            width=30,
            textvariable=self.salary_val["Pf"]
        )

        self.pf.place(
            x=170,
            y=200
        )


        # =====================================================
        # TAX
        # =====================================================

        Label(
            self.center,
            text="Tax",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=250)


        self.tax = Entry(
            self.center,
            font=("Segoe UI", 10),
            fg="black",
            bg="white",
            width=30,
            textvariable=self.salary_val["Tax"]
        )

        self.tax.place(
            x=170,
            y=250
        )


        # =====================================================
        # DEDUCTIONS
        # =====================================================

        Label(
            self.center,
            text="Deductions",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=300)


        self.ded = Entry(
            self.center,
            font=("Segoe UI", 10),
            fg="black",
            bg="white",
            width=30,
            textvariable=self.salary_val["Deductions"]
        )

        self.ded.place(
            x=170,
            y=300
        )


        # =====================================================
        # GROSS
        # =====================================================

        Label(
            self.center,
            text="Gross",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=350)


        self.gross = Entry(
            self.center,
            font=("Segoe UI", 10),
            fg="black",
            bg="white",
            width=30,
            textvariable=self.salary_val["Gross"],
            state="readonly"
        )

        self.gross.place(
            x=170,
            y=350
        )


        # =====================================================
        # NET
        # =====================================================

        Label(
            self.center,
            text="Net",
            bg="white",
            font=("Segoe UI", 10)
        ).place(x=5, y=400)


        self.net = Entry(
            self.center,
            font=("Segoe UI", 10),
            fg="black",
            bg="white",
            width=30,
            textvariable=self.salary_val["Net"],
            state="readonly"
        )

        self.net.place(
            x=170,
            y=400
        )


        # =====================================================
        # AUTO CALCULATE
        # =====================================================

        def auto_calculate(event=None):

            try:

                basic1 = float(
                    self.salary_val["Basic"].get() or 0
                )

                hra1 = float(
                    self.salary_val["Hra"].get() or 0
                )

                other1 = float(
                    self.salary_val["Other"].get() or 0
                )

                over1 = float(
                    self.salary_val["Over"].get() or 0
                )

                pf1 = float(
                    self.salary_val["Pf"].get() or 0
                )

                tax1 = float(
                    self.salary_val["Tax"].get() or 0
                )

                ded1 = float(
                    self.salary_val["Deductions"].get() or 0
                )


                # ================= GROSS =================

                gross1 = (
                    basic1 +
                    hra1 +
                    other1 +
                    over1
                )


                # ================= NET =================

                net1 = (
                    gross1 -
                    pf1 -
                    tax1 -
                    ded1
                )


                self.salary_val["Gross"].set(
                    f"{gross1:.2f}"
                )

                self.salary_val["Net"].set(
                    f"{net1:.2f}"
                )


            except ValueError:

                self.salary_val["Gross"].set("")

                self.salary_val["Net"].set("")


        # =====================================================
        # BIND ALL SALARY ENTRIES
        # =====================================================

        for value in (
            self.basic,
            self.hra,
            self.other,
            self.over,
            self.pf,
            self.tax,
            self.ded
        ):

            value.bind(
                "<KeyRelease>",
                auto_calculate
            )


        # =====================================================
        # UPDATE BUTTON
        # =====================================================

        Button(
            self.center,
            text="Update Salary",
            bg="#08CD61",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=lambda: self.update_sal(sal_win),
            width=18
        ).place(
            x=5,
            y=450
        )


        # =====================================================
        # CLOSE BUTTON
        # =====================================================

        Button(
            self.center,
            text="Close",
            bg="red",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=lambda: self.close_btn(
                sal_win,
                root1
            ),
            width=18
        ).place(
            x=200,
            y=450
        )


        # =====================================================
        # RIGHT PANEL
        # =====================================================

        self.right = Frame(
            self.main,
            bg="white",
            bd=1,
            relief="solid"
        )

        self.right.place(
            x=820,
            y=0,
            width=420,
            height=560
        )


        self.img = Image.open(
            r"C:\Users\DELL\Desktop\python\Employye\HR-Tech-startups.png"
        )

        self.img = self.img.resize(
            (400, 520)
        )

        self.photo = ImageTk.PhotoImage(
            self.img
        )


        self.pic = Label(
            self.right,
            highlightbackground="grey",
            image=self.photo,
            bg="white"
        )

        self.pic.image = self.photo

        self.pic.pack(
            expand=True
        )


    # =========================================================
    # SEARCH EMPLOYEE
    # =========================================================

    def view_emp_record(self, sal_win):

        emp_id = self.id1.get().strip()


        # ================= VALIDATION =================

        if emp_id == "" or emp_id == "Enter Employee ID":

            messagebox.showerror(
                "Invalid Input",
                "Please enter Employee ID",
                parent=sal_win
            )

            return


        if not emp_id.isdigit():

            messagebox.showerror(
                "Invalid Input",
                "Employee ID should be numeric",
                parent=sal_win
            )

            return


        emp_id = int(emp_id)


        conn = None
        cursor = None


        try:

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employeedb"
            )

            cursor = conn.cursor()


            # =================================================
            # EMPLOYEE DATA
            # =================================================

            cursor.execute(
                """
                SELECT *
                FROM employee
                WHERE EMPLOYEE_ID=%s
                """,
                (emp_id,)
            )


            employee = cursor.fetchone()


            # =================================================
            # EMPLOYEE NOT FOUND
            # =================================================

            if employee is None:

                self.listbox.delete(
                    0,
                    END
                )

                self.clear_salary()

                messagebox.showerror(
                    "Invalid ID",
                    "Employee Not Found",
                    parent=sal_win
                )

                return


            # =================================================
            # CLEAR OLD EMPLOYEE DATA
            # =================================================

            self.listbox.delete(
                0,
                END
            )


            # =================================================
            # DISPLAY EMPLOYEE DATA
            # =================================================

            self.listbox.insert(
                END,
                f"EMPLOYEE ID: {employee[0]}"
            )

            self.listbox.insert(
                END,
                f"NAME: {employee[1]}"
            )

            self.listbox.insert(
                END,
                f"GENDER: {employee[2]}"
            )

            self.listbox.insert(
                END,
                f"DATE OF BIRTH: {employee[3]}"
            )

            self.listbox.insert(
                END,
                f"PHONE NUMBER: {employee[4]}"
            )

            self.listbox.insert(
                END,
                f"EMAIL ID: {employee[5]}"
            )

            self.listbox.insert(
                END,
                f"ADDRESS: {employee[6]}"
            )

            self.listbox.insert(
                END,
                f"DEPARTMENT: {employee[7]}"
            )

            self.listbox.insert(
                END,
                f"DATE OF JOINING: {employee[8]}"
            )

            self.listbox.insert(
                END,
                f"DESIGNATION: {employee[9]}"
            )

            self.listbox.insert(
                END,
                f"EMPLOYMENT STATUS: {employee[10]}"
            )

            self.listbox.insert(
                END,
                f"EMPLOYMENT TYPE: {employee[11]}"
            )


            # =================================================
            # SEARCH SALARY
            # =================================================

            cursor.execute(
                """
                SELECT
                    BASIC,
                    HRA,
                    OTHER_ALLOWENCE,
                    OVERTIME,
                    PF,
                    TAX,
                    DEDUCTIONS,
                    GROSS,
                    NET
                FROM salary
                WHERE EMPLOYEE_ID=%s
                """,
                (emp_id,)
            )


            salary = cursor.fetchone()


            # =================================================
            # SALARY FOUND
            # =================================================

            if salary is not None:

                self.salary_val["Basic"].set(
                    salary[0]
                )

                self.salary_val["Hra"].set(
                    salary[1]
                )

                self.salary_val["Other"].set(
                    salary[2]
                )

                self.salary_val["Over"].set(
                    salary[3]
                )

                self.salary_val["Pf"].set(
                    salary[4]
                )

                self.salary_val["Tax"].set(
                    salary[5]
                )

                self.salary_val["Deductions"].set(
                    salary[6]
                )

                self.salary_val["Gross"].set(
                    salary[7]
                )

                self.salary_val["Net"].set(
                    salary[8]
                )


            # =================================================
            # SALARY NOT FOUND
            # =================================================

            else:

                self.clear_salary()


            messagebox.showinfo(
                "Employee Found",
                "Employee details and salary loaded successfully.",
                parent=sal_win
            )


        except mysql.connector.Error as err:

            messagebox.showerror(
                "Database Error",
                f"Database Error:\n{err}",
                parent=sal_win
            )


        finally:

            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()


    # =========================================================
    # CLEAR SALARY
    # =========================================================

    def clear_salary(self):

        for key in self.salary_val:

            self.salary_val[key].set("")


    # =========================================================
    # UPDATE SALARY
    # =========================================================

    def update_sal(self, sal_win):

        emp_id = self.id1.get().strip()


        # ================= EMPLOYEE ID =================

        if emp_id == "" or not emp_id.isdigit():

            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid Employee ID.",
                parent=sal_win
            )

            return


        emp_id = int(emp_id)


        try:

            # =================================================
            # GET SALARY VALUES
            # =================================================

            basic = float(
                self.salary_val["Basic"].get() or 0
            )

            hra = float(
                self.salary_val["Hra"].get() or 0
            )

            other = float(
                self.salary_val["Other"].get() or 0
            )

            overtime = float(
                self.salary_val["Over"].get() or 0
            )

            pf = float(
                self.salary_val["Pf"].get() or 0
            )

            tax = float(
                self.salary_val["Tax"].get() or 0
            )

            deductions = float(
                self.salary_val["Deductions"].get() or 0
            )


            # =================================================
            # CALCULATE
            # =================================================

            gross = (
                basic +
                hra +
                other +
                overtime
            )


            net = (
                gross -
                pf -
                tax -
                deductions
            )


            # =================================================
            # DISPLAY CALCULATED VALUES
            # =================================================

            self.salary_val["Gross"].set(
                f"{gross:.2f}"
            )

            self.salary_val["Net"].set(
                f"{net:.2f}"
            )


            # =================================================
            # DATABASE
            # =================================================

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employeedb"
            )

            cursor = conn.cursor()


            # =================================================
            # CHECK EMPLOYEE
            # =================================================

            cursor.execute(
                """
                SELECT EMPLOYEE_ID
                FROM employee
                WHERE EMPLOYEE_ID=%s
                """,
                (emp_id,)
            )


            employee = cursor.fetchone()


            if employee is None:

                messagebox.showerror(
                    "Invalid Employee",
                    "Employee does not exist.",
                    parent=sal_win
                )

                cursor.close()
                conn.close()

                return


            # =================================================
            # INSERT OR UPDATE SALARY
            # =================================================

            cursor.execute(
                """
                INSERT INTO salary
                (
                    EMPLOYEE_ID,
                    BASIC,
                    HRA,
                    OTHER_ALLOWENCE,
                    OVERTIME,
                    PF,
                    TAX,
                    DEDUCTIONS,
                    GROSS,
                    NET
                )
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

                ON DUPLICATE KEY UPDATE

                    BASIC=%s,
                    HRA=%s,
                    OTHER_ALLOWENCE=%s,
                    OVERTIME=%s,
                    PF=%s,
                    TAX=%s,
                    DEDUCTIONS=%s,
                    GROSS=%s,
                    NET=%s
                """,

                (
                    emp_id,
                    basic,
                    hra,
                    other,
                    overtime,
                    pf,
                    tax,
                    deductions,
                    gross,
                    net,

                    basic,
                    hra,
                    other,
                    overtime,
                    pf,
                    tax,
                    deductions,
                    gross,
                    net
                )
            )


            conn.commit()


            cursor.close()
            conn.close()


            messagebox.showinfo(
                "Success",
                "Salary updated successfully.",
                parent=sal_win
            )


        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Salary fields should contain numbers only.",
                parent=sal_win
            )


        except mysql.connector.Error as err:

            messagebox.showerror(
                "Database Error",
                f"Database Error:\n{err}",
                parent=sal_win
            )


    # =========================================================
    # CLOSE
    # =========================================================

    def close_btn(self, sal_win, root1):

        sal_win.destroy()

        root1.deiconify()