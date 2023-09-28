from flask import Flask, render_template, request
import pickle
import templates

app = Flask(__name__)
model = pickle.load(open('airline_pick.sav', 'rb'))


@app.route('/')
def home():
    result = ''
    return render_template('Air_index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Baggage_handling = float(request.form['Baggage_handling'])
    Checkin_service = float(request.form['Checkin_service'])
    Inflight_entertainment = float(request.form['Inflight_entertainment'])
    On_board_service = float(request.form['On_board_service'])
    Flight_Distance = float(request.form['Flight_Distance'])
    Leg_room_service = float(request.form['Leg_room_service'])
    Type_of_Travel = float(request.form['Type_of_Travel'])
    Age = float(request.form['Age'])
    Ease_of_Online_booking = float(request.form['Ease_of_Online_booking'])
    Class = float(request.form['Class'])
    Online_boarding = float(request.form['Online_boarding'])


    result = model.predict([[Baggage_handling, Checkin_service, Inflight_entertainment, On_board_service,
                             Flight_Distance, Leg_room_service, Type_of_Travel, Age, Ease_of_Online_booking,
                             Class,Online_boarding]])[0]

    return render_template('Air_index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)