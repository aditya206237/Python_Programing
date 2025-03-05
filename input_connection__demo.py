import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="adit_python_db",
)
mycursor = mydb.cursor()
name=input("Enter the name:--")
email=input("Enter the email:--")
sql = "INSERT INTO details_of_student (name,email) VALUES (%s, %s)"
val = (name,email)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")