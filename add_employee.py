from tkinter import *;
from PIL import Image,ImageTk;
import mysql.connector;
from tkinter import ttk;
from tkcalendar import DateEntry;
from datetime import date;
from tkinter import messagebox;
class Employee_manager:
    def __init__(self):
        self.create_Database()

    def create_Database(self):
  
        try: 
            #============== Database Connection==========================
            conn=mysql.connector.connect(host="localhost",user="root",password="");
            cursor=conn.cursor();

            #===============Creating a Databsae==================  
            cursor.execute("CREATE DATABASE IF NOT EXISTS employeedb");
            conn.database="employeedb";
            cursor.execute("USE employeedb")
            #=============Creating a Table===================
            cursor.execute("""CREATE TABLE IF NOT EXISTS employee(
                EMPLOYEE_ID INT PRIMARY KEY,
                FULL_NAME VARCHAR(50) NOT NULL,
                GENDER VARCHAR(10) NOT NULL,
                DATE_OF_BIRTH DATE NOT NULL,
                CONTACT_NO VARCHAR(10) NOT NULL UNIQUE,
                EMAIL_ID VARCHAR(100) NOT NULL UNIQUE,
                ADDRESS TEXT NOT NULL,
                DEPARTMENT VARCHAR(50) NOT NULL,
                DATE_OF_JOINING DATE NOT NULL,
                DESIGNATION VARCHAR(50) NOT NULL,
                EMPLOYMENT_STATUS VARCHAR(50) NOT NULL,
                EMPLOYMENT_TYPE VARCHAR(50) NOT NULL)    
            """ )
            conn.commit();   
            conn.close()
        except mysql.connector.Error as err:
                messagebox.showerror("Database error",f"Error: {err}") 


    def add_employees(self,root1): 

        root1.withdraw()
        a_win=Toplevel(root1)
        a_win.geometry("1280x720");
        a_win.title("Add New Employee");
        a_win.configure(bg="#F8FBFF");
    #==================Add New Employee Section==================
        self.curr_date=date.today()

        Label(a_win,text="ADD NEW EMPLOYEE",
            font=("Arial",22,"bold"),
            pady=7,
            bg="#054488",
            fg="white").place(width=1280);
        
        Label(a_win,text="Employee Management System",
            font=("Arial",15),
                bg="#054488",
                fg="white").place(x=0,y=40,width=1280,height=40);
        
        #===============================Personal Infornmation Section==========================

        Label(a_win,bg="#FFFFFF",
            highlightbackground="#D5DDE5",
            highlightthickness=1,).place(x=20,y=100,width=1230,height=490);

        #==============Clear Function==================
        def Clear_func(event,obj,placeholder):
            if obj.get()==placeholder:
                obj.delete(0,END)
                obj.config(fg="black",bg="white")

        #=================Restore Function=============
        def Restore_func(event,obj,placeholder):
            if obj.get()=="":
              obj.insert(0,placeholder);
              obj.config(bg="white",fg="grey",font=("Calibri",13))


        

    #=================Personal Infornmation===========
        
        Label(a_win,text="PERSONAL INFORNMATION",
            bg="white",
            font=("Calibri",14,"bold"),
            fg="#054488").place(x=40,y=110)
        
        #===================UnderLine=====================
        Frame(a_win,bg="#4681C0",height=1).place(x=280,y=125,width=960)

        #==============Employee Id==================
        Label(a_win,text="Employee ID",
            bg="#FFFFFF",
            fg="black",
            width=10,
            font=("Calibri",13)).place(x=40,y=150)
        self.id1=Entry(a_win,bg="#FFFFFF",fg="grey",font=("Calibri",13),width=35)
        self.id1.place(x=210,y=150);
        self.id1.insert(0,"Enter Employee ID")
        self.id1.bind("<FocusIn>",lambda event:Clear_func(event,self.id1,"Enter Employee ID",))
        self.id1.bind("<FocusOut>",lambda event:Restore_func(event,self.id1,"Enter Employee ID"))
        

        #======================Gender  Variable=============

        self.Gender_var=StringVar(value="Male");

        #================Gender function==================


        #=======================================Gender Section============================================

        Label(a_win,text="Gender",bg="#FFFFFF",
            fg="black"
            ,font=("Calibri",13)).place(x=40,y=200);

        self.Male=Radiobutton(a_win,
                            text="Male",
                            font=("Calibri",13),
                            bg="#FFFFFF",
                            fg="black",
                            activebackground="#FFFFFF",
                            selectcolor="white",
                            value="Male",
                            variable=self.Gender_var)
        self.Male.place(x=200,y=200);
        
        self.Female=Radiobutton(a_win,text="Female",
                        font=("Calibri",13),
                        bg="#FFFFFF",
                        fg="black",
                        activebackground="#FFFFFF",
                        selectcolor="white",
                        value="Female",
                        variable=self.Gender_var)
        self.Female.place(x=290,y=200);

        self.Others=Radiobutton(a_win,text="Others",
                            font=("Calibri",13),
                            bg="#FFFFFF",
                            fg="black",
                            activebackground="#FFFFFF",
                            selectcolor="white",
                            value="Others",
                            variable=self.Gender_var)
        self.Others.place(x=390,y=200);

        #===================Phone Number=======================
        Label(a_win,text="Phone Number",
                bg="#FFFFFF",
                fg="black",
                width=12,
                font=("Calibri",13)).place(x=40,y=250)
        self.Phone=Entry(a_win,bg="#FFFFFF",fg="grey",font=("Calibri",13),width=35)
        self.Phone.place(x=210,y=253);
        self.Phone.insert(0,"Enter Phone Number");
        self.Phone.bind("<FocusIn>",lambda event:Clear_func(event,self.Phone,"Enter Phone Number"))
        self.Phone.bind("<FocusOut>",lambda event:Restore_func(event,self.Phone,"Enter Phone Number"))

        #===================addresss============================
        Label(a_win,text="Address",
                    bg="#FFFFFF",
                    fg="black",
                    width=10,
                    font=("Calibri",13),
                    ).place(x=25,y=320)
        self.Address=Text(a_win,font=("Calibri",13),
                    bg="white",
                    fg="black",
                    width=108,
                    height=3)
        self.Address.place(x=210,y=320)
        #=====================Full Name====================
        Label(a_win,text="Full Name",
                bg="#FFFFFF",
                fg="black",
                width=10,
                font=("Calibri",13)).place(x=650,y=150)
        self.name=Entry(a_win,bg="#FFFFFF",fg="grey",font=("Calibri",13),width=35)
        self.name.place(x=800,y=150);
        self.name.insert(0,"Enter Full Name")
        self.name.bind("<FocusIn>",lambda event:Clear_func(event,self.name,"Enter Full Name"))
        self.name.bind("<FocusOut>",lambda event:Restore_func(event,self.name,"Enter Full Name"))

        #=================== Date of Birth==================
        Label(a_win,text="Date of Birth",
                    bg="#FFFFFF",
                    fg="black",
                    width=13,
                    font=("Calibri",13)).place(x=640,y=200)
        self.dob=DateEntry(a_win,
                    font=("Calibri",13),fg="white",bg="black",
                    width=33,
                    date_pattern="yyyy-mm-dd",
                    mindate=date(self.curr_date.year-60,1,1),
                    maxdate=date(self.curr_date.year-15,self.curr_date.month,self.curr_date.day))
        self.dob.place(x=800,y=200)


        #==================Email address=====================
        Label(a_win,text="Email Address",
                        bg="#FFFFFF",
                        fg="black",
                        width=13,
                        font=("Calibri",13)).place(x=640,y=250)
        self.email=Entry(a_win,bg="#FFFFFF",fg="grey",font=("Calibri",13),width=35)
        self.email.place(x=800,y=250);
        self.email.insert(0,"Enter Email Address")
        self.email.bind("<FocusIn>",lambda event:Clear_func(event,self.email,"Enter Email Address"))
        self.email.bind("<FocusOut>",lambda event:Restore_func(event,self.email,"Enter Email Address"))



        #================Job Infornmaion====================
        Label(a_win,text="JOB INFORNMATION",
                bg="white",
                font=("Calibri",14,"bold"),
                fg="#054488").place(x=40,y=400)
            
            #===================UnderLine=====================
        Frame(a_win,bg="#4681C0",height=1).place(x=220,y=415,width=1020)

        #============Department=========================
        self.department=StringVar()
        Label(a_win,
            text="Department",
            bg="white",
            fg="black",
            width=10,
            font=("Calibri",13)).place(x=40,y=450);
        
        self.dept=ttk.Combobox(a_win,
                                values=["Select department",
                                        "Human Resources",
                                        "Information Technology",
                                        "Finance",
                                        "Marketing",
                                        "Sales",
                                        "Operations",
                                        "Administration",
                                        "Customer Support",
                                        "Research & Development",
                                        "Production"],
                                    state="readonly" ,
                                    width=32,
                                    textvariable=self.department,
                                    font=("Calibri",13))
        self.dept.current(0);
        self.dept.place(x=210,y=450)

        #====================Date of joining===================
        
        Label(a_win,
            text="Date of Joining",
            bg="white",
            fg="black",
            width=12,
            font=("Calibri",13)).place(x=40,y=500);

        self.doj=DateEntry(a_win,bg="white",width=32,fg="black",date_pattern="yyyy-mm-dd",font=("Calibri",13))
        
        self.doj.place(x=210,y=500,height=27)

        #======================Employee Status============================
        self.statusvalue=StringVar()
        Label(a_win,
              text="Employment Status",
              bg="white",
              fg="black",
              
              font=("Calibri",13)).place(x=40,y=550)
        self.emp=ttk.Combobox(a_win,
                              values=["Select Status",
                                     "Active",
                                     "Inactive",
                                     "On Leave",
                                     "Resigned",
                                     "Terminated"],
                                     state="readonly",
                                     width=32,
                                     textvariable=self.statusvalue,
                                     font=("Calibri",13))
        self.emp.current(0);
        self.emp.place(x=215,y=550)


        #===================Designation===================
        self.designationvalue=StringVar()
        
        Label(a_win,
                    text="Designation",
                    bg="white",
                    fg="black",
                    font=("Calibri",13)).place(x=640,y=450);
                
        self.designation=ttk.Combobox(a_win,
                                        values=["Select Designation",
                                                "Manager",
                                                "Team Leader",
                                                "Software Developer",
                                                "HR Executive",
                                                "Accountant",
                                                "Sales Executive",
                                                "Intern"
                                                ],
                                            state="readonly" ,
                                            width=32,
                                            textvariable=self.designationvalue,
                                            font=("Calibri",13))
        self.designation.current(0);
        self.designation.place(x=820,y=450)

        #==============Employment Type=======================
        self.emptype=StringVar()
        Label(a_win,
                    text="Employment Type",
                    bg="white",
                    fg="black",
                    width=15,
                    font=("Calibri",13)).place(x=640,y=500);
                
        self.e_type=ttk.Combobox(a_win,
                                        values=["Select Employment Type",
                                                "Full-Time",
                                                "Part-Time",
                                                "Contract",
                                                "Internship",
                                                ],
                                            state="readonly" ,
                                            width=32,
                                            textvariable=self.emptype,
                                            font=("Calibri",13))
        
        self.e_type.current(0);
        self.e_type.place(x=820,y=500)


        self.save=Button(a_win,
                        text="Save Employee",
                        font=("Arial",13,"bold"),
                        bg="#267A02",
                        fg="white",pady=4,padx=20,
                        command=lambda:self.Save_employee(a_win))
        self.save.place(x=300,y=594)

        self.clear=Button(a_win,
                            text="Clear From",
                            font=("Arial",13,"bold"),
                            bg="#054488",
                            fg="white",pady=4,padx=30,
                            command=lambda:self.clear_func(a_win))
        self.clear.place(x=520,y=594)

        #================Cancel=================

        self.cancel=Button(a_win,
                                text="Cancel",
                                font=("Arial",13,"bold"),
                                bg="red",
                                fg="white",pady=4,padx=40,
                                command=lambda:self.Cancel(a_win,root1))
        self.cancel.place(x=720,y=594)

    def Save_employee(self,a_win):
                #====================BLANK FIELDS======================
                employeeId=self.id1.get()
                fname=self.name.get()
                add=self.Address.get(1.0,END)
                mail=self.email.get()
                gender=self.Gender_var.get()
                dept_value=self.department.get()
                Status=self.statusvalue.get()
                desig_value=self.designationvalue.get()
                employee_type=self.emptype.get()
                if employeeId=="" or employeeId=="Enter Employee ID" or employeeId.isspace() or fname=="" or fname=="Enter Full Name" or fname.isspace() or add.strip()==""or add.isspace() or mail=="" or mail.isspace() or mail=="Enter Email Address":
                    messagebox.showerror("Invalid Input","All Fields are Required to fill.")
                    return
            
                #====================NAME VALIDATION====================
                fname=fname.replace(" ","")
                if not fname.isalpha():
                    messagebox.showerror("Invalid Input","Name should contain only alphabets")
                    return
                else:
                     fname=self.name.get()
                
                #=================EMPLOYEE ID VALIDATION=======================
                if not employeeId.isdigit():
                    messagebox.showerror("Invalid Input","Employee ID should be numeric")
                    return
                else:
                     employeeId=int(employeeId)
                
                #=================EMAIL VALIDATION===================
                if not mail[0].isalpha() or not mail.endswith("@gmail.com") or " " in mail:
                    messagebox.showerror("Invalid Email","Email is incorrect,Please try again!")
                    return
    
            #=================PHONE NUMBER VALIDATION===================
                mob=self.Phone.get()
                if mob.isdigit()==False:
                  messagebox.showerror("Invalid Input","Mobile Number must contain only digits.")
                  return
                if len(mob)!=10:
                  messagebox.showerror("Invalid Input","Mobile Number must be exactly 10 digits.")
                  return
                if mob[0] not in "6789":
                  messagebox.showerror("Invalid Input","Mobile Number must start with 6,7,8 or 9.")
                  return
    
                #====================DATE OF JOINING VALIDATION=======================
                doj_value=self.doj.get_date() 
                dob_value=self.dob.get_date()  
                if doj_value<=dob_value:
                  messagebox.showerror("invalid Input","Date of Birth cannot be greater than or equal to Date of Joinning")
                  return
                if dept_value == "Select department":
                    messagebox.showerror(
                        "Invalid Input",
                        "Please select Department",
                        parent=a_win
                    )
                    return

                if Status == "Select Status":
                    messagebox.showerror(
                        "Invalid Input",
                        "Please select Employment Status",
                        parent=a_win
                    )
                    return

                if desig_value == "Select Designation":
                        messagebox.showerror(
                            "Invalid Input",
                            "Please select Designation",
                            parent=a_win
                        )
                        return

                if employee_type == "Select Employment Type":
                        messagebox.showerror(
                            "Invalid Input",
                            "Please select Employment Type",
                            parent=a_win
                        )
                        return

                #===========INSERT DATA INTO TABLE==================
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="")
                    cursor=conn.cursor()
                    cursor.execute("USE employeedb")
                    cursor.execute("""INSERT INTO employee(EMPLOYEE_ID,FULL_NAME,GENDER,
                    DATE_OF_BIRTH,CONTACT_NO,EMAIL_ID,ADDRESS,DEPARTMENT,DATE_OF_JOINING,DESIGNATION,
                    EMPLOYMENT_STATUS,EMPLOYMENT_TYPE)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (employeeId,fname,gender,dob_value,mob,mail,add,
                     dept_value,doj_value,desig_value,Status,employee_type))
                    conn.commit()
                    conn.close()

                     #====================SAVE EMPLOYEEE=====================
                    messagebox.showinfo("Success","Employee saved successfully.")   
                    
                     #===========AFTER STORING VALUE INTO DATABASE CLEAR ALL FILEDS

                    self.id1.delete(0,END)
                    self.id1.insert(0,"Enter Employee ID")
                    self.id1.config(fg="grey")
                    self.Phone.delete(0,END)
                    self.Phone.insert(0,"Enter Phone Number")
                    self.Phone.config(fg="grey")
                    self.Address.delete("1.0",END)
                    self.name.delete(0,END)
                    self.name.insert(0,"Enter Full Name")
                    self.name.config(fg="grey")
                    self.email.delete(0,END)
                    self.email.insert(0,"Enter Email Address")
                    self.email.config(fg="grey")
                    self.dept.current(0) 
                    self.emp.current(0)
                    self.designation.current(0)
                    self.e_type.current(0)
                    self.dob.set_date(date(self.curr_date.year-15,self.curr_date.month,self.curr_date.day))
                    self.doj.set_date(date(self.curr_date.year,self.curr_date.month,self.curr_date.day))
                    self.Gender_var.set("Male")
                    
                        
                except Exception as e:
                            messagebox.showerror("Error",f"Database Error:\n{str(e)}",parent=a_win)
        

    def clear_func(self,a_win):
                        self.id1.delete(0,END)
                        self.id1.insert(0,"Enter Employee ID")
                        self.id1.config(fg="grey")
                        self.Phone.delete(0,END)
                        self.Phone.insert(0,"Enter Phone Number")
                        self.Phone.config(fg="grey")
                        self.Address.delete("1.0",END)
                        self.name.delete(0,END)
                        self.name.insert(0,"Enter Full Name")
                        self.name.config(fg="grey")
                        self.email.delete(0,END)
                        self.email.insert(0,"Enter Email Address")
                        self.email.config(fg="grey")
                        self.dept.current(0)  # we can also used set()it take a value not index
                        #combobox=set,current()
                        #radiobutton=set()
                        #checkbutton=set()
                        #calander=set_date()
                        #entry=insert()
                        #text=insert()
                
                        self.emp.current(0)
                        self.designation.current(0)
                        self.e_type.current(0)
                        self.dob.set_date(date(self.curr_date.year-15,self.curr_date.month,self.curr_date.day))
                        self.doj.set_date(date(self.curr_date.year,self.curr_date.month,self.curr_date.day))
                        self.Gender_var.set("Male")
                        self.id1.focus_set()
    
    def Cancel(self,a_win,root1):
                a_win.destroy();
                root1.deiconify();

    
                
        
        
        







        

