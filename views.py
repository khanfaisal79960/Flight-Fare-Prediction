from flask import Flask, render_template, url_for, request, redirect
import joblib

model = joblib.load('./Model/flight_fare_predictor.joblib')

Days = ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']

Airlines = ['Air India', 'AirAsia', 'AkasaAir', 'AllianceAir', 'GO FIRST',
       'Indigo', 'SpiceJet', 'StarAir', 'Vistara']

Classes = ['Business', 'Economy', 'First', 'Premium Economy']

Cities = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad',
       'Kolkata', 'Mumbai']

Departures = ['12 PM - 6 PM', '6 AM - 12 PM', 'After 6 PM', 'Before 6 AM']

Stops = ['1-stop', '2+-stop', 'non-stop']

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       day = int(request.form['destination'])
       airline = int(request.form['airline'])
       classe = int(request.form['class'])
       source = int(request.form['source'])
       departure = int(request.form['departure'])
       stops = int(request.form['stops'])
       arrival = int(request.form['arrival'])
       destination = int(request.form['destination'])
       duration = float(request.form['duration'])
       days = int(request.form['days'])
       
       x_test = [[day, airline, classe, source, departure, stops, arrival,destination, duration, days]]
       prediction = model.predict(x_test)
       label = f'{prediction[0]: .2f}'

       return render_template('index.html', label=label)

    return render_template('index.html', days=Days, airlines=Airlines, classes=Classes, cities=Cities, departures=Departures, stops=Stops)