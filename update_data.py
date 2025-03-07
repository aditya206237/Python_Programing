import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="adit_python_db",
)
no = input("Enter the number to be updated:-")
name = input("Enter the new name:-")
email = input("Enter the new email:-")

mycursor = mydb.cursor()

sql = "UPDATE details_of_student SET name = %s, email = %s WHERE id = %s"
mycursor.execute(sql, (name, email, no))

mydb.commit()
print(mycursor.rowcount,"Record updated successfully")

