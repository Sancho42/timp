from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:qwe@localhost/dbTiMP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1024), nullable=False)
    password = db.Column(db.String(1024), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class UsedCipher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inputText = db.Column(db.String(4096), nullable=False)
    inputKeys = db.Column(db.String(4096), nullable=False)
    outputText = db.Column(db.String(4096), nullable=False)
    encryptionMode = db.Column(db.String(64), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    users = db.relationship('User', backref=db.backref('ciphers', lazy=True))

    def __repr__(self):
        return '<UsedCipher %r>' % self.id