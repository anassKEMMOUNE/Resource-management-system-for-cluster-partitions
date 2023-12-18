from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import login as lg
import scontrol as sc
import sinfo as si
import squeue as sq
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
        global ssh_connection
        ssh_connection = lg.establish_ssh_connection(form.username.data,form.password.data)
        # For simplicity, let's check hardcoded credentials.
        if ssh_connection != None:
            flash('Login successful!', 'success')
            # You can store user session data here if needed
            session['username'] = form.username.data
            session['password'] = form.password.data
            
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)


@app.route('/index')
def index():
    global ssh_connection

        # Check if the user is logged in (you can use a more sophisticated check here)
    if 'username' in session:
        try : 
            ssh_connection
        except NameError:
            ssh_connection = lg.establish_ssh_connection(session['username'],session['password'])
        # return f'Hello, {session["username"]}! Welcome to the dashboard.'
        stdin, stdout, stderr = ssh_connection.exec_command("scontrol show partitions")
        result = sc.parse_scontrol_partitions(stdout.read().decode("utf-8"))
        

        stdin, stdout, stderr = ssh_connection.exec_command("sinfo")
        result1 = si.parse_sinfo_partitions(stdout.read().decode("utf-8"))
        

        stdin, stdout, stderr = ssh_connection.exec_command("scontrol show nodes")
        result2 = sc.parse_scontrol_nodes(stdout.read().decode("utf-8"))
        
        
        stdin, stdout, stderr = ssh_connection.exec_command("squeue")
        result3 = sq.parse_squeue_jobs(stdout.read().decode("utf-8"))
            
        
        return render_template('index.html', result = result ,result1 = result1, result2 = result2, result3 = result3)
    else:
        flash('You need to login first.', 'warning')
        return redirect(url_for('login'))
    

if __name__ == '__main__':
    app.run(debug=True)