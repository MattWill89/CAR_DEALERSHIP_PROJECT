import base64
import email
from flask import Blueprint, redirect, render_template 
from flask_login import current_user, user_logged_in, LoginManager
from forms import AddCarForm

from models import User, Car

login_manager = LoginManager()


site = Blueprint('site', __name__, template_folder='site_templates')



@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():

    user_now = []
    cars = Car.query.all()

    @login_manager.request_loader
    def load_user_from_request(request):

    # first, try to login using the api_key url arg
        api_key = request.args.get('api_key')
        if api_key:
            user = User.query.filter_by(api_key=api_key).first()
        if user:

            print(user)

            return user


    if current_user:

        return render_template('profile.html', cars=cars)
    
    else:

        return redirect("/signin")
    


@site.route('/addcar')
def add_car():
    form = AddCarForm() 

    return render_template('add_car.html', form=form) 
