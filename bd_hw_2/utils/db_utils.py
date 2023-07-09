import sqlite3

def create_db(db_name: str):
    
    connection = sqlite3.connect(db_name+".db")

    return connection
   

def get_data(connection):

    cursor = connection.cursor()

    return [cursor, connection]
