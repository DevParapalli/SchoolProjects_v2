"Write a Program to show database connectivity of python Data Frames with mysql database"
import mysql.connector
import pandas

# Boilerplate code 
database = mysql.connector.connect(
    host="127.0.0.1",
    user="python",
    password="python",
    database="python"
)
# pass this to function
cursor = database.cursor(buffered=True)

# Database contains name and addr only, in table person

def add_data(name:str, addr:str, cursor=cursor):
    sql = f'INSERT INTO person VALUES ("{name}", "{addr}");'
    cursor.execute(sql)
    database.commit()

def remove_data(id:int, cursor=cursor):
    sql = f"DELETE FROM person WHERE id={id};"
    cursor.execute(sql)
    database.commit()

def update_data(name:str, addr:str, id:int, cursor=cursor):
    sql = f"UPDATE person SET name = '{name}' addr = '{addr}' WHERE id={id}; "
    cursor.execute(sql)
    database.commit()

def dump_data():
    sql = "SELECT * FROM person"
    cursor.execute(sql)
    database.commit()

def main():
    dump_data()
    result = cursor.fetchall()
    df = pandas.DataFrame(result)
    print(df)

if __name__ == "__main__":
    main()

__OUTPUT__ = """
   0       1       2
0  1     Dev  Nagpur
1  2   Patil   Delhi
2  3   Kural   Patna
3  4  George  Indore
"""