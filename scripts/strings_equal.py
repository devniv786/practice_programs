def check_string_lists_equal(list1: list[str], list2: list[str]) -> bool:
    string1 = "".join(i for i in list1)
    string2 = "".join(i for i in list2)
    print(string1, string2)
    return True if string1 == string2 else False

if __name__=="__main__":
    str_list1 = input("Enter a list of strings")
    str_list2 = [i for i in input("Enter a list of strings") if i.isalpha()]
    print(check_string_lists_equal(str_list1, str_list1))
