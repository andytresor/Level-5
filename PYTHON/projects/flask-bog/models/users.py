from config import db
from sqlalchemy.sql import func # type: ignore

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now())