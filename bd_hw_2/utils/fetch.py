def fetch(cursor: object, connection: object, table_name: str, lenth):
    
    fetchall_query = cursor.execute(f"""
    SELECT * FROM {table_name}
    """)
    if lenth:  
        return fetchall_query.fetchmany(lenth)
    
    elif lenth == True :
        return fetchall_query.fetchone()
    
    elif lenth == False:
        return fetchall_query.fetchall()

    connection.commit()