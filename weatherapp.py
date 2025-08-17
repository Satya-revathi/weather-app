import requests

def get_weather(city):
    API_KEY = "c322be1ac9cc88616d248fe53e65d04f"  # Replace with your OpenWeather API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description']}")
    else:
        print(f"Error: {data.get('message', 'Unable to fetch weather')}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
