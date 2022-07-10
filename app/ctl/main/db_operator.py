import psycopg2
import os
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


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
def check_exist_table(table, conn):
    df = pd.read_sql(f"select count(*) from pg_class where relname='{table}'", conn)
    if df['count'][0] == 0:
        return False
    else:
        return True


@dbconnect
def create_user_info(conn):
    if check_exist_table('user_info'):
        return '用户表已经存在'
    else:
        try:
            cursor = conn.cursor()
            sql = f"CREATE TABLE public.user_info (usr varchar NULL, pwd varchar NULL);"
            cursor.execute(sql)
            conn.commit()
            return '用户表创建成功'
        except Exception:
            return '用户表创建失败'


@dbconnect
def test(conn):
    return pd.read_sql('select * from public.user_info', conn).to_dict()
