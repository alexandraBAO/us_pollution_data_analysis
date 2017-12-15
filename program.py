
iris_dic = {}

for l in open('iris.data.txt','r'):
    sepalL, sepalW, petalL, petalW, classN = l.strip('\n').split(',')
    if classN in iris_dic.keys():
        iris_dic[classN].append([sepalL, sepalW, petalL, petalW])
    else:
        iris_dic[classN] = [ [sepalL, sepalW, petalL, petalW] ]

print iris_dic
#print sum(iris_dic['Iris-virginica'][])


#print sum([float(x[0]) for x in iris_dic['Iris-virginica']])

#for k in iris_dic:
#    print k
#    print iris_dic[k]
#    print '----------------'
