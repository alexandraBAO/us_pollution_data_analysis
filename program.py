import pandas as pd
import dateutil

data = pd.read_csv('pollution_us_2000_2016.csv', nrows=10)

data['year'] = data['Date Local'].apply(dateutil.parser.parse, dayfirst=True)
data['city'] = data['City']

# Average emission of pollutants per day in each year
print data.groupby(data['year'].map(lambda x: x.year))[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].mean()
