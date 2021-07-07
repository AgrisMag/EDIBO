import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="music_shop"
)
cursor = mydb.cursor()
cursor.execute("SET FOREIGN_KEY_CHECKS=0")

file_to_read = open('chinook_dump.txt', 'r', encoding='utf8')
file_to_write = open('data_out.sql', 'w', encoding='utf8')
data = file_to_read.read()
data_lines = data.split('\n')[:-1]

for line in data_lines[:-1]:
    if line.startswith("INSERT") and 'sqlite' not in line:
        file_to_write.write(line + "\n")
for line in open("data_out.sql", encoding='utf8'):
    cursor.execute(line)
cursor.execute("SET FOREIGN_KEY_CHECKS=1")
mydb.commit()
file_to_read.close()
file_to_write.close()
