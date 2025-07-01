import requests
import json

def get_weather(api_key, location):
    """Fetch weather data from OpenWeatherMap API"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Get temperature in Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    """Display weather information in a user-friendly format"""
    if not weather_data:
        print("No weather data available.")
        return
    
    try:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        weather_desc = weather_data['weather'][0]['description'].title()
        wind_speed = weather_data['wind']['speed']
        
        print("\n=== Current Weather ===")
        print(f"Location: {city}, {country}")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Weather: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    except KeyError:
        print("Error: Unexpected weather data format.")
        print("Full response:", json.dumps(weather_data, indent=2))

def main():
    print("=== Simple Weather App ===")
    print("Get current weather for any city or ZIP code\n")
    
    api_key = "ANY ACTIVE API KEY"   #GET FROM  https://openweathermap.org/
    
    while True:
        location = input("Enter city name or ZIP code (or 'quit' to exit): ").strip()
        if location.lower() == 'quit':
            break
            
        if not location:
            print("Please enter a location.")
            continue
            
        weather_data = get_weather(api_key, location)
        display_weather(weather_data)
        
        print("\n" + "="*30 + "\n")

if __name__ == "__main__":
    main()