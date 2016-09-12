from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError, Email, EqualTo
from models import blog

def name_exists(form, field):
    if blog.User.select().where(blog.User.username == field.data).exists():
        raise ValidationError('User with that name already exists')


def email_exists(form, field):
    if blog.User.select().where(blog.User.email == field.data).exists():
        raise ValidationError('User with that email already exists')

class LoginForm(Form):
    #default
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


    #open ID
    #open_id = StringField('OpenId', validators=[DataRequired()])

class EditForm(Form):
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=500)])


class RegisterForm(Form):
    username = StringField(
        'username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username: one word, letters, numbers and underscore")
            ),
            name_exists
        ])

    email = StringField(
        'email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ]
    )

    password = PasswordField(
        'password',
        validators=[
            DataRequired(),
            Length(min=8),
            EqualTo('password2', message='No match')
        ]
    )

    password2 = PasswordField(
        'confirm',
        validators=[DataRequired()]
    )

class PostForm(Form):
    content = TextAreaField(
        'Post',
        validators=[DataRequired()]
    )

class PostHandForm(Form):
    content = TextAreaField(
        'Post the hand',
        validators=[DataRequired()]
    )


    flop = TextAreaField(
        'Flop'
    )

    turn = TextAreaField(
        'Turn'
    )

    river = TextAreaField(
        'River'
    )

    summary = TextAreaField(
        'Summary'
    )

class BuffForm(Form):
    cost_1 = StringField()
    cost_2 = StringField()
    cost_3 = StringField()
