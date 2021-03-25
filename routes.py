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
