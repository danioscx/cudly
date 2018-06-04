from wtforms import Form, StringField, PasswordField, validators, FileField


class LoginForm(Form):

    username = StringField('username', validators=[
        validators.required(),
        validators.length(min=2, max=80)
    ])
    password = PasswordField('password', validators=[
        validators.required(),
        validators.length(min=4, max=100)
    ])


class RegisterForm(Form):

    name = StringField('name', validators=[
        validators.required(),
        validators.length(min=3, max=80)
    ])
    email = StringField('email', validators=[
        validators.required(),
        validators.length(min=4, max=80)
    ])
    password = PasswordField('password', validators=[
        validators.required(),
        validators.length(min=4, max=80)
    ])


class CommentForm(Form):

    content = StringField('content', validators=[
        validators.required(),
        validators.length(min=1, max=1000000)
    ])


class RepliesForm(Form):

    user = StringField('user', validators=[
        validators.required(),
        validators.length(min=1, max=80)
    ])
    content = StringField('content', validators=[
        validators.required(),
        validators.length(min=1, max=1000000)
    ])


class PostForm(Form):

    title = StringField('title', validators=[
        validators.required(),
        validators.length(min=1, max=80)
    ])
    content = StringField('content', validators=[
        validators.required(),
        validators.length(min=1, max=1000000)
    ])


class ImageForm(Form):

    files = FileField('files', validators=[
        validators.required()
    ])
