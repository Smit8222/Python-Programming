from array import array

n = int(input("Enter the number of elements: "))

arr1 = array('i', [])

print("Enter the elements:")
for i in range(n):
    num = int(input(f"Element {i+1}: "))
    arr1.append(num)

arr2 = array('i', arr1)

print("Original array:", arr1.tolist())
print("Copied array:  ", arr2.tolist())
