import mysql.connector
class DataBase:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "adit_python_db"
        )
        self.mycursor = self.mydb.cursor()
    def insertData(self, name, email):
        self.name=name
        self.email=email
        sql = "INSERT INTO details_of_student (name, email) VALUES (%s, %s)"
        val = (name, email)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record inserted.")
    def viewData(self):
        self.mycursor.execute("SELECT * FROM details_of_student")
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)
    def deleteData(self):
        no = input("Enter the ID of the record to delete:-")
        sql = "DELETE FROM details_of_student WHERE id = %s"
        self.mycursor.execute(sql, (no,))
        self.mydb.commit()
        print(self.mycursor.rowcount, "record deleted.")
    def updateData(self):
        no = input("Enter the number to be updated:-")
        name = input("Enter the new email:-")
        email = input("Enter the new email:-")
        sql = "UPDATE details_of_student SET name = %s, email = %s WHERE id = %s"
        self.mycursor.execute(sql, (name, email, no))
        self.mydb.commit()
        print(self.mycursor.rowcount, "record updated succesfully.")

print("For inserting data enter=>1")
print("For viewing data enter=>2")
print("For deleting data enter=>3")
print("For updating data enter=>4")
d=DataBase()
choice = int(input("Enter your choice:-"))
if choice==1:
    name = input("Enter the name:-")
    email = input("Enter the email:-")
    d.insertData(name, email)
elif choice==2:
    d.viewData()
elif choice==3:
    d.deleteData()
elif choice==4:
    d.updateData()
else:
    print("Invalid choice")
    