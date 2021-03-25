from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

class Package(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  editor = db.Column(db.String(30))
  author = db.Column(db.String(30), db.ForeignKey("user.id"), nullable=False)
  tournament = db.Column(db.String)

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  package_id = db.Column(db.Integer, db.ForeignKey("package.id"), nullable=False)
  questions = db.Column("Question")

class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  question = db.Column(db.String, nullable=False)
  point = db.Column(db.Integer)
  title_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(25), nullable=False)
  image = db.Column(db.String(20), nullable=False, default='default.jpg')
  





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
    print("sdjds")
        # flash(f'Account created for {form.username.data}!', 'success')
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