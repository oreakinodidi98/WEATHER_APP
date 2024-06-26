from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)
# makes app a flask application

#define routes in flask 
@app.route('/')
@app.route('/index')
# this is the home page route

# following the routes we define a function that will be executed when the route is accessed
def index():
    return render_template("index.html")

# handle a rooute for weather
@app.route('/weather')
def get_weather():
    # get city from query string
    city = request.args.get('city')
    
    # check from an empty string or strings with only spaces
    if not bool(city.strip()):
        #default value for city of London if no city is provided or city is only spaces
        city = "London"
    # get weather data
    weather_data = get_current_weather(city)
    # City is not found by API
    if not weather_data['cod'] == 200:
        return render_template("city_not_found.html")
    # render weather.html template and pass weather data
    return render_template("weather.html",
                           title=weather_data["name"],
                           status=weather_data["weather"][0]["description"].capitalize(),
                           temp=f"{weather_data['main']['temp']:.1f}", 
                           feels_like=f"{weather_data['main']['feels_like']:.1f}")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)