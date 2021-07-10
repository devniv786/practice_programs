import itertools

def get_maximum_consecutive_positive_elements(list=[]) -> int:
    temp_max_count = 0
    max_cons_elem_count = 0
    for i in list:
        if int(i) > 0:
            temp_max_count += 1
        else:
            if temp_max_count > max_cons_elem_count:
                max_cons_elem_count = temp_max_count
                temp_max_count = 0

    return max_cons_elem_count

if __name__=="__main__":
    list = input("Enter a comma seperated list of integers").split(",")
    # print(list)
    print(get_maximum_consecutive_positive_elements(list))

