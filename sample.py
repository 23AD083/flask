from flask import Flask, redirect ,render_template, request, url_for 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class todo(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String(100))
  complete=db.Column(db.Boolean)



@app.route("/")
def index():
  #show all todos
  todo_list=todo.query.all()
  print(todo_list)
  return render_template('base.html',todo_list=todo_list)

with app.app_context():
  db.create_all()
  db.create_all()
@app.route("/add",methods=["POST"])
@app.route("/add",methods=["POST"])
def add():
  new_todo=todo(title="Todo 1",complete=False)
  with app.app_context():
    db.session.add(new_todo)
    db.session.commit()
  return redirect(url_for('index'))

@app.route("/update/<int:todo_id>")
def update(todo_id):
  todo=todo.query.filter_by(id=todo_id).first()
  todo.complete=True
  db.session.commit()
  return redirect(url_for('index'))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
  # title=request.form.get("title") 
  new_todo=todo.query.filter_by(id=todo_id).first()
  # new_todo.title=title
  db.session.delete(new_todo)
  db.session.commit()
  return redirect(url_for('index'))
if __name__=="__main__":
  app.run(debug=True)


