from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import login as lg
import commands as cm

app = Flask(__name__,static_url_path='/static')
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
    if "username" in session :
        del session["username"]
    form = LoginForm()

    if form.validate_on_submit():
        global ssh_connection
        ssh_connection = lg.establish_ssh_connection(form.username.data,form.password.data)
        # For simplicity, let's check hardcoded credentials.
        if ssh_connection != None:
            # You can store user session data here if needed
            session['username'] = form.username.data
            session['password'] = form.password.data
            
            return redirect(url_for('partitions'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)


@app.route('/partitions')
def partitions():
    global ssh_connection


    if 'username' in session:
        try : 
            ssh_connection
        except :
            ssh_connection = lg.establish_ssh_connection(session['username'],session['password'])
        
        
        result0,result1,result2,result3,result4 = cm.all_commands(ssh_connection)
        path0 = "url"
        
        return render_template('partitions.html', result0 = result0 ,result1 = result1, result2 = result2, result3 = result3, result4 = result4 ,path0 = path0)
    else:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))


@app.route('/nodes')
def nodes():
    if 'username' in session:
        try : 
            ssh_connection
        except :
            ssh_connection = lg.establish_ssh_connection(session['username'],session['password'])
        
        
        return render_template('nodes.html')
    else:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)