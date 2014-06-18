from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, FileField
from wtforms.validators import Required, Length, url
from wtforms.fields.html5 import URLField
from app.models import User


class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me')

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        if self.nickname.data != User.make_valid_nickname(self.nickname.data):
            self.nickname.errors.append(gettext('This nickname has invalid characters. Please use letters, numbers, dots and underscores only.'))
            return False
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True

class PostForm(Form):
    post = TextField('post', validators = [Required()])
    image = FileField('image', validators = [Required()])
    link1 = URLField(validators=[url()])
    link2 = URLField(validators=[url()])
    link3 = URLField(validators=[url()])
    link1_text = TextField('link1_text', validators = [Required()])
    link2_text = TextField('link2_text', validators = [Required()])
    link3_text = TextField('link3_text', validators = [Required()])


class SearchForm(Form):
    search = TextField('search', validators = [Required()])



    