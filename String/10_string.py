sentence  = "coding in python is fun "
sum= 0 
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for char in sentence.lower():
     if char in vowels:
         sum += 1         



print(f"There are {sum} vowels in the given sentence.")         