from itertools import combinations


def least_integer(input_list:list) -> int:
    max_sum = sum(input_list)
    min_elem = min(input_list)
    max_elem = max(input_list)

    input_list.sort()
    values_list = [i for i in range(1, max_sum+1)]

    temp_sum = []
    for i in range(1, len(input_list)+1):
        for com in combinations(input_list, i):
            temp_sum.append(sum(com))

    temp_sum = list(set(temp_sum))

    for val in values_list:
        if(val not in temp_sum):
            return val
        else:
            continue

    return max_sum+1


input_list = [1,2,4,5,7,10]
print(least_integer(input_list))
