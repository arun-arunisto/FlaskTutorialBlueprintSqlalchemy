from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Todo_Model
import datetime

todo_bp = Blueprint("todo_bp", __name__,
                    template_folder="templates",
                    static_folder="static",
                    static_url_path="/todo/static")



@todo_bp.route("/todo")
def index():
    todos = db.session.execute(db.select(Todo_Model)).scalars()
    return render_template("index.html", todos=todos)

@todo_bp.route("/todo_add", methods=["POST"])
def todo_add():
    if request.method == "POST":
        todo_desc = request.form["todo_desc"]
        todo_model = Todo_Model(todo_desc=todo_desc,date=datetime.datetime.now().replace(microsecond=0))
        db.session.add(todo_model)
        db.session.commit()
    return redirect(url_for("todo_bp.index"))

@todo_bp.route("/delete/<int:id>/", methods=["GET"])
def todo_delete(id):
    todo = db.get_or_404(Todo_Model, id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo_bp.index"))

