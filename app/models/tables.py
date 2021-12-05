from os import set_inheritable
from app import db

class Gate_Status(db.Model):
    __tablename__ = "gate_status"

    id = db.Column(db.Integer, primary_key=True)
    ic_open = db.Column(db.Integer)
    last_modified_date = db.Column(db.DateTime)

    def __init__(self, id, ic_open, last_modified_date):
        self.id = id
        self.ic_open = ic_open
        self.last_modified_date = last_modified_date

class Vacante_Status(db.Model):
    __tablename__ = "vacante_status"

    id = db.Column(db.Integer, primary_key=True)
    v1 = db.Column(db.Integer)
    v2 = db.Column(db.Integer)
    v3 = db.Column(db.Integer)
    last_modified_date = db.Column(db.DateTime)

    def __init__(self, id, v1, v2, v3, last_modified_date):
        self.id = id
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.last_modified_date = last_modified_date
