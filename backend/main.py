from flask import Flask, request, jsonify
from engine import Session, Stacja
from flask_cors import CORS
session = Session()

app = Flask(__name__)
CORS(app)
@app.route('/create_station', methods=["POST"])
def create_station():
    data = request.get_json()
    station = Stacja(name=data.name, adres=data.adres, price=data.price, actual_date=data.actual_date)
    session.add(station)
    session.commit()
    return jsonify({"message": "station added", "station": {
        "name": station.name,
        "adres": station.adres,
        "price": station.price,
        "actual_date": station.actual_date
    }}), 201
@app.route('/stations', methods=["GET"])
def stations():
    data = session.query(Stacja).all()
    station_list = []
    for station in data:
        station_list.append({"name": station.name, "adres": station.adres, "price": station.price, "actual_date": station.actual_date})
    return jsonify(station_list)
@app.route('/stations/<name>', methods=["GET"])
def get_station(name):
    data = session.query(Stacja).filter_by(name=name)
    
    return jsonify({"name": data.name, "adres": data.adres, "price": data.price, "actual_date": data.actual_date}), 200

@app.route('/update_station/<id>', methods=["PUT"])
def update_station(id):
    data = request.get_json()
    station = session.query(Stacja).filter_by(id=id).first()
    if not station:
        return jsonify({"message": "Station not found"}), 404
    if data.price:
        station.price = data['price']
    if data.actual_date:
        station.actual_date = data['actual_date']
    session.commit()
    return jsonify({"message": "station successfully updated"}), 200

@app.route('/delete_station/<id>', methods=["DELETE"])
def delete_station(id):
    station = session.query(Stacja).filter_by(id=id).first()
    if not station:
        return jsonify({"message": "station not found"}), 404
    session.delete(station)
    session.commit()
    return jsonify({"message": "Station successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)