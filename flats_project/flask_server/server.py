from flask import Flask, render_template
from db.models import Flat, session_scope

app = Flask(__name__)

@app.route('/')
def hello_world():
    with session_scope() as session:
        flats = Flat.load_all_flats(session)
        return render_template('flats.html', flats=flats)
