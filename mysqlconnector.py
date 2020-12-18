import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "Rachana", password = "Password@45")

mycursor = mydb.cursor()
mycursor.execute("show databases")
result = mycursor.fetchall()
for i in result:
    print(i)