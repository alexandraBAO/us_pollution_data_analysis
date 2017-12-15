N=5
f=open("pollution_us_2000_2016.csv")
for i in range(N):
    if i > 0:
      line=f.next().strip().split(',')
      print line[2]
f.close()