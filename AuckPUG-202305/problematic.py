"""
I really should document this script!
"""
# ---------------------------------------------------------------------------------------------------------------------
__author__ = "William Hamilton"
__contributors__ = ""
__python__ = ""
__created__ = "27/04/23"
__copyright__ = "Copyright © 2023~"
__license__ = ""
__ToDo__ = """
- nothing to add just yet other than - make things better
"""
# ---------------------------------------------------------------------------------------------------------------------

import configparser
import codecs
import sqlite3
import urllib
import pyodbc

# Setup configuration
config = configparser.ConfigParser()
config.read_file(codecs.open('config.ini', "r", "utf8"))

site_version = config['environment']['system']
DB_SERVER_NEW = config['environment']['db_server_new']
DB_SERVER_TEST = config['environment']['db_server_test']
DB_SERVER_OLD = config['environment']['db_server_old']
DB_NAME = config['environment']['db_name']
# Stored DB queries
# https://www.sqlitetutorial.net/sqlite-sample-database
get_albums = config['queries']['get_albums']
get_artists = config['queries']['get_artists']
country_most_invoices = config['queries']['country_most_invoices']
best_customer = config['queries']['best_customer']

print(f'\nUsing {site_version} database connection\n')


if site_version == 'OLD':
    con = sqlite3.connect("chinook.db")
    
elif site_version == 'NEW':
    params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};"f"SERVER={DB_SERVER_TEST};"f"DATABASE={DB_NAME};"f"Trusted_Connection=yes;")
    con = f"mssql+pyodbc:///?odbc_connect={params}"

elif site_version == 'TEST':
    params = urllib.parse.quote_plus(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"f"SERVER={DB_SERVER_TEST};"f"DATABASE={DB_NAME};"f"UID={username};"f"PWD={password};")
    con = f"mssql+pyodbc:///?odbc_connect={params}"

else:
    print('No database connection')




cursor = con.cursor()
cursor.execute(get_albums)
rows = cursor.fetchall()
print(rows)

cursor.execute(country_most_invoices)
rows = cursor.fetchall()
print(rows)

def artists_as_list():
    """
        Returns a list of artists from database (DB configurable in the .ini file).
        Returns:
            list
        """
    query = get_artists
    print(query)

    # query database
    # convert return into python list
                # or even a generator, if later code runs row-wise




if __name__ == "__main__":
    print('\nStarting')

    print('\nTerminating')
