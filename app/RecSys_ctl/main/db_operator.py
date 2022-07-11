import psycopg2
import os
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

CREATE_TABLE_SQL = {
    'user_info': f"CREATE TABLE public.user_info (usr varchar NULL, pwd varchar NULL);",
    'user_rating': f"CREATE TABLE public.user_rating (usr varchar NULL, item varchar NULL, rating integer NULL);",
    'item_info': f"CREATE TABLE public.item_info (item varchar NULL, descr varchar NULL);"
}


def dbconnect(fun):
    def inner(*args, **kwargs):
        conn = psycopg2.connect(database=os.getenv('PROJECT_DBNAME'),
                                user=os.getenv('DB_USER'),
                                password=os.getenv('DB_PASSWORD'),
                                host=os.getenv('DB_HOST'),
                                port=os.getenv('DB_PORT'))
        result = fun(*args, **kwargs, conn=conn)
        conn.close()
        return result
    return inner


@dbconnect
def is_exist_table(table, conn):
    df = pd.read_sql(f"select count(*) from pg_class where relname='{table}'", conn)
    if df['count'][0] == 0:
        return False
    else:
        return True


@dbconnect
def create_table(table, conn):
    if is_exist_table(table):
        return f'table named {table} already exist'
    else:
        try:
            cursor = conn.cursor()
            cursor.execute(CREATE_TABLE_SQL[table])
            conn.commit()
            return f'success to create table {table}'
        except Exception:
            return f'fail to create table {table}'

