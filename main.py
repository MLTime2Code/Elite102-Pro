import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'example', password = 'SQL1Sh4rd2USE*')

cursor = connection.cursor()


testQuery = ("SELECT * FROM pokemon")

 

cursor.execute(testQuery)

 

for item in cursor:

    print(item)

 

cursor.close()

connection.close()
