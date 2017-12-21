import pandas as pd
import dateutil
import re

pattern = re.compile('2015')
data = pd.read_csv('pollution_us_2000_2016.csv')

#get just data for year 2015
# can extract to a function or method later
year = 2015
data = data.loc[(data['Date Local'] > (str(year-1) + '-12-31')) & ( data['Date Local'] < str(year + 1))]


data['year'] = data['Date Local'].apply(dateutil.parser.parse, dayfirst=True)
data['CO Mean'] = data['CO Mean'].map(lambda x: x*1000)
data['O3 Mean'] = data['O3 Mean'].map(lambda x: x*1000)

# Average emission of pollutants per day in each year
# print data.groupby(data['year'].map(lambda x: x.year))[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].mean()

# print data.groupby(['State', data['year'].map(lambda x: x.year)])[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].mean()


print data.groupby(['State', data['year'].map(lambda x: x.month)])[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].mean()