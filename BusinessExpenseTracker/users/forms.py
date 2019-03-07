# Form Based Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from BusinessExpenseTracker.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class NewExpense(FlaskForm):
    company_name = StringField('company_name', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()], format="%Y-%m-%d")
    total = IntegerField('Total',validators=[DataRequired()])
    myChoices = ["EUR (Euro)","BPB (Pound Sterling)","USD (United States, Dollar)" ]
    currency = SelectField('Currency_SelectField', choices = myChoices, validators = [DataRequired()])
    expense_category = ["Diesel", "Petrol","CAR PARKING","TOLLS","AIR FARES","TRAIN FARES",
    "OTHER TRAVEL","ACCOMODATION","SUBSISTENCE","STAFF ENTERTAINING",
    "CUSTOMER ENTERTAINING","STATIONARY","MISCELLANEOUS"]
    category=SelectField('Currency_SelectField', choices = expense_category, validators = [DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    receipt_picture = FileField('receipt Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])


    mobilenumber = IntegerField('mobilenumber', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')
