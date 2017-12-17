import pandas as pd
import dateutil
import datetime

class MyClass:
  def __init__(self, state, county, city, dateLocal, no2Mean, o3Mean, so2Mean, coMean):
    self.state = state
    self.county = county
    self.city = city
    self.dateLocal = dateLocal
    self.no2Mean = no2Mean
    self.o3Mean = o3Mean
    self.so2Mean = so2Mean
    self.coMean = coMean

results = []

data = pd.read_csv('pollution_us_2000_2016.csv', nrows=40)

data['date'] = data['Date Local'].apply(dateutil.parser.parse, dayfirst=True)

lines = data['NO2 Mean'].count()
no2MeanAverage = data['NO2 Mean'].sum() / lines




print 'The average consum of NO2 Mean from ' + str(min(data['date'])) + ' to ' + str(max(data['date'])) + ' is: ' + str(no2MeanAverage)
