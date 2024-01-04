from sqlalchemy import Column, Integer, String
from .database import Base


db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

class article(Base):
    __tablename__ = "article"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    

    def __repr__(self):
        return f'<Article {self.id}>'