from tkinter import *
import mysql.connector
from tkinter import messagebox


class Delete_employee:

    def __init__(self):
        self.create_Database()

    # =====================================================
    #                 DATABASE CONNECTION
    # =====================================================

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
                "Database Error",
                f"Error: {err}"
            )

    # =====================================================
    #                    DELETE PAGE
    # =====================================================

    def delete_page(self, root1):

        root1.withdraw()

        d_win = Toplevel(root1)

        d_win.geometry("1280x720")
        d_win.title("Delete Employee")
        d_win.resizable(False, False)
        d_win.config(bg="#F5F7FB")

        # =================================================
        #                     HEADER
        # =================================================

        Label(
            d_win,
            text="DELETE EMPLOYEE",
            bg="#054488",
            fg="white",
            font=("Arial", 22, "bold"),
            pady=10
        ).place(
            x=0,
            y=0,
            width=1280,
            height=55
        )

        Label(
            d_win,
            text="Employee Management System",
            bg="#054488",
            fg="white",
            font=("Arial", 13)
        ).place(
            x=0,
            y=55,
            width=1280,
            height=30
        )

        # =================================================
        #                  SEARCH FRAME
        # =================================================

        search_frame = Frame(
            d_win,
            bg="white",
            highlightbackground="#D5DDE5",
            highlightthickness=2
        )

        search_frame.place(
            x=250,
            y=120,
            width=800,
            height=100
        )

        Label(
            search_frame,
            text="Employee ID",
            bg="white",
            fg="black",
            font=("Arial", 13, "bold")
        ).place(
            x=50,
            y=35
        )

        # =================================================
        #                   EMPLOYEE ID
        # =================================================

        self.emp_id = Entry(
            search_frame,
            font=("Segoe UI", 13),
            bg="white",
            fg="black",
            highlightthickness=1,
            highlightbackground="#D5DDE5"
        )

        self.emp_id.place(
            x=200,
            y=32,
            width=250,
            height=38
        )

        # =================================================
        #                     SEARCH
        # =================================================

        Button(
            search_frame,
            text="Search",
            bg="#0D6EFD",
            fg="white",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            relief=FLAT,
            command=lambda: self.search_employee(d_win)
        ).place(
            x=500,
            y=30,
            width=120,
            height=38
        )

        # =================================================
        #                 DETAILS HEADING
        # =================================================

        Label(
            d_win,
            text="Employee Details",
            bg="#F5F7FB",
            fg="black",
            font=("Arial", 17, "bold")
        ).place(
            x=250,
            y=245
        )

        # =================================================
        #                  DETAILS FRAME
        # =================================================

        details_frame = Frame(
            d_win,
            bg="white",
            highlightbackground="#D5DDE5",
            highlightthickness=1
        )

        details_frame.place(
            x=250,
            y=280,
            width=800,
            height=210
        )

        # =================================================
        #                    LISTBOX
        # =================================================

        self.lst = Listbox(
            details_frame,
            bg="white",
            fg="purple",
            font=("Segoe UI", 13),
            bd=0,
            highlightthickness=0,
            activestyle="none"
        )

        self.lst.place(
            x=10,
            y=10,
            width=755,
            height=185
        )

        # =================================================
        #                  SCROLLBAR
        # =================================================

        self.scrollbar = Scrollbar(
            details_frame,
            orient=VERTICAL,
            command=self.lst.yview
        )

        self.scrollbar.place(
            x=765,
            y=10,
            width=20,
            height=185
        )

        self.lst.config(
            yscrollcommand=self.scrollbar.set
        )

        # =================================================
        #                    WARNING
        # =================================================

        Label(
            d_win,
            text="⚠ Are you sure you want to delete this employee?",
            bg="#FFF3F3",
            fg="red",
            font=("Arial", 13, "bold")
        ).place(
            x=330,
            y=515,
            width=650,
            height=50
        )

        # =================================================
        #                 DELETE BUTTON
        # =================================================

        self.delete_btn = Button(
            d_win,
            text="Delete Employee",
            bg="#DC3545",
            fg="white",
            font=("Arial", 13, "bold"),
            cursor="hand2",
            relief=FLAT,
            state=DISABLED,
            command=lambda: self.delete_employee(d_win)
        )

        self.delete_btn.place(
            x=430,
            y=585,
            width=200,
            height=45
        )

        # =================================================
        #                    CANCEL
        # =================================================

        Button(
            d_win,
            text="Cancel",
            bg="#6C757D",
            fg="white",
            font=("Arial", 13, "bold"),
            cursor="hand2",
            relief=FLAT,
            command=lambda: self.back(d_win, root1)
        ).place(
            x=680,
            y=585,
            width=150,
            height=45
        )

    # =====================================================
    #                 SEARCH EMPLOYEE
    # =====================================================

    def search_employee(self, d_win):

        emp_id = self.emp_id.get().strip()

        # =================================================
        #                 CLEAR OLD DATA
        # =================================================

        self.lst.delete(
            0,
            END
        )

        self.delete_btn.config(
            state=DISABLED
        )

        # =================================================
        #                 BLANK VALIDATION
        # =================================================

        if emp_id == "":

            messagebox.showerror(
                "Invalid Input",
                "Please enter Employee ID.",
                parent=d_win
            )

            self.emp_id.focus()

            return

        # =================================================
        #                 NUMERIC VALIDATION
        # =================================================

        if not emp_id.isdigit():

            messagebox.showerror(
                "Invalid Input",
                "Employee ID should be numeric.",
                parent=d_win
            )

            self.emp_id.focus()

            return

        emp_id = int(emp_id)

        conn = None
        cursor = None

        try:

            # =================================================
            #                 DATABASE CONNECTION
            # =================================================

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employeedb"
            )

            cursor = conn.cursor()

            # =================================================
            #                     SEARCH
            # =================================================

            cursor.execute(
                """
                SELECT *
                FROM employee
                WHERE Employee_ID=%s
                """,
                (emp_id,)
            )

            check = cursor.fetchone()

            # =================================================
            #                EMPLOYEE NOT FOUND
            # =================================================

            if check is None:

                messagebox.showerror(
                    "Employee Not Found",
                    "No employee found with this Employee ID.",
                    parent=d_win
                )

                return

            # =================================================
            #                 DISPLAY DETAILS
            # =================================================

            self.lst.insert(
                END,
                f"EMPLOYEE ID: {check[0]}"
            )

            self.lst.insert(
                END,
                f"NAME: {check[1]}"
            )

            self.lst.insert(
                END,
                f"GENDER: {check[2]}"
            )

            self.lst.insert(
                END,
                f"DATE OF BIRTH: {check[3]}"
            )

            self.lst.insert(
                END,
                f"PHONE NUMBER: {check[4]}"
            )

            self.lst.insert(
                END,
                f"EMAIL ID: {check[5]}"
            )

            self.lst.insert(
                END,
                f"ADDRESS: {check[6]}"
            )

            self.lst.insert(
                END,
                f"DEPARTMENT: {check[7]}"
            )

            self.lst.insert(
                END,
                f"DATE OF JOINING: {check[8]}"
            )

            self.lst.insert(
                END,
                f"DESIGNATION: {check[9]}"
            )

            self.lst.insert(
                END,
                f"EMPLOYMENT STATUS: {check[10]}"
            )

            self.lst.insert(
                END,
                f"EMPLOYMENT TYPE: {check[11]}"
            )

            # Save employee ID for delete operation
            self.selected_emp_id = emp_id

            # Enable Delete button
            self.delete_btn.config(
                state=NORMAL
            )

            messagebox.showinfo(
                "Employee Found",
                "Employee details loaded successfully.",
                parent=d_win
            )

        except mysql.connector.Error as err:

            messagebox.showerror(
                "Database Error",
                f"Database Error:\n{err}",
                parent=d_win
            )

        finally:

            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()

    # =====================================================
    #                  DELETE EMPLOYEE
    # =====================================================

    def delete_employee(self, d_win):

        # =================================================
        #               CHECK EMPLOYEE
        # =================================================

        if not hasattr(self, "selected_emp_id"):

            messagebox.showerror(
                "Error",
                "Please search an employee first.",
                parent=d_win
            )

            return

        # =================================================
        #                CONFIRMATION
        # =================================================

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this employee?\n\n"
            "This action cannot be undone.",
            parent=d_win
        )

        if not confirm:

            return

        conn = None
        cursor = None

        try:

            # =================================================
            #                 DATABASE
            # =================================================

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employeedb"
            )

            cursor = conn.cursor()

            # =================================================
            #                    DELETE
            # =================================================

            cursor.execute(
                """
                DELETE FROM employee
                WHERE Employee_ID=%s
                """,
                (self.selected_emp_id,)
            )

            conn.commit()

            # =================================================
            #                CHECK DELETE
            # =================================================

            if cursor.rowcount == 0:

                messagebox.showerror(
                    "Error",
                    "Employee could not be deleted.",
                    parent=d_win
                )

                return

            # =================================================
            #                SUCCESS MESSAGE
            # =================================================

            messagebox.showinfo(
                "Delete Successful",
                "Employee deleted successfully.",
                parent=d_win
            )

            # =================================================
            #                CLEAR DETAILS
            # =================================================

            self.lst.delete(
                0,
                END
            )

            self.emp_id.delete(
                0,
                END
            )

            self.delete_btn.config(
                state=DISABLED
            )

            # Remove selected ID
            del self.selected_emp_id

        except mysql.connector.Error as err:

            if conn is not None:
                conn.rollback()

            messagebox.showerror(
                "Database Error",
                f"Database Error:\n{err}",
                parent=d_win
            )

        finally:

            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()

    # =====================================================
    #                    BACK TO DASHBOARD
    # =====================================================

    def back(self, d_win, root1):

        d_win.destroy()

        root1.deiconify()