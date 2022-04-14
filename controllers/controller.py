from flask import render_template,request
from app import app
from models.event import Event
from models.calendar import *

@app.route('/')
def home():
    return "Bananas"

@app.route('/getevents')
def index():
    return render_template('index.html', title='Home', all_events=all_events)

@app.route('/addevents', methods=['POST'])
def add_event():
    print(request.form)
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_room = request.form["room"]
    event_description = request.form["description"]
    event_recurring = request.form["recurring"]
    if event_recurring == "Y":
        event_recurring = True
    elif event_recurring == "N":
        event_recurring = False


    new_event = Event(event_date, event_name, event_room, event_description, event_recurring)
    add_new_event(new_event)
    # print(task_title)
    # print(task_description)
    return render_template('index.html',title='Home',all_events=all_events)