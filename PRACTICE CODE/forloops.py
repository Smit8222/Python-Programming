num = (1,3,5,7,9,11,13,15,17,19)
x = 13

for vul in num:
    if vul == x:
        print("Found it!")
        break
    print(vul)
    vul += 1
else:
    print("Not found!")