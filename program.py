import pandas as pd
import dateutil
import re

year = 2016
pattern = re.compile(str(year))
data = pd.read_csv('pollution_us_2000_2016.csv')
data['year'] = data['Date Local'].apply(dateutil.parser.parse, dayfirst=True)
data['CO Mean'] = data['CO Mean'].map(lambda x: x*1000)
data['O3 Mean'] = data['O3 Mean'].map(lambda x: x*1000)

#get just data for year 2015
# can extract to a function or method later
data_result = data.loc[(data['Date Local'] > (str(year-1) + '-12-31')) & ( data['Date Local'] < str(year + 1))]



# Average emission of pollutants per day in each year
# print data.groupby(data['year'].map(lambda x: x.year))[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].mean()

# print data.groupby(['State', data['year'].map(lambda x: x.year)])[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].mean()



result =  data_result.groupby([data['year'].map(lambda x: x.month)])[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].mean()
result.rename(index=str, columns={"year": "month"})
print year
print result
#2010 without grouping data


#get 2010 data
# year_2010 = data.loc[(data['Date Local'] > (str(year-1) + '-12-31')) & ( data['Date Local'] < str(year + 1))]

# result =  data_2015[['NO2 Mean', 'CO Mean', 'SO2 Mean', 'O3 Mean']].mean()

# print result