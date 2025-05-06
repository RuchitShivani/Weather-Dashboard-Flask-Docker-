from flask import Flask, render_template, request
import requests
import json

API_KEY = 'b9e7ccafb0d650fa63fff45b1d537e77'  # Your OpenWeatherMap API key
CITIES = ['Chennai', 'New York', 'Los Angeles', 'London', 'Tokyo']  # List of cities to track
URL_TEMPLATE = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

app = Flask(__name__)

def fetch_weather(city):
    URL = URL_TEMPLATE.format(city=city, api_key=API_KEY)
    response = requests.get(URL)
    return response.json()

@app.route('/')
def home():
    city = request.args.get('city', 'Chennai')  # Default to Chennai if no city is passed in URL
    data = fetch_weather(city)
    
    # Extract weather info from the data
    if data.get("main"):
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        icon = data["weather"][0]["icon"]
    else:
        temperature = weather_description = humidity = icon = "Data not available"

    return render_template(
        'index.html', 
        city=city, 
        temperature=temperature, 
        weather_description=weather_description, 
        humidity=humidity, 
        icon=icon,
        cities=CITIES
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3017)
