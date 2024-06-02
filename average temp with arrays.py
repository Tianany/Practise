import array
a= array.array('d',[])
n =7
print("enter the seven different temperatures  ")
for i in range(n):
    temp =float(input("enter temperature "))
    a.append(temp)
    sum =0.0
    for item in a:
        sum =sum+temp
        average = sum/7
        print("the average is ",average)

