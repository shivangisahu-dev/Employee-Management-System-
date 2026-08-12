from tkinter import *
from tkinter import messagebox; #messagebox package
import mysql.connector; #libray
from PIL import Image,ImageTk
from Employee import Employee_dashboard;
def create_Database():
    try: 
        #============== Database Connection==========================
        conn=mysql.connector.connect(host="localhost",user="root",password="");
        cursor=conn.cursor();

        #===============Creating a Databsae==================  
        cursor.execute("CREATE DATABASE IF NOT EXISTS employeedb");
        conn.database="employeedb";
        cursor.execute("USE employeedb")
        #=============Creating a Table===================
        cursor.execute("""CREATE TABLE IF NOT EXISTS user(
            Username VARCHAR(100) PRIMARY KEY,
            Password VARCHAR(100) NOT NULL)
        """ );
        conn.commit();
        #================ Databse connected succesfully or not==================
        if conn.is_connected():
           print("connnected Successfully");

        #===============Insert Username and Password==============
        cursor.execute("USE employeedb")
        cursor.execute("SELECT * FROM user WHERE Username='admin'");
        check=cursor.fetchone();#agar username=admin exist krta hoga to 1row return krega otherwise None return krega
        if check is None:
          cursor.execute("""INSERT INTO user (Username,Password)
            VALUES ("admin","admin@123")
            """);
          conn.commit();
        conn.close();
    except mysql.connector.Error as err:
        messagebox.showerror("Database error",f"Error: {err}")

def Login_page():
    root = Tk()
    root.title("Employee Management System")
    root.geometry("950x550")
    root.config(bg="#EEF4FA")
    root.resizable(False, False)

    #==================Entry Function==============
    def clear_entry(event,entry,placeholder,is_password=False):
            if entry.get()==placeholder:
                entry.delete(0,END);
                entry.config(bg="white",fg="black",font=("Segoe UI",11))
                if is_password==True:
                    entry.config(show="*");
    
        #=================code for Restore Entry=====================
    def restore_entry(event,entry,placeholder,is_password=False):
            if entry.get()=="":
               entry.insert(0,placeholder);
               entry.config(bg="white",fg="grey",show="",font=("Segoe UI",11));

    # ================= LEFT PANEL =================

    left_frame = Frame(
        root,
        bg="#2F5D8C",
        width=350,
        height=550
    )
    left_frame.place(x=0, y=0)

    Label(
        left_frame,
        text="EMPLOYEE\nMANAGEMENT\nSYSTEM",
        font=("Segoe UI", 24, "bold"),
        bg="#2F5D8C",
        fg="white",
        justify="center"
    ).place(x=45, y=130)

    Label(
        left_frame,
        text="Manage employees efficiently\nwith a modern system",
        font=("Segoe UI", 11),
        bg="#2F5D8C",
        fg="#DCE6F2",
        justify="center"
    ).place(x=60, y=260)

    # ================= LOGIN CARD =================

    login_frame = Frame(
        root,
        bg="white",
        width=420,
        height=380,
        highlightbackground="#D6E0EA",
        highlightthickness=1
    )
    login_frame.place(x=460, y=85)

    Label(
        login_frame,
        text="Welcome Back",
        font=("Segoe UI", 22, "bold"),
        bg="white",
        fg="#1F4E79"
    ).place(x=105, y=35)

    Label(
        login_frame,
        text="Login to continue",
        font=("Segoe UI", 10),
        bg="white",
        fg="gray"
    ).place(x=155, y=75)

    # Username

    Label(
        login_frame,
        text="Username",
        font=("Segoe UI", 10, "bold"),
        bg="white"
    ).place(x=50, y=125)

    username=Entry(
        login_frame,
        font=("Segoe UI", 11,),
        width=32,
        relief="solid",
        bd=1,
        fg="grey",
        bg="white"
        
    )
    username.place(x=50, y=150, height=35)
    username.insert(0,"Username")
    username.bind("<FocusIn>",lambda event:clear_entry(event,username,"Username"))
    username.bind("<FocusOut>",lambda event:restore_entry(event,username,"Username"))

    # Password

    Label(

        login_frame,
        text="Password",
        font=("Segoe UI", 10, "bold"),
        bg="white"
    ).place(x=50, y=210)

    password=Entry(
        login_frame,
        font=("Segoe UI", 11),
        width=32,
        relief="solid",
        bd=1,
        fg="grey",
        bg="white"
    )
    password.place(x=50, y=235, height=35)
    password.insert(0,"Password");
    password.bind("<FocusIn>",lambda event:clear_entry(event,password,"Password",True))
    password.bind("<FocusOut>",lambda event:restore_entry(event,password,"Password",True))
    #====================LOGIN FUNCTION================
    def Login():
          Username=username.get();
          passs=password.get();
          if(Username==""or Username=="username" or passs=="" or passs=="Password"):
              messagebox.showerror("Error","Please fill all field",parent=root);
              return;
    
          try:  
             conn=mysql.connector.connect(host="localhost",user="root",password="");
             cursor=conn.cursor();
             cursor.execute("USE employeedb");
    
             cursor.execute("SELECT * FROM user WHERE Username=%s AND Password=%s",(Username,passs));
             result=cursor.fetchone();
             conn.close();
            
             if result==None:
                messagebox.showerror("Failed","Invalid Username or password",parent=root)
             else:

                 Employee_dashboard(root);
          except Exception as e:
              messagebox.showerror("Error",f"Database Error:\n{str(e)}",parent=root)
    

    # Login Button

    Button(
        login_frame,
        text="LOGIN",
        font=("Segoe UI", 11, "bold"),
        bg="#2F5D8C",
        fg="white",
        activebackground="#23476A",
        activeforeground="white",
        bd=0,
        width=30,
        cursor="hand2",
        command=Login
    ).place(x=45, y=310)
    

    root.mainloop()
create_Database()
Login_page()