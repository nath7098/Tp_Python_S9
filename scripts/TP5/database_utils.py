import sqlite3
import csv


def parser(filepath, col_names_index, data_index):
    data = []
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        line = 1
        for row in csv_reader:
            if line_count == col_names_index:
                data.insert(0, row)
            elif line_count >= data_index:
                data.insert(line, row)
            line_count += 1

    return data


def create_table_communes(db=sqlite3.Connection, data=None):
    if data is None:
        data = []

    # Creating table if doesn't exist
    statement = '''create table if not exists COMMUNES(
                        Code_commune VARCHAR(255) NOT NULL ,
                        Code_département VARCHAR(255) NOT NULL,
                        Nom_de_la_commune VARCHAR(255) NOT NULL,
                        Population_totale INTEGER(16),
                        PRIMARY KEY (Code_commune, Code_département)
                    )'''
    cursor = db.cursor()
    cursor.execute(statement)
    db.commit()

    # INSERT DATA #

    for d in data:
        values = (d[5], d[2], d[6], d[9])
        # inserting into table
        insert_statement = '''insert or ignore into COMMUNES(Code_commune, Code_département, Nom_de_la_commune, Population_totale)
                                values(?,?,?,?)'''
        cursor = db.cursor()
        cursor.execute(insert_statement, values)
    db.commit()


def create_table_departements(db=sqlite3.Connection, data=None):
    if data is None:
        data = []

    # Creating table if doesn't exist
    statement = '''create table if not exists DEPARTEMENTS(
                        Code_région VARCHAR(255) NOT NULL,
                        Code_département VARCHAR(255) NOT NULL ,
                        Nom_département VARCHAR(255) NOT NULL,
                        PRIMARY KEY (Code_région, Code_département)
                    )'''
    cursor = db.cursor()
    cursor.execute(statement)
    db.commit()

    # INSERT DATA #

    for d in data:
        values = (d[0], d[2], d[3])
        # inserting into table
        insert_statement = '''insert or ignore into DEPARTEMENTS(Code_région, Code_département, Nom_département)
                                values(?,?,?)'''
        cursor = db.cursor()
        cursor.execute(insert_statement, values)
    db.commit()


def create_table_regions(db=sqlite3.Connection, data=None):
    if data is None:
        data = []

    # Creating table if doesn't exist
    statement = '''create table if not exists REGIONS(
                        Code_région VARCHAR(255) NOT NULL PRIMARY KEY ,
                        Nom_région VARCHAR(255) NOT NULL
                    )'''
    cursor = db.cursor()
    cursor.execute(statement)
    db.commit()

    # INSERT DATA #

    for d in data:
        values = (d[0], d[1])
        # inserting into table
        insert_statement = '''insert or ignore into REGIONS(Code_région, Nom_région)
                                    values(?,?)'''
        cursor = db.cursor()
        cursor.execute(insert_statement, values)
    db.commit()