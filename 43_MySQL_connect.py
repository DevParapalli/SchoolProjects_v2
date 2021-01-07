"Write a Program to show MySQL database connectivity in python."
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="dev_parapalli",
    password="thisisnotapassword",
    database="thisisnotadatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# optional here
mycursor.execute(
    "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

val = [
    ('Dev', 'Nagpur'),
    ('Patil', 'Delhi'),
    ('Kural', 'Patna'),
    ('George', 'Indore'),
]

mycursor.executemany(sql, val)

mydb.commit()  # finalizes the connection
