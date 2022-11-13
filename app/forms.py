from email import message
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import DecimalField
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
    name = StringField('name', validators=[InputRequired(), Regexp("^([^0-9]*)$", message="Name cannot contain digits")])
    industry = SelectField('industry', choices=['Select one','Agriculture', 'Economics & Finance', 'Education', 'Entertainment', 'Healthcare', 'Marketing','Technology'])
    country = SelectField('country', choices=['Select one', 'Central African Republic', 'Haiti','Myanmar','Nigeria', 'Nepal', 'Senegal','Somalia', 'Tuvalu'])
    time_of_operation = SelectField('time_of_operation', choices=['Select one', 'Less than 12 months', '1-3 years', '4-9 years', 'Over ten years'])
    gross_income = FloatField('gross_income', validators=[InputRequired()])
    net_profit = FloatField('net_profit', validators=[InputRequired()])
    elec_emissions = FloatField('elec_emissions', validators=[InputRequired()])
    gas_emissions = FloatField('gas_emissions', validators=[InputRequired()])
    co2_emissions = FloatField('gas_emissions', validators=[InputRequired()])
    fuel_consumption = FloatField('fuel_consumption', validators=[InputRequired(), Length(min=2, max=20)])
    energy_consumption = FloatField('energy_consumption', validators=[InputRequired(), Length(min=2, max=20)])
    work_outsourced = SelectField('work_outsourced', choices=['Select one','Yes', 'No'])
    work_outsourced_dist = SelectField('work_outsourced_dist', choices=['Select one', 'N/A', 'Within my country of operation', 'Within my continent of operation', 'Out of the continent'])
    upload = FileField('upload')
