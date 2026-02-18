a = [1,2,3,4,5]
print(a)
for i in range(len(a)) :
    temp = a[1]
    a[1] = a[2]
    a[2] = temp
print(a)