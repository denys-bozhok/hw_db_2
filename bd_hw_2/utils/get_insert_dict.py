def get_insert_dict(instance: dict) -> dict:

    insert_keys = []
    insert_values = []

    for key, value in instance.items():
        if key == "id":
            continue

        elif type(value) == int:
            value = str(value)
            insert_values.append(value)
            
        elif type(value) == str:
            value = f'"{value}"'
            insert_values.append(value)
        
        insert_keys.append(key)
        
    for_insert_dict = {
        "insert_keys": insert_keys,
        "insert_values": insert_values
    }

    return for_insert_dict
