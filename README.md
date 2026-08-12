# Employee-Management-System-
A desktop-based Employee Management System developed using Python, Tkinter, and MySQL to efficiently manage employee records, personal details, job information, and salary details through an intuitive graphical interface.
🧑‍💼 Employee Management System

<p align="center">
  <strong>A Python-based Employee Management System built with Tkinter and MySQL</strong>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql">
  <img src="https://img.shields.io/badge/Pillow-Image%20Processing-green?style=for-the-badge">
</p>---

<h2><b>📌 About the Project</b></h2>Employee Management System is a Python-based desktop application designed to efficiently manage employee information and salary-related operations through an intuitive graphical user interface.<br><br>

The application uses <b>Tkinter</b> for the user interface and <b>MySQL</b> for storing and managing employee records. It provides essential operations such as adding, updating, searching, deleting, and viewing employee information.

---

<h2><b>✨ Features</b></h2><p><b>👤 Add Employee</b><br>
Add and store new employee information.</p><p><b>🔄 Update Employee</b><br>
Update existing employee records.</p><p><b>🔍 Search Employee</b><br>
Search and retrieve employee information.</p><p><b>🗑️ Delete Employee</b><br>
Remove employee records from the database.</p><p><b>👥 View Employees</b><br>
Display employee records in a structured table.</p><p><b>💰 Calculate Salary</b><br>
Calculate employee salary based on required details.</p><p>---

<h2><b>🛠️ Technologies Used</b></h2><h3><b>🐍 Python</b></h3>Used for application logic, event handling, data processing, and employee management operations.

<h3><b>🖥️ Tkinter</b></h3>Used to create the graphical user interface, including forms, buttons, menus, input fields, and tables.

<h3><b>🗄️ MySQL</b></h3>Used as the relational database for storing and managing employee records.

<h3><b>🔗 MySQL Connector</b></h3>Used to establish connectivity between the Python application and MySQL database.

<h3><b>🖼️ Pillow (PIL)</b></h3>Used for loading, resizing, and displaying images in the Tkinter interface.

---

<h2><b>🏗️ How It Works</b></h2><pre>
             👤 User
                │
                ▼
        ┌─────────────────┐
        │   Tkinter GUI   │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │  Python Logic   │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ MySQL Database  │
        └─────────────────┘
</pre>The user interacts with the Tkinter interface. Python processes the requested operation and communicates with the MySQL database to store or retrieve employee information.

---

<h2><b>🗄️ Database Operations</b></h2>The application performs the following CRUD operations:

- <b>CREATE / INSERT</b> → Add new employee records
- <b>READ / SELECT</b> → Search and view employee records
- <b>UPDATE</b> → Modify existing employee information
- <b>DELETE</b> → Remove employee records

The application uses <b>parameterized SQL queries</b> while interacting with the database.

---

<h2><b>🔄 Application Workflow</b></h2><pre>
Launch Application
⬇️
Connect to MySQL Database
⬇️
Select Employee Operation
⬇️
Enter / Retrieve Employee Details
⬇️
Process Request Using Python
⬇️
Execute SQL Query
⬇️
Display Result in Tkinter Interface
</pre>---

<h2><b>💡 Key Concepts Demonstrated</b></h2>
<p>-Python Programming</p>
<p>-Object-Oriented Programming</p>
<p>-Tkinter GUI Development</p>
<p>-Event Handling</p>
<p>-MySQL Database Connectivity</p>
<p>-SQL & CRUD Operations</p>
<p>-Parameterized Queries</p>
<p>-Form Handling</p>
<p>-Input Validation</p>
<p>-Image Processing<p>
<p>Application Development<p>
<h2><b>📂 Project Structure</b></h2><pre>
Employee-Management-System/
│
├── Python Files
├── Images / Assets
└── README.md
</pre>---

<h2><b>🚀 Setup & Installation</b></h2><h3><b>1. Clone the Repository</b></h3><pre>
git clone &lt;repository-https://github.com/shivangisahu-dev/Employee-Management-System-/edit/main/README.md;
</pre><h3><b>2. Install Dependencies</b></h3><pre>
pip install mysql-connector-python pillow
</pre><h3><b>3. Configure MySQL</b></h3>Create the required database and employee table in MySQL.

Update the MySQL connection details in the Python code according to your local setup.

<h3><b>4. Run the Application</b></h3><pre>
python Login.py
</pre>---

<h2><b>🎯 Project Highlights</b></h2><p align="center">
  <strong>Python</strong><br>
  <strong>Tkinter</strong><br>
  <strong>MySQL</strong><br>
  <strong>CRUD Operations</strong><br>
  <strong>Database Connectivity</strong>
</p>---

<h2><b>👩‍💻 Conclusion</b></h2>The Employee Management System demonstrates the practical implementation of a database-driven application using Python, Tkinter, and MySQL. It provides an organized way to manage employee records and perform essential employee and salary-related operations through a user-friendly interface.

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>
