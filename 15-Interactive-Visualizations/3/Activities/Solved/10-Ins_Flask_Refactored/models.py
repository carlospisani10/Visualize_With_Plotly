from app import db

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
