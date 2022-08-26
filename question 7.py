



my_dict=[{"first":"1"},{"second":"2"},{"third":"1"},{"forth":"5"},{"dive":"5"},{"six":"9"},{"seven":"7"}]
a=[]
for i in range(len(my_dict)):
    for j in my_dict[i]:
        if my_dict[i][j] not in a:
            a.append(my_dict[i][j])
print(a)



