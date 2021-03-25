from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import Package, User, Category, Question
app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)


  




@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/jeopardy")
def jeopardy():
  return ""

@app.route("/register", methods=['GET', 'POST'])
def register():
  print("Hello")
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))
  return render_template("register.html", form=form)

@app.route("/login", methods=['GET', 'POST']) 
def login():
  form = LoginForm()
  if form.validate_on_submit():
    return redirect(url_for('home'))
  return render_template("login.html", form=form)

if __name__ == "__main__":
  app.run(debug=True)