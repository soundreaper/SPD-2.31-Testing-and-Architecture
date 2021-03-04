class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(observer):
        pass

    def removeObserver(observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers():
        pass

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.


class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.


class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.


class CurrentConditionsDisplay(Observer):

    def __init__(self, weatherData):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData  # save the ref in an attribute.
        weatherData.registerObserver(self)  # register the observer
        # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current conditions:", self.temerature,
              "F degrees and", self.humidity, "[%] humidity",
              "and pressure", self.pressure)


class StatisticsDisplay(Observer):
    def __init__(self, weather_data):
        self.temparature = []
        self.humidity = []
        self.pressure = []
        self.weather_data = weather_data
        weather_data.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temparature.append(temperature)
        self.humidity.append(humidity)
        self.pressure.append(pressure)
        self.display()

    def display(self):
        print("Temperature: ")
        print("\nMinimum: ", min(self.temparature))
        print("\nMaximum: ", max(self.temparature))
        print("\nAverage: ", sum(self.temparature)/len(self.temparature))

        print("\n\nHumidity: ")
        print("\nMinimum: ", min(self.humidity))
        print("\nMaximum: ", max(self.humidity))
        print("\nAverage: ", sum(self.humidity)/len(self.humidity))

        print("\n\nPressure: ")
        print("\nMinimum: ", min(self.pressure))
        print("\nMaximum: ", max(self.pressure))
        print("\nAverage: ", sum(self.pressure)/len(self.pressure))


class ForecastDisplay(Observer):
    def __init__(self, weather_data):
        self.forecast_temp = 0
        self.forecast_humidity = 0
        self.forecast_pressure = 0
        self.weather_data = weather_data
        weather_data.registerObserver(self)

    def predict(self, temperature, humidity, pressure):
        self.forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forecast_humadity = humidity - 0.9 * humidity
        self.forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()

    def display(self):
        print("Temperature: ", self.forecast_temp)
        print("Humidity: ", self.forecast_humidity)
        print("Pressure: ", self.forecast_pressure)


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.setMeasurements(80, 65, 30.4)
        weather_data.setMeasurements(82, 70, 29.2)
        weather_data.setMeasurements(78, 90, 29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.removeObserver(forecast_display)
        weather_data.removeObserver(statistics_display)
        weather_data.setMeasurements(120, 100, 1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
