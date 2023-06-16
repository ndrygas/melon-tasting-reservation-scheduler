"""Models for storing reservations in database"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""user, their reservations"""

class User(db.Model):
    """A user account"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)

    reservation = db.relationship("Reservation", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'


class Reservation(db.Model):
    """A reservation for melons."""

    __tablename__ = 'reservations'

    reservation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date = db.Column(db.String(50), unique=True, nullable=False)

    user = db.relationship("User", back_populates="reservation")

    def __repr__(self):
        return f'<Reservation reservation_id={self.reservation_id} date={self.date}>'
    

def connect_to_db(app):
    """Connect the database to Flask app"""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///reservations"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db")


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)