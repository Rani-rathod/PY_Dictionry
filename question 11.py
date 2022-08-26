

# my_dict={'a':50,'b':58,'c':56,'d':40,"e":100,'f':20}
# max=0
# dic={}
# for i in my_dict:
#     if my_dict[i]>max:
#         key1=i
#         max=my_dict[i]
# dic[key1]=max
# max1=0
# for i in my_dict:
#     if my_dict[i]>max1 and my_dict[i]!=max:
#         key2=i
#         max1=my_dict[i]
# dic[key2]=max1
# max2=0
# for i in my_dict:
#     if my_dict[i]>max2 and my_dict[i]!=max and my_dict[i]!=max1:
#         key3=i
#         max2=my_dict[i]
# dic[key3]=max2
# print(dic)


my_dict={'a':56,'b':58,'c':50,'d':40,"e":100,'f':20}
a=[]
max=0
for i in range(3):
    for j in my_dict:
        if my_dict[j]>max:
            max=my_dict[j]
            a.append(max)
            # a.append(j)
print(a)
