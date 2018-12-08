import pandas as pd
import sqlite3
from sqlite3 import Error

Currency_exchange = pd.read_csv("new.csv")
Currency_exchange.columns =['month','av-USD-EUR','min-USD-EUR','max-USD-EUR','nb-days']

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
if __name__ == '__main__':
    create_connection("new.db")

Currency_exchange.to_sql(name = "currency", con = conn)

query = "SELECT * FROM currency;"

df = pd.read_sql_query(query,conn)

df