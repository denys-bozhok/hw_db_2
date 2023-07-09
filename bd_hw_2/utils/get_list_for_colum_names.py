def get_list_for_colum_names(instance: dict, name: str) -> dict:

    for_colums_title_arr = []

    for key, value in instance.items():
        
        if key == "id":
            key += " INTEGER PRIMARY KEY AUTOINCREMENT"
            for_colums_title_arr.append(key)

        elif "_id" in key:
            key += " PRIMARY KEY"
            for_colums_title_arr.append(key)

        elif type(value) == int:
            key += " INT"
            for_colums_title_arr.append(key)

        elif type(value) == str:
            key += " TXT"
            for_colums_title_arr.append(key)

        else:
            for_colums_title_arr.append(key)

    for_coulums_name = {
        "name": name,
        "colums_titles": for_colums_title_arr
    }

    return for_coulums_name

