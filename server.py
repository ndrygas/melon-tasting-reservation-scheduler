"""Server for web app handling login and reservations."""

from flask import Flask

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    print(session)
    if "username" not in session:
        return render_template('homepage.html')
    
    else:
        username = session["username"]
        user = crud.get_user_by_name(username)
        return redirect(f"/{user.username}")
    
    

@app.route("/create-account", methods=["POST"])
def create_account():
    """Create a new user account and redirect back to login page"""
    
    username = request.form.get('username')


    print(username)

    if username != "" and password != "":
        user = crud.get_user_by_name(username)
        if user:
            flash("That username already exists. Please use a different name.")
        else:    
            user = crud.create_user(username, password)
            db.session.add(user)
            db.session.commit()
            initial_note = crud.create_note(user_id=user.user_id)
            db.session.add(initial_note)
            db.session.commit()
            flash("Success! Please log in.")
    else: 
        flash("Please fill in the create account form.")
        
        
    return redirect("/")


@app.route('/login', methods=["POST"])
def log_in():
    """Log in a user and redirect to their notes."""

    username = request.form.get('username')
   
    user = crud.get_user_by_name(username)
    
    if user:
        session["username"] = user.username
        flash(f"Successfully logged into {user.username}'s account.")
        return redirect(f"/{user.username}")
    else:
        flash("Please enter valid credentials or create a new account.")
        return redirect("/")
    

@app.route('/logout', methods=["POST"])
def log_out():
    """Log out a user and redirect to log in screen."""

    del session["username"]

    return redirect("/")
    

@app.route('/<username>')
def user_home(username):
    """Display a user's homepage and all of their active notes."""
    
    if "username" not in session:
        flash(f"You must be logged in to view your reservations.")
        return redirect("/")
    
    else:
        username = session["username"]
        user = crud.get_user_by_name(username)
        reservations = crud.get_reservation_by_user_id(user.user_id)
        
        return render_template('note.html', user=user, reservations=reservations)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)