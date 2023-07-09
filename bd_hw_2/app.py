from components.Human import *
from components.Auto import *
from components.House import *

from utils.db_utils import create_db, get_data

from utils.create_table import create_table
from utils.delete_table import delete_table
from utils.insert_table import insert_table

from utils.delete_from_table import delete_from_table
from utils.update_set import update_set
from utils.fetch import *

from utils.get_class_name import get_class_name
from utils.get_list_for_colum_names import get_list_for_colum_names
from utils.get_insert_dict import get_insert_dict



def main():

    # ~-----------------INSTANCES-----------------
    humans = [Human("GR4323431", "Dionis", "Grek", 1).__dict__,
              Human("UA0531563", "Oleg", "Wachowski", 2).__dict__,
              Human("R00010D0010", "R2", "D2", 3).__dict__
              ]

    autos = [Auto("Neorion Chicago", "black", "THC-0420").__dict__,
             Auto("ZAZ Lanos", "green", "AH3548CK").__dict__,
             Auto("Tesla Cybertruck", "sikver", "77TC1").__dict__
             ]
    
    houses = [House("Greece, Vyronas, Tralleon 12, 162 31", 69, "GR4323431").__dict__,
              House("Ukraine, Dnipro, Berehova 66, 49021", 35, "UA0531563").__dict__,
              House("Space, Black hole NIGA777 13, 13445", 68, "R00010D0010").__dict__
              ]

    # ~-----------------CREATE_DB-----------------
    # db_name = input("Enter DB name\n")
    
    db_cursor = create_db("hw2_db")

    cursor, connection = get_data(db_cursor)


    # ~-----------------CREATE_TABLE
    # ~(if Foregn key - True(input col_name, tablem col_name-----------------
    # table_name = get_class_name(Auto)
    # table_dict = get_list_for_colum_names(autos[0], table_name)

    # create_table(cursor, connection, table_dict, False)

    # ~-----------------DELETE_TABLE-----------------
    # table_name = get_class_name(Auto)
    # delete_table(cursor, connection, table_name)


    # ~-----------------INSERT_INTO_TABLE-----------------
    # table_name = get_class_name(Auto)

    # for inst in autos:

    #     insert_dict = get_insert_dict(inst)
    #     insert_table(cursor, connection, insert_dict, table_name)


    # *-----------------FETCH all(False)[index?]/one(True)/many(Int)-----------------
    # table_name = get_class_name(Auto)
    # table_dict = get_list_for_colum_names(autos[0], table_name)

    # print(fetch(cursor, connection, table_name, False))

    
    # *-----------------DELETE FROM(inpuy table_name, row)-----------------
    # table_name = get_class_name(House)

    # delete_from_table(cursor, connection, table_name)


    # *-----------------SET-----------------
    table_name = get_class_name(Human)

    update_set(cursor, connection, table_name)


if __name__ == "__main__":
    main()

