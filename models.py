from jeopardy import db 
class Package(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  editor = db.Column(db.String(30), nullable=True)
  author = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
  tournament = db.Column(db.String, nullable=True)
  categories = db.relationship("Category", backref="package", lazy=True)

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  package_id = db.Column(db.Integer, db.ForeignKey("package.id"), nullable=False)
  questions = db.relationship("Question", backref="category", lazy=True)

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