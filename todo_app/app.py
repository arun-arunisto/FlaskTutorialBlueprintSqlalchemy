from flask import Flask
from todo.views import todo_bp
from todo.models import db

app = Flask(__name__)
app.secret_key = "arunisto"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(todo_bp)


if __name__ == "__main__":
    app.run(debug=True)

