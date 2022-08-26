
dict={"Alex":['subj1','subj2','subj3'],"Gavid":['subj1','subj2']}
count=0
for x in dict:
    for y in dict[x]:
        count+=1
print("total=",count)
