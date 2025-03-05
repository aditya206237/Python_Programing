import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="adit_python_db",
)

mycursor = mydb.cursor()

sql = "DELETE FROM details_of_student WHERE id = '3'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")