import psycopg2
import os
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

CREATE_TABLE_SQL = {
    'user_info': 'CREATE TABLE public.user_info (uname varchar NULL, pwd varchar NULL);',
    'item_info': 'CREATE TABLE public.item_info (item varchar NULL, descr varchar NULL);',
    'user_rating': 'CREATE TABLE public.user_rating'
                   ' (uname varchar NULL, item varchar NULL, rating integer NULL);',
    'hot_list': 'CREATE TABLE public.hot_list (item varchar NULL);',
    'rec_list': 'CREATE TABLE public.rec_list (uname varchar NULL, item varchar NULL)'
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


@dbconnect
def get_user_info(uname, pwd, conn):
    df_result = pd.read_sql(f"select * from user_info where uname='{uname}' and pwd='{pwd}'", conn)
    return df_result.to_dict()


@dbconnect
def get_user_history(uname, conn):
    df_result = pd.read_sql(f"select * from user_rating where uname='{uname}'", conn)
    return df_result.to_dict()


