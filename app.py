from flask import Flask

app = Flask(__name__) 

@app.route("/")
def welcome():
    return(
        f"<h3>Available Routes:</h3>"
        f"/api/v1.0/lighting_conditions<br>"
        f"/api/v1.0/weather_conditions<br>"
        f"/api/v1.0/accident_type<br>"
        f"/api/v1.0/population<br>"
        f"/api/v1.0/CRSS_data<br>"
        )


if __name__ == '__main__':
    app.run()
