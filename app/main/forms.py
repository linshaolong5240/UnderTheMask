# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired
from wtforms import TextAreaField,StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required
from flask_pagedown.fields import PageDownField

class FormLogin(FlaskForm):
    username    = StringField('Username', validators = [Required()])
    password    = PasswordField('Password', validators = [Required()])
    remember_me = BooleanField('Remember me')
    submit      = SubmitField('Submit')

class FormPost(FlaskForm):
    title    = StringField('Title', validators = [Required()])
    pagedown = PageDownField("What's on your mind?", validators = [Required()])
    submit   = SubmitField('Submit')

class FormFile(FlaskForm):
    file = FileField('file', validators=[FileRequired()])
    submit = SubmitField('Submit')
