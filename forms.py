from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, URLField, BooleanField
from wtforms.validators import DataRequired, Optional, NumberRange, InputRequired, URL, Length

#class Name that inherits from FlaskForm
class AddPetForm(FlaskForm):
    """Form for adding snacks"""
    
    #name that stores the data and Field Type
    name = StringField("Pet Name",
                       validators=[InputRequired(message='Please add a name')])
    
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
                         validators=[DataRequired()])
    
    photo_url = URLField("Photo",
                         validators=[Optional(), URL()])
    
    age =  IntegerField("Age", 
                        validators=[Optional(), NumberRange(min=0, max=30)])
    
    notes = TextAreaField("Notes", 
                          validators=[Optional(), Length(min=10)])
    
class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    
    photo_url = URLField("Photo",
                         validators=[Optional(), URL()])
    
    notes = TextAreaField("Notes",
                          validators=[Optional(), Length(min=10)])
    
    available = BooleanField("Available?")