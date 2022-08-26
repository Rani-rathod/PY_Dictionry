

my_dict="MISSISSIPPI"
d1={}
for i in my_dict:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
print(d1)
