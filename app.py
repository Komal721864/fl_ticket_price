from flask import Flask,request, render_template
from function import ticket_price

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def predict():

    data = request.form

    airline = data['airline']
    flight_name = data['flight_name']
    source_city = data['source_city']
    departure_time = data['departure_time']
    stops = int(data['stops'])
    arrival_time = data['arrival_time']
    destination_city = data['destination_city']
    flight_class = int(data['flight_class'])
    duration = float(data['duration'])
    days_left = int(data['days_left'])


    price = ticket_price(airline, flight_name,source_city,departure_time,stops,arrival_time,destination_city,flight_class,duration,days_left)
    predicted_price = price.predict_price()
    print(predicted_price)

    return render_template('index.html', final_price= predicted_price)

    
if __name__ == "__main__":
    app.run(host= '0.0.0.0', port= 8080, debug=True)