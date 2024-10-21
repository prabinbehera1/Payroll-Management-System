# Payroll Management System

This is a Payroll Management System created using **Python's Tkinter** library for the GUI and **MySQL** as the backend database. The system allows the user to manage employee records, calculate payrolls, and update employee salary information.

## Features

- Add new employee records.
- Calculate net salary based on hours worked, gross pay rate, medical, tax, and bonus.
- Print salary receipts for employees.
- Update and delete employee salary details.
- Simple and user-friendly interface using Tkinter.

## Requirements

To run this project, you need to have the following installed:

- Python 3.x
- Tkinter (comes pre-installed with Python)
- MySQL Server
- MySQL Connector for Python

### Install MySQL Connector
You can install the MySQL connector using pip:
```bash
pip install mysql-connector-python
```

### Project Structure
``` bash
├── payroll.py          # Main file containing the Payroll Management System logic
├── README.md           # Project README file
```
### MySQL Database Setup

1. Make sure you have MySQL server running on your machine.
2. Create a database named payroll in MySQL
``` SQL
CREATE DATABASE payroll;
```
3. Create a table named payroll in the payroll database:
   ``` SQL
   CREATE TABLE payroll (
    empid INT PRIMARY KEY,
    name VARCHAR(50),
    doj DATE,
    basic DECIMAL(10, 2),
    medical DECIMAL(10, 2),
    bonus DECIMAL(10, 2),
    tax DECIMAL(5, 2),
    salary DECIMAL(10, 2));

### Usage 

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/payroll-management-system.git
2. Open the payroll.py file and update the MySQL connection credentials as per your local setup:
   ```python
   mysql_con = mysql.connect(host='localhost', user='root', passwd='your_password', database='payroll')
3. Run the payroll.py file:
   ```bash
   python payroll.py
4. The Payroll Management System GUI will open, and you can start managing employee records.

### Future Improvements
1. Add more validations for input fields.
2. Implement user authentication to protect sensitive payroll data.
3. Enhance UI/UX with modern design and better form handling.
