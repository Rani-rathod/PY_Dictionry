


dict={'a':2,'b':5,'c':6,'d':7,'e':8,'f':10}
sum=0
sum1=0
for i in dict:
    if dict[i]%2==0:
        print(dict[i],"even number")
        sum=sum+dict[i]
    else:
        print(dict[i],"odd number")
        sum1=sum1+dict[i]
print()
print("Even number sum =",sum)
print("Odd number sum =",sum1)


