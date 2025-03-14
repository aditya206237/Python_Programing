import mysql.connector
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="adit_python_db",
        )
mycursor = mydb.cursor()
print("For Inserting Data write=> insert data")
print("For Viewing Data write=> view data")
print("For Deleting the Data write=> delete data")
print("For Updating the Data write=> update data")

lang = input("Enter the function name you want to perform:-")
match lang:
    case "insert data":
        name = input("Enter the name:--")
        email = input("Enter the email:--")
        sql = "INSERT INTO details_of_student (name,email) VALUES (%s, %s)"
        val = (name, email)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted")

    case "view data":        
        mycursor.execute("SELECT * FROM details_of_student")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    case "delete data":        
        sql = "DELETE FROM details_of_student WHERE id = '1'"

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted")

    case "update data":

        no = input("Enter the number to be updated:-")
        name = input("Enter the new name:-")
        email = input("Enter the new email:-")
        sql = "UPDATE details_of_student SET name = %s,email = %s WHERE id = %s"

        mycursor.execute(sql, (name, email, no,))

        mydb.commit()

    case _:
        print("Nothing")
        