import random
kkk = {}
b = ['d','c','b','a']


for i in range(len(b)):
    tempDict = {b[i]:random.randint(1, 1350)}
    kkk.update(tempDict)



a = kkk['a']
tempList = []
tempDict = {}
for i in kkk:
    tempDict = {i:kkk[i]}
    tempList.append(tempDict)


b = sorted(tempList)
print b
#
# for i in b:
#     for key, value in i.iteritems():
#         print value
