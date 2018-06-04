import shutil

from flask import Blueprint, render_template, request, redirect, url_for, \
    flash, session, json, send_from_directory
from lib.classes import LoginForm, RegisterForm, PostForm, CommentForm
from werkzeug.utils import secure_filename
<<<<<<< HEAD
from lib.models import User, Image, Article, Comments, Tag
=======
from lib.models import User, Image, Article, Comments
>>>>>>> c505dc81b8da6db9bccd4cf9c53fe5fe83068551
from crypto import bcrypt, allow_file, path_folder
from lib import db_session, engine
from datetime import datetime

import os
import base64


def _get_date():
    return datetime.now()


views = Blueprint('views', __name__, template_folder='../views', static_folder='../assets')


@views.route("/")
def index():
    image = Image.query.all()
    article = Article.query.all()
    s = []
    for x in article:
        s.append(x.post_by)
    data = ' '.join(s)
    xx = data.encode()
    return render_template('index.html',
                           img=image,
                           art=article,
                           email=base64.b16encode(xx))


"""
Script bellow handle login register and log out

"""


@views.route("/login", methods=["GET", "POST"])
def login():
    if not session.get('email'):
        form = LoginForm(request.form)
        if request.method == "POST" and form.validate():
            user = User.query.filter_by(email=form.username.data).first()
            if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
                session['email'] = user.email
                session['uid'] = user.url_user
                session['name'] = user.name
                session['pro'] = user.profile_photo
                return redirect(url_for('views.dashboard', uid=user.url_user))
            else:
                flash('wrong email or password please try again!')
        return render_template('login.html', form=form)
    else:
        return redirect(url_for('views.dashboard', uid=session['uid']))


@views.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        b16 = form.email.data.encode()
        if user is not None:
            flash('the email is already used please use another email or login!')
            return redirect(url_for('views.register'))
        else:
            u_insert = User(
                _get_date(),
                form.name.data,
                base64.b16encode(b16),
                form.email.data,
                form.password.data
            )
            db_session.add(u_insert)
            db_session.commit()
            session['email'] = form.email.data
            session['name'] = form.name.data
            session['uid'] = base64.b16encode(b16)
            return redirect(url_for('views.step'))
    return render_template('register.html', form=form)


@views.route("/next/step/2", methods=["GET", "POST"])
def step():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('File cannot empty')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path_file = os.path.join(os.getcwd() + "/assets/media/user_upload", filename)
            if os.path.exists(path_file):
                file.save(
                    os.path.join(
                        os.getcwd() + "/assets/media/error", filename
                    )
                )
                shutil.copy(os.path.join(os.getcwd() + "/assets/media/error", filename),
                            os.getcwd() + "/assets/media/user_upload/" + str('1' + filename)
                            )
                data = "1" + str(filename)
                user = User.query.filter_by(email=session['email']).first()
                link = "/media/storage/" + str(data)
                user.profile_photo = link
                db_session.commit()
                image = Image(
                    link,
                    session['email'],
                    _get_date()
                )
                db_session.add(image)
                db_session.commit()
                session['pro'] = link
                return redirect(url_for('views.dashboard', uid=session['uid']))
            else:
                file.save(
                    os.path.join(
                        os.getcwd() + "/assets/media/user_upload", filename
                    )
                )
                user = User.query.filter_by(email=session['email']).first()
                link = "/media/storage/" + str(filename)
                user.profile_photo = link
                db_session.commit()
                image = Image(
                    link,
                    session['email'],
                    _get_date()
                )
                db_session.add(image)
                db_session.commit()
                session['pro'] = link
                return redirect(url_for('views.dashboard', uid=session['uid']))

    return render_template('next.html')
    

@views.route("/log_out")
def log_out():
    session.pop('email', None)
    session.pop('uid', None)
    session.pop('name', None)
    session.pop('pro', None)
    return redirect(url_for('views.index'))


@views.route("/user/<uid>", methods=["GET", "POST"])
def dashboard(uid):
    data = base64.b16decode(uid).decode()
    cursor = engine.connect()
    select = cursor.execute("SELECT * FROM user WHERE email='" + data + "'")
    tic = Article.query.filter_by(post_by=data).all()
    title, value, date, link = [], [], [], []
    for use in tic:
        title.append(use.title)
        value.append(use.value)
        date.append(use.date)
        link.append(use.link_post)
        pass
    profile, name, back = [], [], []
    for user in select:
        profile.append(user['profile_photo'])
        name.append(user['name'])
        back.append(user['light_photo'])

    return render_template('dashboard.html', profile=profile,
                           name=name, back=back, art=zip(title, value, date, link))


@views.route("/add_post", methods=["GET", "POST"])
def add_post():
    form = PostForm(request.form)
    if request.method == "POST" and form.validate():
        data = form.title.data[:20]
        link = data.replace(' ', '-')
        html = link + str(".html")
        article = Article(
            form.title.data,
            form.content.data,
            _get_date(),
            session['email'],
            html
        )
        db_session.add(article)
        db_session.commit()
<<<<<<< HEAD
        if not request.form['tag']:
            tag = Tag(
                html,
                request.form['tag']
            )
            db_session.add(tag)
            db_session.commit()
        else:
            pass
=======
>>>>>>> c505dc81b8da6db9bccd4cf9c53fe5fe83068551
        return redirect(url_for('views.index'))
    return "/x/231/ws/"


@views.route("/replies_comments")
def replies_comments():
    return


@views.route("/delete_post")
def delete_post():
    return


@views.route("/delete_comments")
def delete_comments():
    return


"""
On script bellow actually for javascript method like a XMLHttpRequest or ajax by jquery

"""


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in allow_file


@views.route("/uploader", methods=["GET", "POST"])
def uploader():
    if request.method == "POST":
        if 'file' not in request.files:
            return json.dumps({"error": "error1"})
        file = request.files['file']
        if file.filename == '':
            return json.dumps({"Error": "error"})
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path_file = os.path.join(os.getcwd() + "/assets/media/user_upload", filename)
            if os.path.exists(path_file):
                file.save(
                    os.path.join(
                        os.getcwd() + "/assets/media/error", filename
                    )
                )
                shutil.copy(os.path.join(os.getcwd() + "/assets/media/error", filename),
                            os.getcwd() + "/assets/media/user_upload/" + str('1' + filename)
                            )
                data = "1" + str(filename)
                user = User.query.filter_by(email=session['email']).first()
                link = "/media/storage/" + str(data)
                user.light_photo = link
                db_session.commit()
                image = Image(
                    link,
                    session['email'],
                    _get_date()
                )
                db_session.add(image)
                db_session.commit()
                return redirect(url_for('views.dashboard', uid=session['uid']))
            else:
                file.save(
                    os.path.join(
                        os.getcwd() + "/assets/media/user_upload", filename
                    )
                )
                user = User.query.filter_by(email=session['email']).first()
                link = "/media/storage/" + str(filename)
                user.light_photo = link
                db_session.commit()
                image = Image(
                    link,
                    session['email'],
                    _get_date()
                )
                db_session.add(image)
                db_session.commit()
                return redirect(url_for('views.dashboard', uid=session['uid']))

    return render_template("dashboard.html")


@views.route("/json_search", methods=["GET", "POST"])
def js_search():
    key = request.args['q']
    cursor = engine.connect()
    user = cursor.execute("SELECT * FROM article")
    data = [x for x in user if key in x]
    return json.dumps({"result": data})


@views.route('/media/storage/<image>', methods=["GET", "POST"])
def image_path(image):

    return send_from_directory(path_folder, image)


@views.route("/article/<link>", methods=["GET", "POST"])
def art(link):
    comment = Comments.query.filter_by(to_post=link).all()
    name, c_d, value = [], [], []
    for data in comment:
        name.append(data.user)
        c_d.append(data.date)
        value.append(data.value)
    article = Article.query.filter_by(link_post=link).first()
    user = []
    lis = []
    pr = []
    for x in name:
        use = User.query.filter_by(email=x).first()
        user.append(use.name)
        lis.append(use.url_user)
        pr.append(use.profile_photo)

    if request.method == "POST":
        form = CommentForm(request.form)
        if not session.get('email'):
            flash("You need to login to add the comments!")
            return redirect(url_for('views.login'))
        else:
            add_comments = Comments(
                session['email'],
                form.content.data,
                link,
                _get_date())
            db_session.add(add_comments)
            db_session.commit()
            return redirect(url_for('views.art', link=link))

    return render_template("art.html", title=article.title,
                           body=article.value, date=article.date,
                           link=article.link_post, comment_value=zip(lis, c_d, value, user, pr))


