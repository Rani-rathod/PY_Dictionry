# num=int(input("enter the no:-"))
# d={}
# for i in range(0,num):
#     d[i]=i**2
# print(d)



# a=['name','age','college']
# b=['aarti',18,'navgurukul']
# c=[2,4,6]
# d={}
# for i in range(len(a)):
#     d1={}
#     for j in range(len(b)):
#         if i==j:
#             d1.update({b[j]:c[j]})
#         d.update({a[i]:d1})
# print(d)




n={'a':10,'b':20,'c':30}
a=input("enter the key:-")
if a in n:
    n.pop(a)
    print(n)
else:
    c=int(input("enter the value:-"))
    n.update({a:c})
    print(n) 
