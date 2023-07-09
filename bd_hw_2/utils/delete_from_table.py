def delete_from_table(cursor: object, connection: object, name: str):
    col_name = input("enter col name for delete row")
    row_indificator = input("enter indificator for delete row")


    cursor.execute (f"""
        DELETE FROM {name} WHERE {col_name} = "{row_indificator}";
    """)

    connection.commit()

    return cursor