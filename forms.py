from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])

class UserSignInForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    # submit_button = SubmitField()

class AddCarForm(FlaskForm):
    make = StringField('Make', validators = [DataRequired()])
    model = StringField('Model', validators = [DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    country = StringField('Country of Origin', validators = [DataRequired()])

class EditCarForm(FlaskForm):
    make = StringField('Make', validators = [DataRequired()])
    model = StringField('Model', validators = [DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    country = StringField('Country of Origin', validators = [DataRequired()])