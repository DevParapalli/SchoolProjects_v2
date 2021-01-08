"Write a Program to show MySQL database connectivity in python."
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1", # Loopback to self.
    user="python",
    password="python",
    database="python"
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# optional here
mycursor.execute(
    "CREATE TABLE person (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), addr VARCHAR(255))")

sql = "INSERT INTO person (name, addr) VALUES (%s, %s)"

val = [
    ('Dev', 'Nagpur'),
    ('Patil', 'Delhi'),
    ('Kural', 'Patna'),
    ('George', 'Indore'),
]

mycursor.executemany(sql, val)

mydb.commit()  # finalizes the connection


__OUTPUT__ = """
+----+--------+--------+
| id | name   | addr   |
+----+--------+--------+
|  1 | Dev    | Nagpur |
|  2 | Patil  | Delhi  |
|  3 | Kural  | Patna  |
|  4 | George | Indore |
+----+--------+--------+
4 rows in set (0.01 sec)
"""