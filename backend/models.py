from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CaseStudy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(900), nullable=True)
