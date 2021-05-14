import urllib.request
import json

API_KEY='key'



class projNoahData():
  def __init__(self):
    # both reqs are obtaining data for marikina ONLY
    self.f_projNoah = urllib.request.urlopen('http://noah.up.edu.ph/api/seven_day_forecast/1623')

  def readData(self):
    self.json_string_2 = self.f_projNoah.read()

  def parseData(self):
    # parse json
    self.parsed_json_2 = json.loads(self.json_string_2)

  def storeData(self):
    # store weather data in .json file
    with open('data_projNoah.json', 'w') as outfile:
        json.dump(self.parsed_json_2, outfile, indent=4, sort_keys=True, separators=(",", ':'))

class projNoahDataFull():
  def __init__(self):
    self.f_projNoahFull = urllib.request.urlopen('http://noah.up.edu.ph/api/seven_day_forecast')

  def readData(self):
    self.json_string_3 = self.f_projNoahFull.read()

  def parseData(self):
    # parse json
    self.parsed_json_3 = json.loads(self.json_string_3)

  def storeData(self):
    # store weather data in .json file
    with open('data_projNoahFull.json', 'w') as outfile:
        json.dump(self.parsed_json_3, outfile, indent=4, sort_keys=True, separators=(",", ':'))


class openWeatherData():
  def __init__(self):
    # both reqs are obtaining data for marikina ONLY
    self.f_openWeather = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/forecast?q=Marikina&appid=2024c1d37dcfec931dc53bfaded31b44')

  def readData(self):
    self.json_string_1 = self.f_openWeather.read()

  def parseData(self):
    # parse json
    self.parsed_json_1 = json.loads(self.json_string_1)

  def storeData(self):
    # store weather data in .json file
    with open('data_openWeather.json', 'w') as outfile:
      json.dump(self.parsed_json_1, outfile, indent=4, sort_keys=True, separators=(",", ':'))




def obtainAndStoreNoah():
    dataNoah = projNoahData()
    dataNoah.readData()
    dataNoah.parseData()
    dataNoah.storeData()


def obtainAndStoreNoahFull():
    dataNoahFull = projNoahDataFull()
    dataNoahFull.readData()
    dataNoahFull.parseData()
    dataNoahFull.storeData()

def obtainAndStoreOpenWeather():
    dataOpenWeather = openWeatherData()
    dataOpenWeather.readData()
    dataOpenWeather.parseData()
    dataOpenWeather.storeData()

if __name__ == "__main__":
    obtainAndStoreNoah()
    obtainAndStoreOpenWeather()
    obtainAndStoreNoahFull()





