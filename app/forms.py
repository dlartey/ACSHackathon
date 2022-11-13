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
    age = SelectField('age', choices=['Under 18', '18-25', '26-36', '36-49','50+'])
    
    screentime_a = SelectField('screentime_a', choices=['Less than 3 hours', '3-5 hours', '6-15 hours', 'Over 16 hours'])
    influencer_a = SelectField('influencer_a', choices=['Yes - all the time', 'Yes - sometimes', 'No, never']) # have you compared yourself to another user on social media
    filters_a = SelectField('filters_a', choices=['Yes - all the time', 'Yes - occasionally', 'Never'])
    self_image_a = SelectField('self_image_a', choices=['Yes, I love how I look', 'Yes, but I am ocassionally self conscious', 'No, I hate it']) # like how i look
    messages_a = SelectField('messages_a', choices=['Yes', 'No']) # do you have a lot of unread messages 
    bedtime_a = SelectField('bedtime_a', choices=['Yes, all the time', 'Yes - sometimes', 'Never']) # use phone before bed often
    following_a = SelectField('following_a', choices=['Family/friends', 'Celebrities','Beauty influencers', 'Fitness influencers', 'Pets/Animals']) # who do you mostly follow online
    recommendation_a = SelectField('recommendation_a', choices=['Yes, significantly', 'Yes - occassionally', 'Never']) # does social media influence your product choices

    outside_b = SelectField('outside_b', choices=['Yes','No']) # gone outside
    eaten_b = SelectField('eaten_b', choices=['Yes - all the time', 'Yes - occasionally', 'No']) # have you eaten today 
    nonline_b = SelectField('nonline_b', choices=['Yes - all the time', 'Yes - occasionally', 'No']) # nonline recreational activity
    exercise_b = SelectField('exercise_b', choices=['Yes - all the time', 'Yes - occasionally', 'No']) # exercised per week 
    sleep_b = SelectField('sleep_b', choices=['Less than 3 hours', '3-6 hours', '7+ hours'])
    
    relationship_c = SelectField('relationship_b', choices=['Yes - all the time', 'Yes - occasionally', 'No']) # spoken to a friend or loved one recently
    confide_c = SelectField('confide_c', choices=['Yes - all the time', 'Yes - occasionally', 'No']) # have confidant
    judged_c = SelectField('judged_c', choices=['Yes - all the time', 'Yes - occasionally', 'Never']) # feel judged by those around you


    stress_d = SelectField('stress_d', choices=['Yes - all the time', 'Yes - occasionally', 'Never']) # get stressed easy?
    concentrate_d = SelectField('concentrate_d', choices=['Yes - all the time', 'Yes - occasionally', 'No']) # good at concentrating
    depress_d = SelectField('depress_d', choices=['Yes - all the time', 'Yes - occasionally', 'Never'])



    





    
