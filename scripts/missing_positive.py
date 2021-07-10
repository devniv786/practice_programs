def find_kth_missing_positive_number(input_list:list, index_find:int) ->int:
    input_list.sort()
    comp_list = [i for i in range(1, 1001)]
    missing_list = []
    count = 0
    for i, val in enumerate(comp_list,start=1):
        if val not in input_list:
            missing_list.append(val)
            count += 1
            if count == index_find:
                break
            else:
                continue
    return missing_list[index_find-1]


if __name__=="__main__":
    input_list = input("Enter a list of comma seperated positive numbers without duplicates").replace('[', '').replace(']', '').split(",")
    input_list = [int(i) for i in input_list]
    index_find = int(input("Enter the index to find the positive integer that is missing from this array"))
    print(find_kth_missing_positive_number(input_list, index_find))
