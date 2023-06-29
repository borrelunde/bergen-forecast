from metno_locationforecast import Place, Forecast
from metno_locationforecast.data_containers import Variable, Interval

APP_NAME = 'weather-forecast'
APP_VER = '1.0.0'

# Create a Place instance for Bergen, Norway.
bergen: Place = Place(name="Bergen", latitude=60.3930, longitude=5.3242, altitude=0)

# Create a Forecast instance for the place Bergen, Norway.
# User agent and save location is provided by the configuration file "setup.cfg".
forecast_bergen: Forecast = Forecast(place=bergen, forecast_type='compact')

# Update the forecast. This requests data from the MET API and saves data to the save location.
api_response: str = forecast_bergen.update()


def present_forecast(forecast_response: str, forecast: Forecast):
    place: Place = forecast.place
    first_interval: Interval = forecast.data.intervals[0]

    print(f'Response: {forecast_response}')
    print('')
    print(f'Forecast for {place.name} between {first_interval.start_time} GMT and {first_interval.end_time} GMT:')

    variables: dict[str, Variable] = first_interval.variables
    for variable_name in variables:
        variable: Variable = variables[variable_name]
        print(f'  {variable.name.replace("_", " ")}: {variable.value} {variable.units}')


if __name__ == "__main__":
    # Print the application name and version.
    print(f'{APP_NAME} version {APP_VER}')

    # Print the forecast data.
    present_forecast(forecast_response=api_response, forecast=forecast_bergen)

    # Print an empty new line to separate the forecast data from whatever comes next.
    print()
