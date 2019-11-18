import sqlite3
import csv


def parser(filepath, col_names_index, data_index):
    data = [[]]
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == col_names_index:
                data[0] = row
            elif line_count >= data_index:
                data += row
            line_count += 1
    return data


def create_table_communes(db=sqlite3.Connection, data=None):
    if data is None:
        data = []

    statement = '''create table if not exists COMMUNES('Code département', 'Code commune', 'Nom de la commune', 'Population totale')'''
    cursor = db.cursor()
    cursor.execute(statement)
    db.commit()


def insert_into_communes(db=sqlite3.Connection, data=None):
    if data is None:
        data = []



def create_table_departements(db=sqlite3.Connection, data=None):
    if data is None:
        data = []

    statement = '''create table if not exists DEPARTMENTS('Code département', 'Nom département', 'Code région')'''
    cursor = db.cursor()
    cursor.execute(statement)
    db.commit()


def create_table_regions(db=sqlite3.Connection, data=None):
    if data is None:
        data = []

    statement = '''create table if not exists REGIONS('Code région', 'Nom région')'''
    cursor = db.cursor()
    cursor.execute(statement)
    db.commit()