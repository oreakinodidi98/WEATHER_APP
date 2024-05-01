from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# load api value from env file
load_dotenv()

#get current weather function 
def get_current_weather(city="London"):
    # provide default value for city in case it is not provided
    #create request URL
    
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEATHER_API_KEY')}&units=metric"

    #get weather data in JSON format
    weather_data = requests.get(request_url).json()
    #return weather data
    return weather_data

if __name__ == "__main__":
    print(f'\n*** Get Current Weather Conditions ***\n')

    city = input("\nEnter city name: ")

    weather_data = get_current_weather(city)
    print(f'\n')
    pprint(weather_data)
    # print(f"Temperature: {weather_data['main']['temp']}°C")
    # print(f"Description: {weather_data['weather'][0]['description']}")