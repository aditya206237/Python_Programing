import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",    
    database="adit_python_db",
)
mycursor = mydb.cursor()
naam = input("Enter the name to view data:-")

sql = f"SELECT * FROM details_of_student WHERE name = %s"
mycursor.execute(sql, (naam,))

myresult = mycursor.fetchall()

for x in myresult:
    print(x)