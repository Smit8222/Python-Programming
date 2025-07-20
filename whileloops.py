# # i =0
# # while i <= 10:
# #     print(i)
# #     i += 1


# i = 1
# while i<= 10:
#     if i == 4:
#         break
#     print(i)
#     i += 1

i = 1
while i<= 20:
    if (i % 2 != 0):
        i += 1
        continue #skips the rest of the loop and goes to the next iteration
    print(i)
    i += 1