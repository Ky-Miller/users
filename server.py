from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key="secret key"

from models.user import User

@app.route('/')
def home_route():

    all_users = User.get_all_users()

    print(all_users)

    return render_template('index.html', all_users = all_users)

@app.route('/user_form')
def user_form():

    return render_template('user_form.html')

@app.route('/submit_new_user', methods= ['POST'])
def submit():

    User.add_user(request.form)
    
    return redirect('/')

app.run(debug=True, host="localhost", port=5000)