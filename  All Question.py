
# d1={'a': 100, 'b': 200, 'c':300}
# d2={'a': 300, 'b': 200, 'd':400}
# for i in d1 :
#     if i in d2 :
#         d2[i]=(d1[i]+d2[i])
#     else :
#         d2[i]=d1[i]
# print(d2)



# a='w3resource'
# count={}
# for i in a:
#     if i not in count:
#         count[i]=1
#     else:
#         count[i]+=1
# print(count)



# n=int(input("enter the number:-"))
# a={}
# for i in range(1,n+1):
#     key=i
#     value=i*i
#     z={key:value}
#     a.update(z)
# print(a)


# d={}
# n=15
# for i in range(1,n+1):
#     key=i
#     value=i*i
#     z={key:value}
#     d.update(z)
# print(d)


# dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# for i in dic:
#     for j in dic:
#         if dic[i]>dic[j]:
#             dic[i],dic[j]=dic[j],dic[i]
# print(dic)


# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# a={}
# for i in dic1:
#     a.update(dic1)
#     a.update(dic2)
#     a.update(dic3)
# print(a)

# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# a={}
# for i in(d1,d2,d3):
#     a.update(i)
# print(a)


# d={0:10, 1:20}
# d[2]=30
# print(d)


# dic= {'data1':100,'data2':-54,'data3':247}
# a=1
# for k in dic:    
#     a=a*dic[k]
# print(a)


# d1={'a': 100, 'b': 200}
# d2={'x': 300, 'y': 200}
# dic={}
# for x in (d1,d2):
#     dic.update(x)
# print(dic)



# list=['a','b','c','d','e','f']
# list1=[1,2,3,4,5]
# dict={}
# for i in list:
#     for j in list1:
#         dict[i]=j
#         list1.remove(j)
#         break
# print(dict)



# dict_num={4:10,7:20,1:30,5:40,2:50,8:60}
# count=0
# for i in dict_num:
#     count=count+1
#     print(i,dict_num[i],count)



# list1=['S001', 'S002', 'S003', 'S004']
# list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# dict={}
# for i in list1:
#     for j in list2:
#         dict[i]=j
#         list2.remove(j)
#         break
# print(dict)



# dict={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# a=[]
# for i in dict:
#     for j in dict:
#         if dict[i]==dict[j] and i!=j:
#             a.append(i)
# print(a)


# students={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# b=[]
# for i in students:
#     b.append(i)
# print(b)


# dic={'C1':[10,20,30],'C2':[20,30,40],'C3':[12,34]}
# b={}
# for i in dic:
#     for j in dic:
#         if dic[i]!=[]:
#             b.update({i:dic[j]})
# print(b)



# dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
# dic.popitem()
# print(dic)


# dict={'a':1,'b':2,'c':3,'d':4}
# if 'a' in dict: 
#     del dict['a']
# print(dict)



# dict={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in dict:
#     print(dict[i])


# dic={'physics':100,'math':80,'chemistry':50}
# for i in dic:
#     print(i)


# students={'Theodore':19,'Roxanne':22,'Mathew':21,'Betty':20}
# for i in students:
#     print([i])


# students={'Theodore':19,'Roxanne':22,'Mathew':21,'Betty':20}
# a=[]
# for i in students:
#     a.append(students[i])
# print(a)


# color={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# a=[]
# for i in color:
#     a.append(color[i])
# print(a)




# dic={'Cierra Vega':175,'Alden Cantrell':180,'Kierra Gentry':165,'Pierre Cox':190}
# dic.pop("Kierra Gentry")
# print(dic)



# a=input("enter the number:-")
# b=input("enter the number:-")
# i=0
# c={}
# while i<len(a):
#     c.update({a[i]:b[i]})
#     i+=1
# print(c)




# a={3:5,7:{'a':20,'b':5},7:4}
# sum=0
# for x,y in a.items():
#     if type(y)==dict:
#         for i,j in y:
#             if type(i)==int:
#                 sum+=i
#             if type(j)==int:
#                 sum+=j
#     else:
#         if type(x)==int:
#             sum+=x
#         if type(y)==int:
#             sum+=y
# print(sum)


# data= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# c=[]
# for key in data:
#     for i in key:
#         if key[i] in c:
#             pass
#         else:
#             c.append(key[i])

# print(c)


# dic={'Rani':17,'Anisha':19,'Guddu':5,'Saurav':10}
# # a=[]
# # for key in dic:
# #     if key in a:
# #         pass
# #     else:
# #         a.append(key)
# # print(a)
# a=[]
# for velue in dic:
#     if velue in a:
#         pass
#     else:
#         a.append(dic[velue])
# print(a)


