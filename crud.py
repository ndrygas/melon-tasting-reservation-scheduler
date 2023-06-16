"""Handles database functions"""

from model import db, User, Reservation, connect_to_db

def create_user(username):
    """Create and return a new user."""

    user = User(username=username)
    
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

def create_reservation(user_id, date):
    """Create and return a new reservation."""

    reservation = Reservation(user_id=user_id, date=date)

    return reservation


def get_reservation_by_id(reservation_id):
    """Return a reservation by its primary key (ID)."""

    return Reservation.query.get(reservation_id)


def get_reservations_by_user_id(user_id):
    """Return all the reservations made by a user, ordered by reservation ID."""

    return Reservation.query.filter_by(user_id=user_id).order_by("reservation_id").all()


def get_all_reservations():
    """Returns all reservations."""

    return Reservation.query.all()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)