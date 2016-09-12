import datetime

from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash, check_password_hash

from hashlib import md5

from peewee import *
import models

DATABASE = SqliteDatabase("blog.db")

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True, default="")
    password = CharField(max_length=100, default="")
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)
    about_me = TextField()
    last_seen = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)


    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            with DATABASE.transaction():
                cls.create(
                    username=username,
                    email=email,
                    password=generate_password_hash(password),
                    is_admin=admin,
                    about_me='',
                    last_seen=datetime.datetime.now()
                )
        except IntegrityError:
            raise ValueError("User already exists")

    #TODO: Logic away
    def get_stream(self):
        return Post.select().where(
            (Post.user==self)
        )

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email.encode('utf-8')).hexdigest() + '?d=mm&s=' + str(size)

    def set_last_seen(self):
        self.last_seen = datetime.datetime.now()
        self.save()

    def change_password(self, password):
        self.password = generate_password_hash(password)
        self.save()



    #test version. replace later
    def update_email(self, email):
        self.email = email
        self.save()

    #test version
    def update_about_me(self, about_me):
        self.about_me = about_me
        self.save()

    # @staticmethod
    # def make_unique_nickname(nickname):
    #     if User.select().where(nickname==nickname).get() is None:
    #         return nickname
    #     version = 2
    #     while True:
    #         new_nickname = nickname + str(version)
    #         if User.select().where(nickname=new_nickname).get() is None:
    #             break
    #         version += 1
    #     return new_nickname




class Post(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(
                            rel_model=User,
                            related_name='posts'
                          )

    #Why does it crush everything?

    class Meta:
         database = DATABASE
         order_by = ('-timestamp',)

    @classmethod
    def create_post(cls, content, user):
        with DATABASE.transaction():
                cls.create(
                    content=content,
                    user=user
                )



class Hand(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    flop = TextField()
    turn = TextField()
    river = TextField()
    summary = TextField()
    user = ForeignKeyField(
        rel_model=User,
        related_name='hands'
    )

    class Meta:
         database = DATABASE
         order_by = ('-timestamp',)

    @classmethod
    def create_hand(cls,
                    content,
                    user,
                    flop,
                    turn,
                    river,
                    summary
                    ):
        with DATABASE.transaction():
                cls.create(
                    content=content,
                    user=user,
                    flop=flop,
                    turn=turn,
                    river=river,
                    summary=summary
                )

    def get_stream(self, user):
        return Hand.select().where(Hand.user == user)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post, Hand], safe=True)
    DATABASE.close()












