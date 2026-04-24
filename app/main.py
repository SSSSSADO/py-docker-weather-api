import datetime
import os
import requests


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris"
    data = requests.get(url).json()
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M")

    print(f"{country} {date} {time} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
