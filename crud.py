"""Handles database functions"""

from model import db, User, Reservation, connect_to_db

#add_reservation
#create_user

def create_user(username, password):
    """Create and return a new user."""

    user = User(username=username, password=password)
    
    return user


def get_user_by_id(user_id):
    """Return a user by using their primary key (ID)."""

    return User.query.get(user_id)


def get_user_by_name(username):
    """Return a user by using their username."""

    return User.query.filter(User.username == username).first()

def get_all_users():
    """Return all users."""

    return User.query.all()

def create_note(user_id, title="", body="", favorite=True):
    """Create and return a new note."""

    note = Note(user_id=user_id, title=title, body=body)

    return note


def get_note_by_id(note_id):
    """Return a note by its primary key (ID)."""

    return Note.query.get(note_id)


def get_notes_by_user_id(user_id):
    """Return all the notes made by a user, ordered by note ID."""

    return Note.query.filter_by(user_id=user_id).order_by("note_id").all()


def get_all_notes():
    """Returns all notes."""

    return Note.query.all()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)