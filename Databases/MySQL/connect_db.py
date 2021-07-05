import mysql.connector

mydb = mysql.connector.connect(host='127.0.0.1',
                               user='root', password='root',
                               port='3306',
                               database='music_shop')

mydb.close()
