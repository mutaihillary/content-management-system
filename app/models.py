from app import db


# class Base(db.Model):
#     __abstract__ = True
#     id = db.Column(db.Integer, primary_key=True)
#     date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
#     date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())


class User(db.Model):
    __tablename__ = 'auth_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128),  nullable=False,unique=True)
    password = db.Column(db.String(192),  nullable=False)
    # role = db.Column(db.SmallInteger, nullable=False)
    # status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self,name,email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name
"""""
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140))
    text = db.Column(db.String(250))

    def __repr__(self,title,text):
        self.title = title
        self.title = text
        return '<Post %r>' % (self.body)
    """""