import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="host",
    password="",
    database="aditya_python_db",
)
mycursor = mydb.cursor() # connect With Database

sql = "INSERT INTO student_details (name, age) VALUES (%s, %s)"
val = ("Aditya","aditdtudy879@gmail.com")
mycursor.execute(sql, val)

mydb.commit() # Save Into Table
print(mycursor.rowcount, "record inserted.")