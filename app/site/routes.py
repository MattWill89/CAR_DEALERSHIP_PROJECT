import base64
import email
from flask import Blueprint, redirect, render_template , url_for, flash
from flask_login import current_user, user_logged_in, LoginManager
from forms import AddCarForm, EditCarForm

from models import User, Car, db

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
    

# "/addcar" is an endpoint / route. Like any other endpoint, it
# can receive different types of requests:
    
    # GET  - Read
    # POST  - Create
    # PATCH / PUT - Update
    # DELETE - Destroy

# CRUD => Four Basic Ways That We Can Interact w/ Information in the DB

@site.route('/addcar', methods=['GET', 'POST'])
def add_car():
    
    
    form = AddCarForm() 

    if form.validate_on_submit():
        make = form.make.data
        model = form.model.data
        year = form.year.data
        color = form.color.data
        country = form.country.data

        car = Car(make=make, year=year, color=color, country=country)
        db.session.add(car)
        db.session.commit()

        flash(f'Successfully created car listing')
        return redirect(url_for('site.profile'))

    return render_template('add_car.html', form=form) 

@site.route('/edit_car/<serial_number>')
def edit_car(serial_number):

    form = EditCarForm()

    car = Car.query.filter_by(serial_number=serial_number).first()

    print(car)

    return render_template('edit_car.html', form=form)