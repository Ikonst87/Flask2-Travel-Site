from flask import Flask, render_template
import data

tours = data.tours


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html', departures=data.departures, title=data.title, tours=tours)


@app.route("/departures/<departure>/")
def render_departure(departure):
    try:
        dep_city = data.departures[departure].replace("Из", "из")
    except KeyError:
        return render_template('error.html', departures=data.departures, title=data.title, type='departure',
                               id=departure), 404
    tours_dep = {}
    for tour_id, tour_data in tours.items():
        if tour_data["departure"] == departure:
            tours_dep[tour_id] = tour_data

    return render_template('departure.html', departures=data.departures, title=data.title, tours=tours_dep,
                           dep_city=dep_city)


@app.route("/tours/<id>/")
def render_tours(id):
    tour_id = int(id)
    try:
        tour = tours[tour_id]
        dep_city = data.departures[tour["departure"]].replace("Из", "из")
    except KeyError:
        return render_template('error.html', departures=data.departures, title=data.title, type='tour', id=id), 404
    return render_template('tour.html', departures=data.departures, title=data.title, tour=tour, dep_city=dep_city)


if __name__ == '__main__':
    app.run(debug=True)
