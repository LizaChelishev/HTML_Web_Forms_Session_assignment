from Users import Users
from werkzeug.security import generate_password_hash


class DbRepo:
    def __init__(self, local_session):
        self.local_session = local_session

    def get_user_by_id(self, id_to_get):
        return self.local_session.query(Users).get(id_to_get).all()

    def get_all_users(self):
        return self.local_session.query(Users).all()

    def post_user(self, user):
        self.local_session.add(user)
        self.local_session.commit()

    def update_by_column_value(self, table_class, column_name, value, data):
        self.local_session.query(table_class).filter(column_name == value).update(data)
        self.local_session.commit()

    def get_user_by_username(self, value):
        return self.local_session.query(Users).filter(Users.username == value).all()

    def get_user_by_email(self, value):
        return self.local_session.query(Users).filter(Users.email == value).all()

    def add_all(self, rows_list):
        self.local_session.add_all(rows_list)
        self.local_session.commit()

    def delete_user_by_id(self, id_column_name, id_to_remove):
        self.local_session.query(Users).filter(id_column_name == id_to_remove).delete(synchronize_session=False)
        self.local_session.commit()

    def put_by_id(self, id_column_name, id_to_update, data):
        exist_object = self.local_session.query(Users).filter(id_column_name == id_to_update)
        if not exist_object:
            self.local_session.add(exist_object)
        exist_object.update(data)
        self.local_session.commit()

    def patch_by_id(self, id_column_name, id_to_update, data):
        exist_object = self.local_session.query(Users).filter(id_column_name == id_to_update)
        if not exist_object:
            return
        exist_object.update(data)
        self.local_session.commit()

    def drop_all_tables(self):
        self.local_session.execute('drop TABLE users CASCADE')
        self.local_session.commit()

    def reset_db(self):
        self.add_all([Users(username='Eran', email='Eran@gmail.com', password=generate_password_hash('0000')),
                      Users(username='Yossi', email='Yos@gmail.com', password=generate_password_hash('0001')),
                      Users(username='Shimon', email='Shimonkush@gmail.com', password=generate_password_hash('0002')),
                      Users(username='Baruch', email='Baruch.g@gmail.com', password=generate_password_hash('0003')),
                      Users(username='Eden', email='queeneden@gmail.com', password=generate_password_hash('0004'))])

