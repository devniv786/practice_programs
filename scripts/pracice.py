
# def repeat_first(input_list):
#     num_dict = {}
#     for i in input_list:
#         if i in num_dict:
#             return i
#         else:
#             num_dict[i] = 'Hello'
#
#
list_temp = [1,2,3,4,6,7,8]
# print(repeat_first(list_temp))

#
#
# def first_common(l1, l2, l3):
#     max_elem = max(max(l1), max(l2), max(l3))
#     for e1, e2, e3 in zip(l1, l2, l3):
#
#
#
# list1 = [1,2,3,4,5,6]
# list2 = [5,6,7]
# list3 = [6,7,8,9,10,11,12,13]

def binary_search(input_list, elem_search, low, middle, high):


    if(input_list[middle]==elem_search):
        return middle
    elif(input_list[middle]>elem_search):
        input_list = input_list[:middle]
        low = 0
        high = len(input_list) -1
        middle = (low+high)//2
        binary_search(input_list, elem_search, low, middle, high)
    elif(input_list[middle]<elem_search):
        input_list = input_list[middle+1:]
        low = 0
        high = len(input_list) -1
        middle = (low+high)//2
        binary_search(input_list, elem_search, low, middle, high)
    else:
        return -1

elem_search = 6

low = 0
high = len(list_temp) - 1
middle = (low + high) // 2
binary_search(sorted(list_temp), elem_search, low, middle, high)



def gen_example(n):
    for i in range(n):
        yield i


gen_op = gen_example(10)
print(gen_op.__next__())
print(gen_op.__next__())
print(gen_op.__next__())
print(gen_op.__next__())
print(gen_op.__next__())
print(gen_op.__next__())
print(gen_op.close())
print(gen_op.__next__())
print(gen_op.__next__())
print(gen_op.__next__())
print(gen_op.__next__())
print(gen_op.__next__())
print(gen_op.__next__())



def square_plus_one(func):
    def wrapper(*args):
        op = func(*args)
        return op +1
    return wrapper

@square_plus_one
def square(n):
    return n**2

print(square(3))







import enum
# Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 3
# printing all enum members using loop
print ("The enum members are : ")
for weekday in (Days):
   print(weekday)