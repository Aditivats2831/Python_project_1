'''Weather API Fetcher
Description: A program that fetches and displays the current weather of a specified location using an API.'''

import requests

def fetch_weather(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
        'appid': api_key
    }
    
    # Make a get request to the OpenWeatherMap API
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        # Extract data in JSON format
        weather_data = response.json()
        
        # Extract relevant information
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        
        # Print the weather information
        print(f"Weather in {city}: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Error fetching weather data: {response.status_code}")


if __name__ == "__main__":
    # Prompt the user to enter API key and city name
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    city = input("Enter city name: ").strip()
    
    fetch_weather(api_key, city)
