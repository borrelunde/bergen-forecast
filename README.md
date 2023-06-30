# Bergen Forecast

## Introduction

Using [metno-locationforecast](https://github.com/Rory-Sullivan/metno-locationforecast); a Python interface for the MET Norway Locationforecast/2.0 service. A free weather data service provided by the Norwegian Meteorological Institute.

## Getting started

It is expected that you have Python installed.

Install the dependency requirements listed in `requirements.txt` with this command.

```bat
pip install -r requirements.txt
```

Run the program with this command.

```
python weather-forecast.py
```

## Batch file

Perhaps you'd like to run the Python program from a batch file. This is an example script provided for that.

*example/path/run-bergen-forecast.bat*
```bat
@ECHO OFF

REM Execute the Python script.
python bergen-forecast.py

REM Prevent terminal from exiting immediately
REM after the Python script is finished.
@PAUSE
```