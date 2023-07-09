def update_set(cursor: object, connection: object, table_name:str):

    string = ""
    update_str = ""

    titles_arr = input("enter titles for update by coma\n").split(", ")
    rows_arr = input("enter rows for update\n").split(", ")
    set_row = input("enter needed updates by coma: \n").split(", ")

    arr_lenth = len(titles_arr)
    i = 0

    string += titles_arr[i] + " = " + '"'+ rows_arr[i]+'"'

    while i < arr_lenth:
        if i == arr_lenth - 1:
            update_str += titles_arr[i] + " = " + '"'+ set_row[i]+'"'
        
        else:
            update_str += titles_arr[i] + " = " + '"'+ set_row[i]+'"' + ", "

        i += 1

    cursor.execute(f"""
        UPDATE {table_name} SET {update_str} WHERE {string};
    """)

    connection.commit()

    return (cursor)
    