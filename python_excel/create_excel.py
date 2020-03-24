# create an excel file using python

# import xlsxwriter module
import xlsxwriter

# creating a workbook using the bultin method and assigning a name to our file
data9 = xlsxwriter.Workbook("data9.xlsx")

# create an object
worksheet = data9.add_worksheet("Trainees")

# note - rows and columns are zero indexed
# first cell in a worksheet A1 is (0, 0), B1 is (0, 1)

# using the builtin write method we inserted data to our file
worksheet.write("A1", "Data 9")
# worksheet.write("A2", "Andy")
# worksheet.write("A3", "Ben")
# worksheet.write("A4", "CJ")
# worksheet.write("A5", "Gigi")
# worksheet.write("A6", "Johnny")
# worksheet.write("A7", "Khanhi")
# worksheet.write("A8", "Sassy")
# worksheet.write("A9", "Shugs")
# worksheet.write("A10", "Tosin")
# worksheet.write("A11", "Vivek")
# worksheet.write("A12", "Weiyee")
# worksheet.write("A13", "Yin")

# efficient method to inset names under the Data 9 column
row = 2
column = 0

content = ["First Name", "Andy", "Ben", "CJ", "Gigi", "Johnny", "Khanhi", "Sassy", "Shugs", "Tosin", "Vivek", "Weiyee", "Yin"]

for name in content:
    worksheet.write(row, column, name)
    row += 1

# we used close method to save and close our file
data9.close()

