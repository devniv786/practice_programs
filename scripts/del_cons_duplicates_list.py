import itertools

def delete_consecutive_duplicate_elements(input_list=[]) -> list:
    temp_list = []
    for key, value in itertools.groupby(input_list):
        temp_list.append(list(value))
    final_list = [i[0] for i in temp_list if len(i) == 1]
    return final_list

if __name__=="__main__":
    test_list = [1, 1, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 6]
    final_list = []
    temp = None
    for i in test_list:
        if(temp!=i):
            final_list.append(i)
        else:
            if i in final_list:
                final_list.remove(i)
        temp = i
    print(test_list)
    op_list = delete_consecutive_duplicate_elements(test_list)
    print("Final list without consecutive duplicate elements is: {}".format(op_list))


a = ["Apple","Facebook","Tesla"]
b = ["1 Mar 2005", "25 Nov 2013","17 Apr 2008"]
