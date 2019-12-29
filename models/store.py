import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    item = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name, price):
        self.name = name

    def json(self):
        return { 'name': self.name, 'items': {item.json for item in self.items.all()} }

    @classmethod
    def find_by_name(self):
        return ItemModel.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
