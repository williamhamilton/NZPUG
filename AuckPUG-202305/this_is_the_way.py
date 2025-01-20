"""
I really should document this script!
"""
# ---------------------------------------------------------------------------------------------------------------------
__author__ = "William Hamilton"
__python__ = ""
__created__ = "27/04/23"
__copyright__ = "Copyright © 2023~"
__license__ = ""
__ToDo__ = """
- make more betterer
"""
# ---------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
import sqlite3
import pyodbc
import enum
import configparser
import codecs

# Setup configuration
config = configparser.ConfigParser()
config.read_file(codecs.open('config.ini', "r", "utf8"))

SITE_VERSION = config['environment']['system']
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


class Database(enum.Enum):
    OLD = "OldConnection"
    TEST = "TestConnection"
    NEW = "NewConnection"

class DatabaseConnection(ABC):

    @abstractmethod
    def connect(self):
        pass

    @classmethod
    def get_connection(cls, db_type: Database):
        db_map = {
            Database.OLD: OldConnection,
            Database.NEW: NewConnection,
            Database.TEST: TestConnection
        }
        connection_class = db_map.get(db_type)
        if connection_class is None:
            raise ValueError(f"Unsupported database type: {db_type}")
        return connection_class()

class OldConnection(DatabaseConnection):

    def connect(self):
        conn = sqlite3.connect('chinook.db')
        return conn

class NewConnection(DatabaseConnection):

    def connect(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=your_server_name;'
                              'Database=your_database_name;'
                              'Trusted_Connection=yes;')
        return conn

class TestConnection(DatabaseConnection):

    def connect(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=your_server_name;'
                              'Database=your_database_name;'
                              'uid=your_username;'
                              'pwd=your_password;')
        return conn



if __name__ == "__main__":
    print('\nStarting Processing')

    db_type = Database.OLD
    connection = DatabaseConnection.get_connection(db_type)
    conn = connection.connect()

    # Get the data
    cursor = conn.cursor()
    cursor.execute(get_albums)
    result = cursor.fetchall()
    print(result)

    cursor.execute(country_most_invoices)
    result = cursor.fetchall()
    print(result)
    print('\nTerminating')




"""
In the above code, the DatabaseConnection class is an abstract base class that defines the interface for connecting 
to a database. The OldConnection, NewConnection, and TestConnection classes are concrete subclasses that implement the 
connect method of the DatabaseConnection class.

Each of the concrete subclasses is a valid substitute for the DatabaseConnection class, since they implement the connect 
method as required by the interface. For example, if you have code that expects an object of type DatabaseConnection, 
you could replace it with an object of type OldConnection, NewConnection, or TestConnection without affecting the 
correctness of the program.

Furthermore, since the NewConnection and TestConnection classes inherit from the DatabaseConnection class and do not 
override any of its methods, they meet the "behavioral subtyping" requirement of the LSP. Behavioral subtyping means 
that a subclass should not weaken any preconditions of its superclass's methods or strengthen any postconditions of its 
superclass's methods. In this case, the NewConnection and TestConnection classes do not modify the behavior of the 
connect method defined in the DatabaseConnection class, so they meet the behavioral subtyping requirement.

In summary, the original code follows the Liskov Substitution Principle since each of the concrete subclasses is a 
valid substitute for the DatabaseConnection class and the NewConnection and TestConnection classes meet the behavioral 
subtyping requirement.
"""