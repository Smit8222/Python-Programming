'''Q.1) write a python program to display a string and count charecter in string using a loop.'''
print(__doc__)
msg = "good bye"
count = 0
for i in range(0 , len(msg)):
    print(msg[i] , end = "")
    count = count + 1
print("Total no. of charecter = " , count)
print(msg[ : :-1])