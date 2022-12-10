"""Methods to interact with the MySQL Database"""
import os

import mysql.connector

from exceptions.database import DatabaseAlreadyExists
from exceptions.database import DatabaseDoesNotExist

mydb = mysql.connector.connect(
    host="localhost", user="root", password=os.getenv("MYSQL_PASS")
)

cursor = mydb.cursor()


def database_exists(name):
    databases = show_databases()
    return [dbname for dbname in databases if name in dbname]


def show_databases():
    databases = []
    cursor.execute(f"SHOW DATABASES")
    for database in cursor:
        databases.append(database)
    return databases


def create_database(name):
    if database_exists(name):
        raise DatabaseAlreadyExists(name)
    cursor.execute(f"CREATE DATABASE {name}")


def drop_databases(name):
    if not database_exists(name):
        raise DatabaseDoesNotExist(name)
    else:
        cursor.execute(f"DROP DATABASE {name}")
