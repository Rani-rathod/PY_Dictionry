
dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
# a={}
# for i in dic1:
#     a.update(dic1)
#     a.update(dic2)
#     a.update(dic3)
# print(a)


for i in dic1:
    if i in dic2:
        dic2[i]=dic2[i]+dic1[i]
    else:
        dic2[i]=dic1[i]
print(dic2)
