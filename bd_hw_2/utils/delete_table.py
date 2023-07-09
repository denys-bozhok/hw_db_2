def delete_table(cursor: object, connection: object, name: str):    
    cursor.execute(f"""
        DROP TABLE {name};
    """)

    connection.commit() 

    return cursor