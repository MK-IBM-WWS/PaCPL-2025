from requests.exceptions import RequestException
import requests
import time

def retry(func):
    def wrapper_retry(*args, **kwargs):
        seconds = 0.5
        while True:
            try:
                return func(*args, **kwargs)
            except RequestException:
                print(f"Failed to get data from API. Retrying in {seconds} seconds")
                time.sleep(seconds)

    return wrapper_retry

class Weather:
    def __init__(self,*, location:str, date:str):
        base_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'
        unit_group = 'metric'
        content_type = 'json'
        api_key = 'XL3Y3ET4F729XHZH6PH2LXVKY'
        self.url = f"{base_url}/{location}/{date}/{date}?unitGroup={unit_group}&contentType={content_type}&key={api_key}"
        self.weather_by_hours=[]
        self.get_weather_by_hours_for_day_from_api()

    @retry
    def get_weather_by_hours_for_day_from_api(self):
        response = requests.get(self.url)
        weather_by_days = response.json()["days"]
        self.weather_by_hours = weather_by_days[0]["hours"]

    def get_temperature_hours(self)->dict:
        temp = {}
        for weather in self.weather_by_hours:
            temp[weather["datetime"][:-3]] = weather["temp"]
        return temp
