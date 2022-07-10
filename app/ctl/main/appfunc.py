import db_operator as db


def init_db_all():
    ls = [db.create_user_info()]
    return {'state': ls}