"""Adopt Project"""

from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    db.create_all()


#Make Homepage Listing Pets
@app.route("/")
def home():
    """Show list of pets, include: name, photo, available tag if available"""
    
    pets = Pet.query.all()
    
    return render_template("home.html", pets=pets)

#Create a Handler for the form
@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add a new pet to the database"""
    #print(request.form)
    form = AddPetForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        pet= Pet(name=name, 
                 species=species, 
                 photo_url=photo_url,
                 age=age,
                 notes=notes)
        
        db.session.add(pet)
        db.session.commit()
        
        flash(f"Added {name} the {species} to the database")
        return redirect("/")
    
    else:
        return render_template("add_new_pet.html", form=form)
    
@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet(id):
    
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.notes = form.notes.data
        db.session.commit()
        return redirect("/")
    
    else:
        return render_template("edit_pet.html", form=form, pet=pet)