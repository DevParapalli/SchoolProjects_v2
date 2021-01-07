"Write a Program to show database connectivity of python Data Frames with mysql database"
import mysql.connector

# Boilerplate code 
database = mysql.connector.connect(
    host="localhost",
    user="this_is_not_a_user",
    password="this_is_not_a_password",
    database="this_is_not_a_database"
)
# pass this to function
cursor = database.cursor()

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
    
def main():
    print("Try using the script with -i flag, then use the prompt to issue commands")

if __name__ == "__main__":
    main()