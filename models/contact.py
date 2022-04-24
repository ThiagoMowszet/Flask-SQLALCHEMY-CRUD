from utils.db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(30))

    def __init__(self,fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone