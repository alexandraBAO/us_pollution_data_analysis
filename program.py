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

N=5
f=open("pollution_us_2000_2016.csv")
for i in range(N):
  line=f.next().strip().split(',')
  if (i > 0):
    results.append(MyClass(line[5], line[6], line[7], line[8], line[10], line[15], line[20], line[25]))
f.close()

print results[3].no2Mean
