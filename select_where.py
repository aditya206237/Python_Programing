import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",    
    database="adit_python_db",
)
mycursor = mydb.cursor()
no = input("Enter the number to view data:-")

sql = f"SELECT * FROM details_of_student WHERE id = %s"
mycursor.execute(sql, (no,))

myresult = mycursor.fetchall()

for x in myresult:
    print(x)