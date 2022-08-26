

list1=["One","Two","Three","Four","Five"]
list2=[1,2,3,4,5]
dict={}
for i in list1:
    for j in list2:
        dict[i]=j
        list2.remove(j)
        break
print(dict)


# a=[1,2,3,4,5,6]
# dic={}
# for i in a:
#     dic[i]=i
#     dic.update({dic[i]:i})
# print(dic)




# a=[1,2,3,4,5,6]
# dic={}
# i=0
# while i<len(a):
#     j=0
#     while j<=i-1:
#         dic.update({a[i]:a[j]})
#         j+=1
#     i+=1
# print(dic)