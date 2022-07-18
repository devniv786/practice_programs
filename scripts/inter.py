# a = 12345
# import math
#
# def reverse_number(a):
#     num=0
#     while a!=0:
#         res = a % 10
#         print(res,end='')
#         a = a // 10
#         if(a!=0):
#             num = num + res * math.pow(10, len(str(a)))
#
#
#     return num
#
# output = reverse_number(a)
# print(output)

names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)

