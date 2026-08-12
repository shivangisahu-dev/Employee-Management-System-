from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
class update_employee:
    def __init__(self):
            self.create_Database()
    
    def create_Database(self):
            try: 
                #============== Database Connection==========================
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="employeedb");
                cursor=conn.cursor();
                cursor.close()
                conn.close()

            except mysql.connector.Error as err:
                    messagebox.showerror("Database error",f"Error: {err}") 
                   
                
    
    def update_employe(self,root1):
        root1.withdraw()
        u_win=Toplevel(root1)
        u_win.geometry("1280x720")
        u_win.title("Employee Management System - Update Employee")
        u_win.resizable(False,False)
        u_win.config(bg="white")

        self.today=date.today()

        #===================== HEADER SEACTION======================
        self.F1=Frame(u_win,
                bg="#123E73",
                height=100)
        self.F1.pack(fill=X)
        self.F1.pack_propagate(False)

        Label(self.F1,
            text="UPDATE EMPLOYEE",
            bg="#123E73",
            fg="white",
            width=30,
            font=("Arial",24,"bold")).pack(pady=8)
        Label(self.F1,
                text="Search employee by ID to update details",
                bg="#123E73",
                fg="white",
                font=("Arial",15,"bold")).pack()
        #============================SEARCH HEADER=====================
        self.s_header=Frame(u_win,
                    bg="white",
                    height=85,
                    highlightbackground="#D3D3D3",
                    highlightthickness=1,
                    width=1230
                    )
        self.s_header.pack(pady=10)

        Label(self.s_header,
            text="Employee ID",
            bg="white",
            fg="#123E73",
            font=("Calibri",18,"bold")).place(x=20,y=15)

        #==============Clear Function==================
        def Clear_code(event,obj,placeholder):
                    if obj.get()==placeholder:
                        obj.delete(0,END)
                        obj.config(fg="black",bg="white")
        
                #=================Restore Function=============
        def Restore(event,obj,placeholder):
                    if obj.get()=="":
                      obj.insert(0,placeholder)
                      obj.config(bg="white",fg="grey",font=("Calibri",13))

        self.emp_id=Entry(self.s_header,
                    bg="white",
                    fg="grey",
                    font=("Calibri",13),width=33,
                    )
        self.emp_id.place(x=240,y=18,height=32)
        self.emp_id.insert(0,"Enter Employee ID")
        self.emp_id.bind("<FocusIn>",lambda event:Clear_code(event,self.emp_id,"Enter Employee ID"))
        self.emp_id.bind("<FocusOut>",lambda event:Restore(event,self.emp_id,"Enter Employee ID"))

        self.btn=Button(self.s_header,
                text="Search",
                fg="white",
                bg="#123E73",
                highlightbackground="#123E73",
                highlightthickness=1,
                font=("Arial",15,"bold"),
                padx=20,
                command=lambda: self.search_employee(u_win)
        )
        self.btn.place(x=670,y=18,height=35)

        #============================SEARCH FOOTER=====================
        self.s_footer=Frame(u_win,
                        bg="white",
                        height=460,
                        highlightbackground="#D3D3D3",
                        highlightthickness=1,
                        width=1230
                        )
        self.s_footer.pack(pady=10)
        #===================NAME========================
        Label(self.s_footer,text="Name",
                        bg="#FFFFFF",
                        fg="#123E73",
                        font=("Calibri",18,"bold")).place(x=20,y=15)
        self.name=Entry(self.s_footer,bg="#FFFFFF",fg="grey",font=("Calibri",13),width=25)
        self.name.place(x=150,y=13,height=30);
        self.name.insert(0,"Enter Full Name")
        self.name.bind("<FocusIn>",lambda event:Clear_code(event,self.name,"Enter Full Name"))
        self.name.bind("<FocusOut>",lambda event:Restore(event,self.name,"Enter Full Name"))

        #=================CONTACT NUMBER================
        Label(self.s_footer,text="Phone",
                            bg="#FFFFFF",
                            fg="#123E73",
                            font=("Calibri",18,"bold")).place(x=20,y=90)
        self.phone=Entry(self.s_footer,bg="#FFFFFF",fg="grey",font=("Calibri",13),width=25)
        self.phone.place(x=150,y=90,height=30);
        self.phone.insert(0,"Enter Phone Number")
        self.phone.bind("<FocusIn>",lambda event:Clear_code(event,self.phone,"Enter Phone Number"))
        self.phone.bind("<FocusOut>",lambda event:Restore(event,self.phone,"Enter Phone Number"))
        #==============Gender==========================
        Label(self.s_footer,text="Gender",
                                bg="#FFFFFF",
                                fg="#123E73",
                                font=("Calibri",18,"bold")).place(x=20,y=170)
        self.gender=Entry(self.s_footer,bg="#FFFFFF",fg="grey",font=("Calibri",13),width=25)
        self.gender.place(x=150,y=170,height=30);
        self.gender.insert(0,"Enter Gender")
        self.gender.bind("<FocusIn>",lambda event:Clear_code(event,self.gender,"Enter Gender"))
        self.gender.bind("<FocusOut>",lambda event:Restore(event,self.gender,"Enter Gender"))

        #========================== email==========================
        Label(self.s_footer,text="Email ID",
                                    bg="#FFFFFF",
                                    fg="#123E73",
                                    font=("Calibri",18,"bold")).place(x=17,y=250)
        self.email=Entry(self.s_footer,bg="#FFFFFF",fg="grey",font=("Calibri",13),width=25)
        self.email.place(x=150,y=250,height=30);
        self.email.insert(0,"Enter Email ID")
        self.email.bind("<FocusIn>",lambda event:Clear_code(event,self.email,"Enter Email ID"))
        self.email.bind("<FocusOut>",lambda event:Restore(event,self.email,"Enter Email ID"))

        #======================ADDRESS============================
        Label(self.s_footer,text="Address",
                                        bg="#FFFFFF",
                                        fg="#123E73",
                                        font=("Calibri",18,"bold")).place(x=17,y=330)
        self.address=Text(self.s_footer,bg="#FFFFFF",fg="black",font=("Calibri",13),width=40,height=5)
        self.address.place(x=150,y=330)

        self.middle=Frame(self.s_footer,
                    highlightbackground="#D3D3D3",
                    highlightthickness=1) 
        self.middle.place(x=570,y=13,height=430)

        #============Department=========================
        self.department=StringVar()
        Label(self.s_footer,
                    text="Department",
                    bg="white",
                    fg="#123E73",
                    font=("Calibri",18,"bold")).place(x=650,y=10);
                
        self.dept=ttk.Combobox(self.s_footer,
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
                                            width=30,
                                            textvariable=self.department,
                                            font=("Calibri",13))
        self.dept.current(0);
        self.dept.place(x=850,y=13)
        #==================DATE OF BIRTH========================

        Label(self.s_footer,text="Date of Birth",
                            bg="#FFFFFF",
                            fg="#123E73",
                            font=("Calibri",18,"bold")).place(x=650,y=80)
        self.dob=DateEntry(self.s_footer,
                            font=("Calibri",13),fg="white",bg="black",
                            width=30,
                            date_pattern="yyyy-mm-dd",
                            mindate=date(self.today.year-60,1,1),
                            maxdate=date(self.today.year-15,self.today.month,self.today.day))
        self.dob.place(x=850,y=84)
        #======================DATE OF JOINING========================

        Label(self.s_footer,text="Date of joining",
                                bg="#FFFFFF",
                                fg="#123E73",
                                font=("Calibri",18,"bold")).place(x=650,y=150)
        self.doj=DateEntry(self.s_footer,bg="white",width=30,fg="black",date_pattern="yyyy-mm-dd",font=("Calibri",13))
        self.doj.place(x=850,y=154)

        #================EMPLOYMENT STATUS=========================
        self.status=StringVar()

        Label(self.s_footer,
                    text="Employment Status",
                    bg="white",
                    fg="#123E73",
                    font=("Calibri",18,"bold")).place(x=630,y=220)
        self.emp=ttk.Combobox(self.s_footer,
                                    values=["Select Status",
                                            "Active",
                                            "Inactive",
                                            "On Leave",
                                            "Resigned",
                                            "Terminated"],
                                            state="readonly",
                                            width=30,
                                            textvariable=self.status,
                                            font=("Calibri",13))
        self.emp.current(0);
        self.emp.place(x=850,y=224)

        #=======================DESIGNATION==============================

        self.designationvalue=StringVar()
                
        Label(self.s_footer,
                            text="Designation",
                            bg="white",
                            fg="#123E73",
                            font=("Calibri",18,"bold")).place(x=650,y=300);
                        
        self.designation=ttk.Combobox(self.s_footer,
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
                                                    width=30,
                                                    textvariable=self.designationvalue,
                                                    font=("Calibri",13))
        self.designation.current(0);
        self.designation.place(x=850,y=304)

        #==============Employment Type=======================
        self.emptype=StringVar()
        Label(self.s_footer,
                            text="Employment Type",
                            bg="white",
                            fg="#123E73",
                            font=("Calibri",18,"bold")).place(x=630,y=360);
                        
        self.e_type=ttk.Combobox(self.s_footer,
                                                 values=["Select Employment Type",
                                                        "Full-Time",
                                                        "Part-Time",
                                                        "Contract",
                                                        "Internship",
                                                        ],
                                                    state="readonly" ,
                                                    width=30,
                                                    textvariable=self.emptype,
                                                    font=("Calibri",13))
                
        self.e_type.current(0);
        self.e_type.place(x=850,y=364)

        #================UPDATE BUTTON====================
        self.update_btn=Button(self.s_footer,
                                text="Update",
                                font=("Calibri",16,"bold"),
                                bg="#3E8CEA",
                                fg="white",
                                relief=FLAT,
                                padx=30,
                                command=lambda:self.update_value(u_win))
        self.update_btn.place(x=660,y=400)

        
        self.reset_btn=Button(self.s_footer,
                                    text="Reset",
                                    font=("Calibri",16,"bold"),
                                    bg="grey",
                                    relief=FLAT,
                                    fg="white",padx=30,
                                    command=lambda:self.reset_func(u_win))
        self.reset_btn.place(x=1030,y=400)

        self.close_btn=Button(self.s_footer,
                                            text="Close",
                                            font=("Calibri",16,"bold"),
                                            bg="red",
                                            relief=FLAT,
                                            fg="white",padx=30,
                                            command=lambda:self.close_windoww(u_win,root1))
        self.close_btn.place(x=850,y=400)

    #===================SEARCH EMPLOYEEE======================================================
    def update_value(self,u_win):
        employeeId=self.emp_id.get()
        
        #=================EMPLOYEE ID VALIDATION=======================
        if not employeeId.isdigit():
            messagebox.showerror("Invalid Input","Employee ID should be numeric")
            return
        else:
            employeeId=int(employeeId)
                          
        #=======================VALIDATION CHECK=====================

        fname=self.name.get()
        add=self.address.get(1.0,END)
        mail=self.email.get()
        gender_value=self.gender.get()
        dept_value=self.department.get()
        Status=self.status.get()
        desig_value=self.designationvalue.get()
        employee_type=self.emptype.get()
        
        #===============================BLANK VALIDATION=====================

        if fname=="" or fname=="Enter Full Name" or fname.isspace() or add.strip()==""or add.isspace() or mail=="" or mail.isspace() or mail=="Enter Email ID":
                        messagebox.showerror("Invalid Input","All Fields are Required to fill.",parent=u_win)
                        return
        #======================GENDER VALIDATION=====================

        if gender_value not in ["Male","Female","Others"]:
            messagebox.showerror("Invalid Gender","Gender must be Male or Female or Others",parent=u_win)
            return      
        #====================NAME VALIDATION====================

        fname=fname.replace(" ","")
        if not fname.isalpha():
            messagebox.showerror("Invalid Input","Name should contain only alphabets",parent=u_win)
            return
        else:
            fname=self.name.get()
#=================EMAIL VALIDATION===================

        if not mail[0].isalpha() or not mail.endswith("@gmail.com") or " " in mail:
            messagebox.showerror("Invalid Email","Email is incorrect,Please try again!",parent=u_win)
            return

        #=================PHONE NUMBER VALIDATION===================

        mob=self.phone.get()
        if mob.isdigit()==False:
            messagebox.showerror("Invalid Input","Mobile Number must contain only digits.",parent=u_win)
            return
        if len(mob)!=10:
            messagebox.showerror("Invalid Input","Mobile Number must be exactly 10 digits.",parent=u_win)
            return
        if mob[0] not in "6789":
            messagebox.showerror("Invalid Input","Mobile Number must start with 6,7,8 or 9.",parent=u_win)
            return

        #====================DATE OF JOINING VALIDATION=======================

        doj_value=self.doj.get_date() 
        dob_value=self.dob.get_date()  
        if doj_value<=dob_value:
            messagebox.showerror("invalid Input","Date of Birth cannot be greater than or equal to Date of Joinning",parent=u_win)
            return
        #===================COMBOBOX VALIDATION====================
        if dept_value == "Select department":
            messagebox.showerror(
                "Invalid Input",
                "Please select Department",
                parent=u_win
            )
            return

        if Status == "Select Status":
            messagebox.showerror(
                "Invalid Input",
                "Please select Employment Status",
                parent=u_win
            )
            return

        if desig_value == "Select Designation":
            messagebox.showerror(
                "Invalid Input",
                "Please select Designation",
                parent=u_win
            )
            return

        if employee_type == "Select Employment Type":
            messagebox.showerror(
                "Invalid Input",
                "Please select Employment Type",
                parent=u_win
            )
            return
                
    #=======================UPDATE DATA============================
    
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="")
            cursor=conn.cursor()
            cursor.execute("USE employeedb")
            cursor.execute("""
                UPDATE employee
                SET
                FULL_NAME=%s,
                GENDER=%s,
                DATE_OF_BIRTH=%s,
                CONTACT_NO=%s,
                EMAIL_ID=%s,
                ADDRESS=%s,
                DEPARTMENT=%s,
                DATE_OF_JOINING=%s,
                DESIGNATION=%s,
                EMPLOYMENT_STATUS=%s,
                EMPLOYMENT_TYPE=%s
            WHERE EMPLOYEE_ID=%s
            """,(fname,
                    gender_value,
                    dob_value,
                    mob,
                    mail,
                    add,
                    dept_value,
                    doj_value,
                    desig_value,
                    Status,
                    employee_type,
                    employeeId
                    ))
            conn.commit()
            conn.close()
      
            messagebox.showinfo("Updated Data","Data Updated Successfully",parent=u_win)
            #===============AFTER SUCCESSFULLY UPDATED DATA REMOVED FROM FORM==============
            self.emp_id.delete(0,END)
            self.emp_id.insert(0,"Enter Employee ID")
            self.emp_id.config(fg="grey")
            self.phone.delete(0,END)
            self.phone.insert(0,"Enter Phone Number")
            self.phone.config(fg="grey")
            self.address.delete("1.0",END)
            self.name.delete(0,END)
            self.name.insert(0,"Enter Full Name")
            self.name.config(fg="grey")
            self.email.delete(0,END)
            self.email.insert(0,"Enter Email ID")
            self.email.config(fg="grey")
            self.dept.current(0)  # we can also used set()it take a value not index
            self.emp.current(0)
            self.designation.current(0)
            self.e_type.current(0)
            self.dob.set_date(date(self.today.year-15,self.today.month,self.today.day))
            self.doj.set_date(date(self.today.year,self.today.month,self.today.day))
            self.gender.delete(0,END)
            self.gender.insert(0,"Enter Gender")
            self.gender.config(fg="grey")
            self.emp_id.focus_set()

        except Exception as e:
             messagebox.showerror("Error",f"Database Error:\n{str(e)}",parent=u_win)

    def search_employee(self,u_win):
            employeeId=self.emp_id.get()
            
            #=================EMPLOYEE ID VALIDATION=======================
            if not employeeId.isdigit():
                messagebox.showerror("Invalid Input","Employee ID should be numeric",parent=u_win)
                return
            else:
                employeeId=int(employeeId)
                              
           
            #===========INSERT DATA INTO TABLE==================
            try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="")
                    cursor=conn.cursor()
                    cursor.execute("USE employeedb")
                    cursor.execute("Select * From employee where Employee_ID=%s",(employeeId,))
                    check=cursor.fetchone()
                    if check==None:
                          messagebox.showerror("Invalid ID","Employee Not Found")
                          cursor.close()
                          conn.close()
                          return

                    
                    self.phone.delete(0,END)
                    self.phone.insert(0,check[4])
                    self.phone.config(fg="black")
                    self.address.delete("1.0",END)
                    self.address.insert("1.0",check[6])
                    self.address.config(fg="black")
                    self.name.delete(0,END)
                    self.name.insert(0,check[1])
                    self.name.config(fg="black")
                    self.email.delete(0,END)
                    self.email.insert(0,check[5])
                    self.email.config(fg="black")
                    self.dept.set(check[7])
                    self.emp.set(check[10])
                    self.designation.set(check[9])
                    self.e_type.set(check[11])
                    self.dob.set_date(check[3])
                    self.doj.set_date(check[8])
                    self.gender.delete(0,END)
                    self.gender.insert(0,check[2])
                    self.gender.config(fg="black")
                    cursor.close()
                    conn.close()

                    messagebox.showinfo(
                        "Employee Found",
                        "Employee details loaded successfully.",
                        parent=u_win
                    )

            except Exception as e:
                        messagebox.showerror("Error",f"Database Error:\n{str(e)}",parent=u_win)
    
                   
    def reset_func(self,u_win):
            self.emp_id.delete(0,END)
            self.emp_id.insert(0,"Enter Employee ID")
            self.emp_id.config(fg="grey")
            self.phone.delete(0,END)
            self.phone.insert(0,"Enter Phone Number")
            self.phone.config(fg="grey")
            self.address.delete("1.0",END)
            self.name.delete(0,END)
            self.name.insert(0,"Enter Full Name")
            self.name.config(fg="grey")
            self.email.delete(0,END)
            self.email.insert(0,"Enter Email ID")
            self.email.config(fg="grey")
            self.dept.current(0)  # we can also used set()it take a value not index
            self.emp.current(0)
            self.designation.current(0)
            self.e_type.current(0)
            self.dob.set_date(date(self.today.year-15,self.today.month,self.today.day))
            self.doj.set_date(date(self.today.year,self.today.month,self.today.day))
            self.gender.delete(0,END)
            self.gender.insert(0,"Enter Gender")
            self.gender.config(fg="grey")
            self.emp_id.focus_set()


    def close_windoww(self,u_win,root1):
                u_win.destroy();
                root1.deiconify();
              


