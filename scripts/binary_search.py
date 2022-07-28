list_temp = [1,2,3,4,6,7,8]

# def binary_search(input_list, elem_search, low, middle, high):
#
#
#     if(input_list[middle]==elem_search):
#         return middle
#     elif(input_list[middle]>elem_search):
#         input_list = input_list[:middle]
#         low = 0
#         high = len(input_list) -1
#         middle = (low+high)//2
#         binary_search(input_list, elem_search, low, middle, high)
#     elif(input_list[middle]<elem_search):
#         input_list = input_list[middle+1:]
#         low = 0
#         high = len(input_list) -1
#         middle = (low+high)//2
#         binary_search(input_list, elem_search, low, middle, high)
#     else:
#         return -1
#
# elem_search = 6
#
# low = 0
# high = len(list_temp) - 1
# middle = (low + high) // 2
# binary_search(sorted(list_temp), elem_search, low, middle, high)



def binary_search(num_list, element):
    low=0
    high=len(num_list)-1
    mid=(low+high)//2
    while low<=high:
        if(element<num_list[mid]):
            # low=mid+1
            high=mid-1
        elif(element>num_list[mid]):
            # high=mid-1
            low = mid + 1
        else:
            return mid #print("Element is in the list at index", mid)

        mid=(low+high)//2

    return -1 #print("Element is not in the list")

index = binary_search(sorted([14,13,12,11,10,9,8]), 11)
print(index)