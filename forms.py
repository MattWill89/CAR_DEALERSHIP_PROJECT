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

# class User(db.Model, UserMixin):
#     id = db.Column(db.String, primary_key=True) #
#     first_name = db.Column(db.String(150), nullable=True, default='')
#     last_name = db.Column(db.String(150), nullable = True, default = '')
#     email = db.Column(db.String(150), nullable = False)
#     password = db.Column(db.String, nullable = True, default = '')
#     g_auth_verify = db.Column(db.Boolean, default = False)
#     token = db.Column(db.String, default = '', unique = True )
#     date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)