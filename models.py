"""Models for Adopt Project"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

def connect_db(app):
    """Connect db to Flask app"""
    db.app = app
    db.init_app(app)
    

class Pet(db.Model):
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer,
                   primary_key = True, 
                   autoincrement=True)
    
    name = db.Column(db.String(20),
                   nullable=False)
    
    species = db.Column(db.String(20),
                        nullable=False)
    
    photo_url = db.Column(db.String,
                        nullable=True)
    
    age = db.Column(db.Integer,
                    nullable=True)
    
    notes = db.Column(db.Text,
                      nullable=True)
    
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
    
    def image_url(self):
        """Return image for pet -- given or generic"""
        
        return self.photo_url or DEFAULT_IMG
    
    