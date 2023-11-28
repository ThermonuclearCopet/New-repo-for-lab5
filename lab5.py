"""
lab №5
"""
#pylint: disable=R0913
from enum import Enum


class WeatherType(Enum):
    """Weather enumeration"""
    SUNNY = 1
    CLOUDY = 2
    RAINY = 3
    FOGGY = 4


class Weather:
    """
    Weather class which include all data from measure
    """

    def __init__(self, day, city, country, temp, humidity, wind_speed, weather_type):
        self.__day = day
        self.__city = city
        self.__country = country
        self.__temp = temp
        self.__humidity = humidity
        self.__wind_speed = wind_speed
        self.__weather_type = weather_type

    def get_day(self):
        """get day"""
        return self.__day

    def get_city(self):
        """get city"""
        return self.__city

    def get_temp(self):
        """get temp"""
        return self.__temp

    def get_humidity(self):
        """get humidity"""
        return self.__humidity

    def get_wind_speed(self):
        """get wind speed"""
        return self.__wind_speed

    def get_weather_type(self):
        """get weather enum type"""
        return self.__weather_type

    def get_weather_country(self):
        """get Vietnam"""
        return self.__country

    def __str__(self):
        """class string"""
        return (f"day: {self.__day}, city: {self.__city}, temperature: {self.__temp}, "
                f"humidity: {self.__humidity}, wind speed: {self.__wind_speed},"
                f" weather type: {self.__weather_type}")

    def __repr__(self):
        """class repr"""
        return (f"{self.__day}, {self.__city}, {self.__temp}, {self.__humidity},"
                f" {self.__wind_speed}, {self.__weather_type}")


class WeatherCalendar:
    """class for all weather measurement"""

    def __init__(self):
        self.weather_entries = []

    def add_weather_entry(self, weather_entry):
        """this function receive Weather object and add it to weather entries list"""
        self.weather_entries.append(weather_entry)

    @staticmethod
    def find_max_temperature(day, *weather):
        """finding max temperature at some day"""
        temperatures = []
        for el in weather:
            if el.get_day() == day:
                temperatures.append(el.get_temp())
        if not temperatures:
            print("Not enough data")
            return None

        max_temperature = max(temperatures)
        return max_temperature

    def sort_entries_by_day(self):
        """sorting weather entries by day"""
        self.weather_entries.sort(key=lambda weather: weather.get_day())

    def get_weather_entries(self):
        """getter for weather entries"""
        return self.weather_entries


def is_lviv_weather(humidity, weather_type):
    """checking if weather is like default in Lviv"""
    if humidity > 80 and weather_type == WeatherType.RAINY:
        print("The typical day in Lviv")
    else:
        print("You're lucky, man")


if __name__ == "__main__":
    weather_entry1 = Weather(day="2023-02-20", city="Lviv", country="Ukraine",
                             temp=25, humidity=75, wind_speed=10, weather_type=WeatherType.SUNNY)
    weather_entry2 = Weather(day="2023-02-20", city="Lviv", country="Ukraine",
                             temp=20, humidity=85, wind_speed=5, weather_type=WeatherType.RAINY)
    weather_entry3 = Weather(day="2023-02-23", city="Lviv", country="Ukraine",
                             temp=18, humidity=57, wind_speed=7, weather_type=WeatherType.SUNNY)
    weather_entry4 = Weather(day="2023-02-22", city="Lviv", country="Ukraine",
                             temp=19, humidity=72, wind_speed=4, weather_type=WeatherType.FOGGY)

    calendar = WeatherCalendar()
    calendar.add_weather_entry(weather_entry1)
    calendar.add_weather_entry(weather_entry2)
    calendar.add_weather_entry(weather_entry3)
    calendar.add_weather_entry(weather_entry4)

    max_temp = calendar.find_max_temperature("2023-02-20", weather_entry1, weather_entry2,
                                             weather_entry3, weather_entry4)
    print(f"The max temperature on 2023-02-20 is {max_temp}°C")

    is_lviv_weather(weather_entry2.get_humidity(), weather_entry2.get_weather_type())

    calendar.sort_entries_by_day()
    str(weather_entry1)

