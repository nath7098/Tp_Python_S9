import sqlite3
import csv
from scripts.TP5.database_utils import *

if __name__ == '__main__':

    data_communes = parser('../../resources/communes.csv', 7, 8)
    data_departments = parser('../../resources/departements.csv', 7, 8)
    data_region = parser('../../resources/regions.csv', 7, 8)


    db = sqlite3.connect('../../resources/database/database.sqlite')

    create_table_communes(db, data_communes)
    create_table_departements(db, data_departments)
    create_table_regions(db, data_region)

    db.close()

