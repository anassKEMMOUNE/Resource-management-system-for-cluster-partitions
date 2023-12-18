from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import login as lg
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for production
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

# Initialize Flask-Session
from flask_session import Session
Session(app)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        ssh_connection = lg.establish_ssh_connection(form.username.data,form.password.data)
        # For simplicity, let's check hardcoded credentials.
        if ssh_connection != None:
            flash('Login successful!', 'success')
            # You can store user session data here if needed
            session['username'] = form.username.data
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in (you can use a more sophisticated check here)
    if 'username' in session:
        return f'Hello, {session["username"]}! Welcome to the dashboard.'
    else:
        flash('You need to login first.', 'warning')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
