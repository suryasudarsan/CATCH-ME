from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

LOCATIONS = [
    {"id": "chennai", "name": "Chennai", "area": "Chennai", "lat": 13.0827, "lon": 80.2707},
    {"id": "madurai", "name": "Madurai", "area": "Madurai", "lat": 9.9252, "lon": 78.1198},
    {"id": "trichy", "name": "Tiruchirappalli (Trichy)", "area": "Tiruchirappalli", "lat": 10.7905, "lon": 78.7047},
    {"id": "chengalpattu", "name": "Chengalpattu", "area": "Chengalpattu", "lat": 12.6819, "lon": 79.9888},
    {"id": "gojan", "name": "Gojan College", "area": "Edapalayam / Redhills, Chennai", "lat": 13.2125, "lon": 80.1468},
]

@app.route("/")
def home():
    return render_template("index.html", locations=LOCATIONS)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)