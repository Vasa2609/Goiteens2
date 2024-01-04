from sqlalchemy import Column, Integer, String
from .database import Base

db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unik=True)
    password = db.Column(db.String(100), unik=True)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
