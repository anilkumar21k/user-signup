from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def display_signup_form():
    return render_template('user-signup.html')

@app.route("/signup", methods=['POST'])
def signup_validation():
    uname = request.form['username']
    pwd = request.form['password']
    vpwd = request.form['verify password']
    em = request.form['email']
    uname_error =''
    pwd_error =''
    vpwd_error =''
    em_error = ''
    

    if uname=='':
        uname_error = 'Please enter username'
    elif (len(uname)>20 or len(uname)<3):
        uname_error = 'Please enter a valid username'
    elif (uname.count(' ')>=1):
        uname_error = 'Username cannot have space'
    
    if pwd=='':
        pwd_error = 'Please enter your password'
    elif (len(pwd)>20 or len(pwd)<3):
        pwd_error = 'Please enter a valid password'
    elif (pwd.count(' ') >=1):
        pwd_error = 'Password cannot have space' 

    if vpwd != pwd:
        vpwd_error = "Your passwords do not match"

    if em =='':
        em=''
    elif ((em.count('@')==0) or (em.count('.')==0)):
        em_error = 'Please enter a valid Email ID'
    elif (len(em)>20 or len(em)<3):
        em_error = 'Your Email ID is too long'
    
    if not uname_error and not pwd_error and not vpwd_error and not em_error:
        #user_name = uname
        #return redirect('/valid-signup?user_name={0}'.format(user_name))
        return render_template('welcome.html', uname=uname)
    else: 
        return render_template('user-signup.html', uname=uname, uname_error=uname_error,
        pwd=pwd, pwd_error=pwd_error, vpwd=vpwd, vpwd_error = vpwd_error, em=em, em_error=em_error)

#@app.route('/valid-signup')
#def valid_signup():
#    user_name = request.args.get('user_name')
 #   return '<h1> Welcome {0}</h1>'.format('user_name')
app.run()