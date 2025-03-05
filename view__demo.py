import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="adit_python_db",
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM details_of_student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)