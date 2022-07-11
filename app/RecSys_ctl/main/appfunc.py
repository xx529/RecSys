from main import db_operator as db


def init_db_all():
    ls = [db.create_table('user_info'),
          db.create_table('user_rating'),
          db.create_table('item_info')]
    return {'state': ls}
