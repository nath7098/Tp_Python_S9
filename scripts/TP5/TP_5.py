from sqlite3 import *
from scripts.TP5.database_utils import *

if __name__ == '__main__':

    data_communes = db_parser('../../resources/communes.csv', 7, 8)
    data_departments = db_parser('../../resources/departements.csv', 7, 8)
    data_region = db_parser('../../resources/regions.csv', 7, 8)

    db = connect('../../resources/database/database.sqlite')
    # db.set_trace_callback(print)

    # Création et remplissage des tables

    create_table_communes(db, data_communes)
    create_table_departements(db, data_departments)
    create_table_regions(db, data_region)

    # print("DEPARTEMENTS :")
    # print_all_departments_population(db)
    # print("\nREGIONS :")
    # print_all_regions_population(db)

    same_name_communes(db)

    # XML WRITER

    # xml_writer("../../resources/xml_database.xml", db)
    #
    # db.close()
    #
    # # XML PARSER
    #
    # xml_parser('../../resources/xml_database.xml')
