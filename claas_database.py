class Database:
    def setData(self,name,email,no):
        self.name=name
        self.email=email
        self.no=no
    def import_data(self):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="adit_python_db",
        )
        mycursor=mydb.cursor()
    def insert_data(self):
        self.no = input("Enter the no: ")
        self.name = input("Enter the name: ")
        self.email = input("Enter the email: ")
    def view_data(self):
        self.mycursor.execute("SELECT * FROM details_of_student")
        result = self.mycursor.fetchall()
        for row in result:
            print(row)

def __init__(self):
    import mysql.connector
    self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="adit_python_db",
    )
    self.mycursor = self.mydb.cursor()
    def delete_data(self):
        no = input("Enter the no of the record to delete: ")
        sql = "DELETE FROM details_of_student WHERE no = %s"
        val = (no,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("Data deleted successfully.")

    def update_data(self):
        no = input("Enter the no of the record to update: ")
        name = input("Enter the new name: ")
        email = input("Enter the new email: ")
        sql = "UPDATE details_of_student SET name = %s, email = %s WHERE no = %s"
        val = (name, email, no)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("Data updated successfully.")

d = Database()
d.import_data()
d.insert_data()
d.view_data()
d.delete_data()
d.update_data()
