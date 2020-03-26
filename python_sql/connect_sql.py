# pyodbc is a open source Python module that makes accessing ODBC databases simple
# an ODBC driver uses the Open Database Connectivity (ODBC) interface by Microsoft
# that allows applications to access data in database management systems (DBMS)
# using SQL as a standard for accesssing the data
# pyodbc is an implementation of a driver that allows you to connect to pretty much any database

import pyodbc

server = "localhost,1433"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"

# connecting to Northwind database
docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+ password)

# a cursor itself is a control structure that allows us to control and manage rows of data from a response
# like an object in a class
cursor = docker_Northwind.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone() #fectchone will only fetch one result the first row
print("The row is", row)

customer_row = cursor.execute("SELECT * FROM Customers;").fetchone()
print("Customer row is", customer_row)

customer_rows = cursor.execute("SELECT * FROM Customers;").fetchall() #fetchall fetch all the rows
print("All customer rows are", customer_rows)

# list out only the unit price from the product table
product_rows = cursor.execute("SELECT * FROM Products;").fetchall()
print("Unit Price")
for record in product_rows:
    print(record.UnitPrice)

# list out last name from the employees table
employees = cursor.execute("SELECT * FROM Employees;").fetchall()
print("Last Name")
for name in employees:
    print(name.LastName)

# list name of employees who live either in London or Seattle
employees = cursor.execute("SELECT * FROM Employees WHERE City IN ('London', 'Seattle');").fetchall()
print("Name")
for record in employees:
    print(record.FirstName, record.LastName)

# not using record (for loop) will print everything together and looks clumpsy
employees = cursor.execute("SELECT FirstName + ' ' + LastName AS 'Name' FROM Employees WHERE City IN ('London', 'Seattle');").fetchall()
print(employees)