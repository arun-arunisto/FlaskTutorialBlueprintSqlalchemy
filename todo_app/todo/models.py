from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo_Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_desc = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)


