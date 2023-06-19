from flask_app import app

from flask import render_template,redirect,request,session,flash

from flask_app.models.user_model import User

# home route
@app.route('/users')
def home_route():

    all_users = User.get_all_users()

    print(all_users)

    return render_template('index.html', all_users = all_users)


# route for showing an individual user's data to the database
@app.route('/users/<int:user_id>')
def show(user_id):

    one_user = User.get_user({ 'user_id' : user_id })

    return render_template('show.html', one_user = one_user)


# route for create new user form
@app.route('/users/user_form')
def user_form():

    return render_template('user_form.html')


#post route for submitting a new user
@app.route('/users/submit_new_user', methods= ['POST'])
def submit():

    User.add_user(request.form)
    
    return redirect('/users')


# route for edditing a user
@app.route('/users/edit/<int:user_id>')
def edit(user_id):

    one_user = User.get_user({ 'user_id' : user_id })

    return render_template('edit.html', one_user = one_user)


# route for posting the user edit to the database
app.route('/users/edit_user', methods=['POST'])
def edit_user():

    User.edit_user({request.form})

    return redirect('/users')

# route for deleting a user entry in the database
@app.route('/users/delete/<int:user_id>')
def delete(user_id):
    
    User.delete_user(user_id)

    return redirect('/users')