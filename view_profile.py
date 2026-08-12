from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def view_all_employee(root1):

    root1.withdraw()

    view_win = Toplevel(root1)
    view_win.title("Employee Management System - View All Employees")
    view_win.geometry("1280x720")
    view_win.resizable(False, False)
    view_win.config(bg="white")

    # =====================================================
    #                     HEADING
    # =====================================================

    Label(
        view_win,
        text="VIEW ALL EMPLOYEES",
        bg="#123E73",
        fg="white",
        font=("Arial", 24, "bold"),
        pady=15
    ).pack(fill=X)

    # =====================================================
    #                 TREEVIEW STYLE
    # =====================================================

    style = ttk.Style()

    style.configure(
        "Treeview",
        font=("Segoe UI", 13),
        rowheight=32,
        background="white",
        foreground="black",
        fieldbackground="white"
    )

    style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 13, "bold"),
        background="#E8F0F8",
        foreground="#123E73",
        relief="solid"
    )

    # =====================================================
    #                   TABLE FRAME
    # =====================================================

    table_frame = Frame(
        view_win,
        bg="white",
        highlightbackground="#D5DDE5",
        highlightthickness=1
    )

    table_frame.place(
        x=20,
        y=90,
        width=1240,
        height=555
    )

    # =====================================================
    #                    COLUMNS
    # =====================================================

    columns = (
        "EMPLOYEE_ID",
        "FULL_NAME",
        "GENDER",
        "DATE_OF_BIRTH",
        "CONTACT_NO",
        "EMAIL_ID",
        "ADDRESS",
        "DEPARTMENT",
        "DATE_OF_JOINING",
        "DESIGNATION",
        "EMPLOYMENT_STATUS",
        "EMPLOYMENT_TYPE"
    )

    # =====================================================
    #                    TREEVIEW
    # =====================================================

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    # =====================================================
    #                    HEADINGS
    # =====================================================

    for column in columns:

        tree.heading(
            column,
            text=column,
            anchor=CENTER
        )

    # =====================================================
    #                 COLUMN WIDTH
    # =====================================================

    tree.column(
        "EMPLOYEE_ID",
        width=110,
        minwidth=100,
        anchor=CENTER
    )

    tree.column(
        "FULL_NAME",
        width=170,
        minwidth=150,
        anchor=W
    )

    tree.column(
        "GENDER",
        width=110,
        minwidth=100,
        anchor=CENTER
    )

    tree.column(
        "DATE_OF_BIRTH",
        width=140,
        minwidth=130,
        anchor=CENTER
    )

    tree.column(
        "CONTACT_NO",
        width=150,
        minwidth=130,
        anchor=CENTER
    )

    tree.column(
        "EMAIL_ID",
        width=240,
        minwidth=200,
        anchor=W
    )

    tree.column(
        "ADDRESS",
        width=280,
        minwidth=220,
        anchor=W
    )

    tree.column(
        "DEPARTMENT",
        width=190,
        minwidth=160,
        anchor=W
    )

    tree.column(
        "DATE_OF_JOINING",
        width=150,
        minwidth=140,
        anchor=CENTER
    )

    tree.column(
        "DESIGNATION",
        width=180,
        minwidth=160,
        anchor=W
    )

    tree.column(
        "EMPLOYMENT_STATUS",
        width=180,
        minwidth=160,
        anchor=CENTER
    )

    tree.column(
        "EMPLOYMENT_TYPE",
        width=160,
        minwidth=140,
        anchor=CENTER
    )

    # =====================================================
    #                 VERTICAL SCROLLBAR
    # =====================================================

    y_scroll = ttk.Scrollbar(
        table_frame,
        orient=VERTICAL,
        command=tree.yview
    )

    # =====================================================
    #                HORIZONTAL SCROLLBAR
    # =====================================================

    x_scroll = ttk.Scrollbar(
        table_frame,
        orient=HORIZONTAL,
        command=tree.xview
    )

    # =====================================================
    #                 CONNECT SCROLLBARS
    # =====================================================

    tree.configure(
        yscrollcommand=y_scroll.set,
        xscrollcommand=x_scroll.set
    )

    # =====================================================
    #                      GRID
    # =====================================================

    tree.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    y_scroll.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    x_scroll.grid(
        row=1,
        column=0,
        sticky="ew"
    )

    table_frame.grid_rowconfigure(
        0,
        weight=1
    )

    table_frame.grid_columnconfigure(
        0,
        weight=1
    )

    # =====================================================
    #                     DATABASE
    # =====================================================

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

        cursor.execute("""
            SELECT
                EMPLOYEE_ID,
                FULL_NAME,
                GENDER,
                DATE_OF_BIRTH,
                CONTACT_NO,
                EMAIL_ID,
                ADDRESS,
                DEPARTMENT,
                DATE_OF_JOINING,
                DESIGNATION,
                EMPLOYMENT_STATUS,
                EMPLOYMENT_TYPE
            FROM employee
        """)

        rows = cursor.fetchall()

        # =================================================
        #                  INSERT DATA
        # =================================================

        for row in rows:

            tree.insert(
                "",
                END,
                values=row
            )

    except mysql.connector.Error as err:

        messagebox.showerror(
            "Database Error",
            f"Error: {err}",
            parent=view_win
        )

    finally:

        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()

    # =====================================================
    #                    CLOSE BUTTON
    # =====================================================

    Button(
        view_win,
        text="Close",
        font=("Calibri", 15, "bold"),
        bg="#D83939",
        fg="white",
        relief=FLAT,
        padx=35,
        pady=5,
        command=lambda: close_window(
            view_win,
            root1
        )
    ).place(
        x=570,
        y=650,
        width=140,
        height=45
    )


# =========================================================
#                  CLOSE WINDOW FUNCTION
# =========================================================

def close_window(view_win, root1):

    view_win.destroy()
    root1.deiconify()