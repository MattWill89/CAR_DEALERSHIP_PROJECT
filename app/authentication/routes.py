from forms import UserLoginForm, UserSignInForm
from models import User, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash, g, session
from flask_login import login_user, logout_user, LoginManager, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserSignInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User(email=email, password=password, first_name=first_name, last_name=last_name)
        db.session.add(user)
        db.session.commit()

        flash(f'Successfully created user account. Welcome To the Odyssey! {email}', 'User-created')
        return redirect(url_for('site.home'))
    return render_template('sign_up.html', form=form)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserLoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        logged_user = User.query.filter_by(email=email).first()

        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            flash('Successfully signed in! Welcome Back To The Odyssey!', 'auth-success')
            return redirect("/")
        else:
            flash('Invalid email or password. Please try again.', 'auth-failed')
    return render_template('sign_in.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out. Hope To See You Back On The Adventure!', 'auth-success')
    return redirect(url_for('site.home'))
