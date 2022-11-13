from email import message
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import DateField
from wtforms import SubmitField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import ValidationError
from wtforms import SelectField
from wtforms import FloatField
from wtforms import DateTimeField
from wtforms import FileField
from wtforms.validators import InputRequired, EqualTo, Length, Email, Regexp, NumberRange
from flask import flash
from datetime import datetime, timedelta
import calendar

# sign up form


class RegisterForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Regexp(
        "^([^0-9]*)$", message="Name cannot contain digits")])
    industry = StringField('industry', validators=[
                           InputRequired(), Length(min=2, max=20)])
    country = SelectField('country', choices=[
                          'Select One', 'Nigeria', 'Nepal'])
    time_of_operation = SelectField('time_of_operation', choices=[])
    emissions = SelectField('time_of_oiperation', choices=[])
    fuel_consumption = StringField('industry', validators=[
        InputRequired(), Length(min=2, max=20)])
    work_outsourced = StringField('industry', validators=[
        InputRequired(), Length(min=2, max=20)])
    upload = FileField('upload')
