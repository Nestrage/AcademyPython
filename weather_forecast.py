import pprint

import requests
from datetime import datetime

CLIENT_ID = "bTq8gSdbwIjTeLvgaLxQU"
CLIENT_SECRET = "QaMvwqGfGmVLjXEa4wM2hiuJbZTt2vbkX1kVVUpF"


def convert_epoch_to_str(datetime_epoch: int) -> str:
    fmt = "%Y-%m-%d %H:%M:%S"
    return datetime.fromtimestamp(datetime_epoch).strftime(fmt)

#
class YahooWeatherForecast:
    def __init__(self):
        self.weather_cache_c = {}
        self.weather_cache_city = {}

    def get(self, city, country):
        if self.weather_cache_c.get(country) and self.weather_cache_city.get(city):
            return self.weather_cache_city[city]
        url = f"https://api.aerisapi.com/forecasts/{city},{country}?&format=json&filter=day&limit=7&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"
        print("requesting data")
        data = requests.get(url).json()
        all_days = data["response"][0]["periods"]
        forecast = []
        for day in all_days:
            forecast.append(
                {
                    "datetime": convert_epoch_to_str(day["timestamp"]),
                    "max_temp": day["maxTempC"],
                    "min_temp": day["minTempC"],
                }
            )
        self.weather_cache_city[city] = forecast
        self.weather_cache_c[country] = self.weather_cache_city
        return forecast


class CityInfo(object):
    def __init__(self, city, country, weather_forecast=None):
        self.city = city
        self.country = country
        self._weather_forecast = weather_forecast or YahooWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city, self.country)


def _main():
    weather_forecast = YahooWeatherForecast()
    for i in range(4):
        city_info = CityInfo("Kiev", "Ukraine", weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()
        pprint.pprint(forecast)
    for i in range(2):
        city_info = CityInfo("Poltava", "Ukraine", weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()
        pprint.pprint(forecast)
    for i in range(4):
        city_info = CityInfo("Tallin", "Estonia", weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()
        pprint.pprint(forecast)



if __name__=='__main__':
    _main()
    print("running_main")
