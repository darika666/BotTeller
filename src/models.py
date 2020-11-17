from config import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)



class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)


class Count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summa = db.Column(db.Integer, primary_key=True)
    category = db.Column(
        db.Integer, db.ForeignKey('category.id'), nullable=False)
    user = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)

db.create_all()
db.session.commit()

