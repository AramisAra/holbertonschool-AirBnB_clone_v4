#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
<<<<<<< HEAD
import uuid
from flask import Flask, render_template
=======
from flask import Flask, render_template
import uuid
>>>>>>> origin/master
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


<<<<<<< HEAD
@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []
    cache_id = uuid.uuid4()
=======
<<<<<<< HEAD
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
=======
@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    print(storage)
    states = storage.all(State)
    print(states)
>>>>>>> 9be1e74082eb8f63a82e93f3a8b86db4b63eeed0
    states = sorted(states, key=lambda k: k.name)
    st_ct = []
>>>>>>> origin/master

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
<<<<<<< HEAD
                           cache_id=cache_id)
=======
<<<<<<< HEAD
                           cache_id=str(uuid.uuid4()))
=======
                           cache_id=uuid.uuid4())
>>>>>>> 9be1e74082eb8f63a82e93f3a8b86db4b63eeed0
>>>>>>> origin/master


if __name__ == "__main__":
    """ Main Function """
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
    
=======
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> 9be1e74082eb8f63a82e93f3a8b86db4b63eeed0
>>>>>>> origin/master
