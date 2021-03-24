from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

# class Category(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(100), nullable=False)

# class Question(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   question = db.Column(db.String, nullable=False)
#   point = db.Column(db.Integer)
#   title_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

# class User(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.column(db.String(20))
  





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

@app.route("/login") 
def login():
  form = LoginForm()
  return render_template("login.html", form=form)

if __name__ == "__main__":
  app.run(debug=True)