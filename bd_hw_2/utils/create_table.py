def create_table(cursor: object, connection: object, titles_dict: dict, foreign_key: bool):    
    string = ''

    name = titles_dict["name"]

    for el in titles_dict:
        string = ", ".join(titles_dict["colums_titles"])
    
    if foreign_key:
        f_key_colum_title = input("Foreign key:\n")
        reference_table = input("Reference table:\n")
        reference_colum_title = input("Reference colum:\n")

        f_key_string = f", FOREIGN KEY ({f_key_colum_title}) REFERENCES {reference_table}({reference_colum_title})"

        string += f_key_string
        print (string)

    cursor.execute(f"""
                      CREATE TABLE IF NOT EXISTS {name}({string});
                      """) 
    
    connection.commit()

    return cursor