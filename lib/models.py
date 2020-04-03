from sqlalchemy import Column, String, Integer, Text, Date
from lib import Mode
from crypto import bcrypt
from datetime import datetime


def _get_date():
    return datetime.now()


class User(Mode):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    date_join = Column(Date)
    name = Column(String(50), nullable=False)
    profile_photo = Column(String(90), unique=True)
    light_photo = Column(String(90), unique=True)
    url_user = Column(String(100), unique=True, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)

    def __init__(self, date_join, name, url_user, email, password):
        self.date_join = date_join
        self.name = name
        self.url_user = url_user
        self.email = email
        self.password = bcrypt.generate_password_hash(password)


class Article(Mode):

    __tablename__ = 'article'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(1000), nullable=False)
    value = Column(String(5000000), nullable=False, unique=True)
    date = Column(Date, nullable=False)
    post_by = Column(String(60), nullable=False)
    link_post = Column(String(60), nullable=False)

    def __init__(self, title, value, date, post_by, link_post):
        self.title = title
        self.value = value
        self.date = date
        self.post_by = post_by
        self.link_post = link_post


class Comments(Mode):

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user = Column(String(80), nullable=False)
    value = Column(Text(1000000), unique=True)
    to_post = Column(String(90), nullable=False)
    date = Column(Date)

    def __init__(self, user, value, to_post, date):
        self.user = user
        self.value = value
        self.to_post = to_post
        self.date = date


class Reply(Mode):

    __tablename__ = 'replies'

    id = Column(Integer, primary_key=True)
    user = Column(String(80), unique=True)
    content = Column(String(1000000), unique=True)
    date = Column(Date)
    to_comment = Column(String(100), nullable=False)

    def __init__(self, user, connect, content, date):
        self.user = user
        self.connect = connect
        self.content = content
        self.date = date


class Image(Mode):

    __tablename__ = 'image_upload'

    id = Column(Integer, primary_key=True)
    link = Column(String(1000), nullable=False)
    img_by = Column(String(100), nullable=False)
    date = Column(Date)

    def __init__(self, link, img_by, date):
        self.link = link
        self.img_by = img_by
        self.date = date


class Tag(Mode):

    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    from_post = Column(String(60), nullable=False)
    tag_it = Column(String(1000))

    def __init__(self, from_post, tag_it):
        self.from_post = from_post
        self.tag_it = tag_it

    def __init__(self, from_post):
        self.from_post = from_post

