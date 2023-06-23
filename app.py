from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# from app import db, app
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

# Set up application context
# with app.app_context():
    # Perform operations that require the application context
    # db.create_all()
# app.app_context()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(400), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
    # return 'This is my index page'

@app.route('/show')
def about():
    # return render_template('about.html')
    allTodo = Todo.query.all()
    print(allTodo)
    # return 'This is the about page'

@app.route('/update')
def update():
    # return render_template('about.html')
    allTodo = Todo.query.all()
    print(allTodo)
    # return 'This is the about page'

@app.route('/delete/<int:sno>')
def delete(sno):
    # return render_template('about.html')
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=False, port=1000)