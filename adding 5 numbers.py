Total =[]
for num in range(0,100):
    if (num%3 == 0) or (num%5 ==0):
        Total.append(num)

print(sum(Total))
