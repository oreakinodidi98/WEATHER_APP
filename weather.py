from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# load api value from env file
load_dotenv()

#get current weather function 
def get_current_weather(city="London"):
    # have provide default value for city in case it is not provided
    #create request URL
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEATHER_API_KEY')}&units=metric"
    #get weather data in JSON format
    weather_data = requests.get(request_url).json()
    #return weather data
    return weather_data

# to run in the terminal
if __name__ == "__main__":
    print(f'\n*** Get Current Weather Conditions ***\n')
    city = input("\nEnter city name: ")
    #check for empty string or strings with only spaces
    if not bool(city.strip()):
        #default value for city of kanas city if no city is provided or city is only spaces
        city = "London"
    weather_data = get_current_weather(city)
    print(f'\n')
    pprint(weather_data)
    