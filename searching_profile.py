from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class Searching_employee:

    def __init__(self):
        self.create_Database()

    # ================= DATABASE CONNECTION =================

    def create_Database(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employeedb"
            )

            cursor = conn.cursor()

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror(
                "Database error",
                f"Error: {err}"
            )

    # ================= SEARCHING PAGE =================

    def searching_page(self, root1):

        root1.withdraw()

        s_win = Toplevel(root1)

        s_win.title("Search Employee")
        s_win.geometry("1280x720")
        s_win.configure(bg="#F8FBFF")

        # ================= MAIN HEADER =================

        self.Main = Frame(
            s_win,
            bg="#0E6ACD"
        )

        self.Main.place(
            x=0,
            y=0,
            width=1280,
            height=80
        )

        Label(
            self.Main,
            text="Employee Management System",
            font=("Segoe UI", 22, "bold"),
            fg="white",
            bg="#0E6ACD"
        ).place(
            x=10,
            y=15
        )

        Label(
            self.Main,
            text="Search Employee",
            font=("Segoe UI", 15, "bold"),
            fg="white",
            bg="#0E6ACD"
        ).place(
            x=1050,
            y=15
        )

        # Header separator
        Frame(
            self.Main,
            bg="white",
            width=2,
            height=70
        ).place(
            x=1020,
            y=5
        )

        # ================= SEARCH OUTER FRAME =================

        self.outer = Frame(
            s_win,
            bg="white",
            highlightbackground="#D5DDE5",
            highlightthickness=1
        )

        self.outer.place(
            x=140,
            y=110,
            width=1000,
            height=200
        )

        Label(
            self.outer,
            text="Search Employee",
            bg="white",
            fg="black",
            font=("Arial", 15)
        ).place(
            x=20,
            y=10
        )

        Frame(
            self.outer,
            bg="#0E6ACD",
            height=2,
            width=175
        ).place(
            x=22,
            y=40
        )

        # ================= EMPLOYEE ID =================

        Label(
            self.outer,
            text="Employee ID",
            bg="white",
            fg="black",
            font=("Segoe UI", 13)
        ).place(
            x=20,
            y=60
        )

        # ================= PLACEHOLDER FUNCTIONS =================

        def clr_func(event, ob, placeholder):

            if ob.get() == placeholder:

                ob.delete(0, END)

                ob.config(
                    fg="black",
                    font=("Segoe UI", 13),
                    bg="white"
                )

        def rst_func(event, ob, placeholder):

            if ob.get().strip() == "":

                ob.insert(
                    0,
                    placeholder
                )

                ob.config(
                    fg="grey",
                    bg="white",
                    font=("Segoe UI", 13)
                )

        # ================= ENTRY =================

        self.e1 = Entry(
            self.outer,
            fg="grey",
            bg="white",
            font=("Segoe UI", 13),
            highlightthickness=1,
            highlightbackground="#EEEFF0"
        )

        self.e1.insert(
            0,
            "Enter Employee ID"
        )

        self.e1.place(
            x=200,
            y=60,
            width=700,
            height=40
        )

        self.e1.bind(
            "<FocusIn>",
            lambda event: clr_func(
                event,
                self.e1,
                "Enter Employee ID"
            )
        )

        self.e1.bind(
            "<FocusOut>",
            lambda event: rst_func(
                event,
                self.e1,
                "Enter Employee ID"
            )
        )

        # ================= SEARCH BUTTON =================

        self.button1 = Button(
            self.outer,
            text="Search",
            bg="#1586FE",
            fg="white",
            font=("Segoe UI", 15),
            pady=4,
            padx=30,
            command=lambda: self.search_emp(s_win)
        )

        self.button1.place(
            x=250,
            y=120
        )

        # ================= CLOSE BUTTON =================

        self.button2 = Button(
            self.outer,
            text="Close",
            bg="#D83939",
            fg="white",
            font=("Segoe UI", 15),
            pady=4,
            padx=30,
            command=lambda: self.close_details(s_win)
        )

        self.button2.place(
            x=430,
            y=120
        )

        # ================= BACK BUTTON =================

        self.button3 = Button(
            self.outer,
            text="Back to Dashboard",
            bg="grey",
            fg="white",
            font=("Segoe UI", 15),
            pady=4,
            padx=30,
            command=lambda: self.backto(
                s_win,
                root1
            )
        )

        self.button3.place(
            x=600,
            y=120
        )

        # =====================================================
        #                 EMPLOYEE DETAILS
        # =====================================================

        Label(
            s_win,
            text="Employee Details",
            bg="#F8FBFF",
            fg="black",
            font=("Arial",17,"bold")
        ).place(
            x=140,
            y=320
        )

        # ================= DETAILS FRAME =================

        self.details_frame = Frame(
            s_win,
            bg="white",
            highlightbackground="#D5DDE5",
            highlightthickness=1
        )

        self.details_frame.place(
            x=140,
            y=355,
            width=1000,
            height=255
        )

        # ================= LISTBOX =================

        self.listbox = Listbox(
            self.details_frame,
            bg="white",
            fg="green",
            font=("Calibri",13),
            bd=0,
            highlightthickness=0,
            activestyle="none"
        )

        self.listbox.place(
            x=10,
            y=10,
            width=950,
            height=233
        )

        # ================= VERTICAL SCROLLBAR =================

        self.scrollbar = Scrollbar(
            self.details_frame,
            orient=VERTICAL,
            command=self.listbox.yview
        )

        self.scrollbar.place(
            x=960,
            y=10,
            width=20,
            height=233
        )

        # ================= CONNECT LISTBOX + SCROLLBAR =================

        self.listbox.config(
            yscrollcommand=self.scrollbar.set
        )


    # =========================================================
    #                    SEARCH EMPLOYEE
    # =========================================================

    def search_emp(self, s_win):

        emp_id = self.e1.get().strip()

        # ================= VALIDATION =================

        if emp_id == "" or emp_id == "Enter Employee ID":

            messagebox.showerror(
                "Invalid Input",
                "Please enter Employee ID",
                parent=s_win
            )

            return

        if not emp_id.isdigit():

            messagebox.showerror(
                "Invalid Input",
                "Employee ID should be numeric",
                parent=s_win
            )

            return

        emp_id = int(emp_id)

        conn = None
        cursor = None

        try:

            # ================= DATABASE =================

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employeedb"
            )

            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM employee WHERE Employee_ID=%s",
                (emp_id,)
            )

            check = cursor.fetchone()

            # ================= EMPLOYEE NOT FOUND =================

            if check is None:

                self.listbox.delete(
                    0,
                    END
                )

                messagebox.showerror(
                    "Invalid ID",
                    "Employee Not Found",
                    parent=s_win
                )

                return

            # ================= CLEAR OLD DATA =================

            self.listbox.delete(
                0,
                END
            )

            # ================= DISPLAY DATA =================

            self.listbox.insert(
                END,
                f"NAME: {check[1]}"
            )

            self.listbox.insert(
                END,
                f"GENDER: {check[2]}"
            )

            self.listbox.insert(
                END,
                f"DATE OF BIRTH: {check[3]}"
            )

            self.listbox.insert(
                END,
                f"PHONE NUMBER: {check[4]}"
            )

            self.listbox.insert(
                END,
                f"EMAIL ID: {check[5]}"
            )

            self.listbox.insert(
                END,
                f"ADDRESS: {check[6]}"
            )

            self.listbox.insert(
                END,
                f"DEPARTMENT: {check[7]}"
            )

            self.listbox.insert(
                END,
                f"DATE OF JOINING: {check[8]}"
            )

            self.listbox.insert(
                END,
                f"DESIGNATION: {check[9]}"
            )

            self.listbox.insert(
                END,
                f"EMPLOYMENT STATUS: {check[10]}"
            )

            self.listbox.insert(
                END,
                f"EMPLOYMENT TYPE: {check[11]}"
            )

            # ================= SUCCESS MESSAGE =================

            messagebox.showinfo(
                "Employee Found",
                "Employee details loaded successfully.",
                parent=s_win
            )

        except mysql.connector.Error as err:

            messagebox.showerror(
                "Database Error",
                f"Database Error:\n{err}",
                parent=s_win
            )

        finally:

            # ================= CLOSE DATABASE =================

            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()

    # =========================================================
    #                    BACK TO DASHBOARD
    # =========================================================

    def backto(self, s_win, root1):

        s_win.destroy()

        root1.deiconify()

    # =========================================================
    #                    CLOSE WINDOW
    # =========================================================

    def close_details(self, s_win):

        s_win.destroy()