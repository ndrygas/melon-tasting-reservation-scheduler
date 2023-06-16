"""Script to seed database with empty reservation slots"""

"""Script to seed database."""

import os
import json
from datetime import datetime

import crud
import model
import server

#Reset database, connect back to it, and create all tables within it

os.system("dropdb reservations")
os.system("createdb reservations")

model.connect_to_db(server.app)
model.db.create_all()