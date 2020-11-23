import sqlite3
import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
import html


def db_parser(filepath, col_names_index, data_index):
    data = []
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        line = 0
        for row in csv_reader:
            if line_count >= data_index and not row[0] == '':
                data.insert(line, row)
                line += 1
            line_count += 1

    return data


def xml_writer(filepath, db: sqlite3.Connection):
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    tree = ET.ElementTree()
    i = 0
    xml_root = ET.Element('data')
    for idx, table in enumerate(tables):
        cursor.execute("SELECT * FROM " + table[0] + ";")
        column_names = [description[0] for description in cursor.description]
        data = cursor.fetchall()
        table_data = ET.SubElement(xml_root, table[0])
        for row in data:
            row_data = ET.SubElement(table_data, 'row')
            for idx, value in enumerate(row):
                value_data = ET.SubElement(row_data, column_names[idx])
                value_data.text = str(value)
    tree._setroot(xml_root)
    tree.write(filepath)


def xml_parser(filepath):
    xmlstring = html.unescape(open(filepath, 'r').read())
    xmldoc = minidom.parseString(xmlstring)
    itemlist = xmldoc.getElementsByTagName('row')
    for item in itemlist.childNodes:
        for node in item:
            print(node[0].value)





################################################## COMMUNE #############################################################


def create_table_communes(db=sqlite3.Connection, data=None):
    if data is None:
        data = []

    # Creating table if doesn't exist
    statement = '''create table if not exists COMMUNES(
                        Code_commune VARCHAR(255) NOT NULL ,
                        Code_département VARCHAR(255) NOT NULL,
                        Nom_de_la_commune VARCHAR(255) NOT NULL,
                        Population_totale INTEGER(32),
                        PRIMARY KEY (Code_commune, Code_département)
                    )'''
    cursor = db.cursor()
    cursor.execute(statement)
    db.commit()

    # INSERT DATA #

    for d in data:
        pop = str(d[9])
        pop = pop.replace(" ", "")
        values = (d[5], d[2], d[6], int(pop))
        # inserting into table
        insert_statement = '''insert or ignore into COMMUNES(Code_commune, Code_département, Nom_de_la_commune, Population_totale)
                                values(?,?,?,?)'''
        cursor = db.cursor()
        cursor.execute(insert_statement, values)
    db.commit()


def same_name_communes(db: sqlite3.Connection):
    statement = '''select c1.Nom_de_la_commune, c1.Code_département from COMMUNES c1 '''

    cursor = db.cursor()
    cursor.execute(statement)
    res = cursor.fetchall()

    communes_dict = dict()

    for line in res:
        if line[0] in communes_dict:
            # append the new number to the existing array at this slot
            communes_dict[line[0]].append(line[1])
        else:
            # create a new array in this slot
            communes_dict[line[0]] = [line[1]]
    i = 0
    for k, v in communes_dict.items():
        if len(v) > 1:
            i += 1
            print(k, ":", v)
    print(i)


################################################## DEPARTEMENT #########################################################


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


def calc_department_population(code_dpt: str, db: sqlite3.Connection) -> int:
    population = 0
    statement = '''select c.Code_département, d.Nom_département, c.Population_totale
                    from COMMUNES c inner join DEPARTEMENTS d on (c.Code_département = d.Code_département)
                    where c.Code_département = ?'''

    cursor = db.cursor()
    cursor.execute(statement, (code_dpt,))
    table = cursor.fetchall()
    for v in table:
        population += int(v[2])
    return population


def print_all_departments_population(db: sqlite3.Connection):
    statement = '''select Code_département, Nom_département from DEPARTEMENTS'''

    cursor = db.cursor()
    cursor.execute(statement)
    departments = cursor.fetchall()
    for line in departments:
        print(line[1] + " : " + str(calc_department_population(line[0], db)))


################################################## REGION ##############################################################


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


def calc_region_population(code_reg: str, db: sqlite3.Connection) -> int:
    population = 0
    statement = '''select d.Code_région, r.Nom_région, d.Code_département, c.Population_totale
                    from (COMMUNES c inner join (
                        DEPARTEMENTS d inner join REGIONS r on d.Code_région = r.Code_région)
                        on c.Code_département = d.Code_département) 
                    where d.Code_région = ?'''

    cursor = db.cursor()
    cursor.execute(statement, (code_reg,))
    table = cursor.fetchall()
    for v in table:
        population += int(v[3])
    return population


def print_all_regions_population(db: sqlite3.Connection):
    statement = '''select Code_région, Nom_région from REGIONS'''

    cursor = db.cursor()
    cursor.execute(statement)
    departments = cursor.fetchall()
    for line in departments:
        print(line[1] + " : " + str(calc_region_population(line[0], db)))
