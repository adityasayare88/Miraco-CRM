import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='admin@MYSQL#2003',
    auth_plugin='mysql_native_password'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE miraco")
print("All Done!!")