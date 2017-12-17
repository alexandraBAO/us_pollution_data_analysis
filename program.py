import pandas as pd
import dateutil

data = pd.read_csv('pollution_us_2000_2016.csv')

data['year'] = data['Date Local'].apply(dateutil.parser.parse, dayfirst=True)

# print data.groupby(data['year'].map(lambda x: x.year))[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].mean()
print data.groupby(data['year'].map(lambda x: x.year))[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].max()
	