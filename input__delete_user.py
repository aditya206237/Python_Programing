import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="adit_python_db",
)

mycursor = mydb.cursor()
no=input("Enter the number:-")

sql = f"DELETE FROM details_of_student WHERE id = %s"

mycursor.execute(sql, (no,))

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")