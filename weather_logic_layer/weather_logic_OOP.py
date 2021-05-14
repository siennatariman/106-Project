import sqlite3
import datetime
import weather_data_OOP


class jsonToSql():

  def __init__(self, parsedJsonOW, parsedJsonN):
    openwDict = parsedJsonOW
    noahDict = parsedJsonN

    self.dataOW = list()
    for row in openwDict['list']:
        date = datetime.datetime.strptime(row['dt_txt'], "%Y-%m-%d %H:%M:%S")
        data = (date, str(row['weather'][0]['main']))
        self.dataOW.append(data)

    self.dataNoah = list()
    for row in noahDict['data']:
        date = datetime.datetime.strptime(row['date'], "%Y-%m-%d")
        data = (date, str(row['readings'][0]['heat_index']), float(row['readings'][0]['rainfall']),
        str(row['readings'][0]['temperature']), str(row['readings'][0]['time']))
        self.dataNoah.append(data)
    

  def createTable(self):
    try:
        db = sqlite3.connect('Weather')
        cursor = db.cursor()
        cursor.executescript('''
            drop table if exists weatherDataNoah;
            create table weatherDataNoah (
                date datetime,
                heat_index float, 
                rainfall float, 
                temperature float, 
                time string);
            ''')
        
        cursor.executescript('''
            drop table if exists weatherDataOW;
            create table weatherDataOW (
                date datetime,
                main string);
            ''')

    except Exception as e:
        print('Error: ',e)
    else:
        print('table created')

  def insertTable(self):
    try:
        db = sqlite3.connect('Weather')
        cursor = db.cursor()
        cursor.executemany('''insert into weatherDataNoah
                          values(?, ?, ?, ?, ?)''',
                          self.dataNoah)

        cursor.executemany('''insert into weatherDataOW
                          values(?, ?)''',
                          self.dataOW)                      
    except Exception as e:
        print(f'error in inserting data: {e}')
    else:
        db.commit()
        print('data inserted')

if __name__ == "__main__":
    openWeather = weather_data_OOP.openWeatherData() 
    projNoah = weather_data_OOP.projNoahData()

    weatherjsonSql = jsonToSql(openWeather.getParsedJson(), 
    projNoah.getParsedJson())
    
    weatherjsonSql.createTable()
    weatherjsonSql.insertTable()
