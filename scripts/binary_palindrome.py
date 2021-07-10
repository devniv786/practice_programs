

def check_binary_palindrome(binary_form):
    """
    Description: checks id the binary form of an integer number is a palindrome or not
    :param binary_form:
    :return: True if it is a palindrome, else False
    """

    if binary_form[::-1]==binary_form:
        return True
    else:
        return False

def get_consecutive_10_binary(binary_form):
    """
    Description: Returns maximum consecutive occurence of 0`s and 1`s in binary representation of a number
    :param binary_form:
    :return: A dict with keys as 0 & 1, & values as max consecutive count
    """

    max_zeros = 0
    max_ones = 0
    count_dict = {}
    count_dict["0"] = 0
    count_dict["1"] = 0

    for digit in binary_form:
        if int(digit)==0:
            # count_zeros += 1
            max_ones = 0
            max_zeros+=1
            if(count_dict["0"] < max_zeros):
                count_dict["0"] = max_zeros
        else:
            # count_ones += 1
            max_ones+=1
            max_zeros = 0
            if(count_dict["1"] < max_ones):
                count_dict["1"] = max_ones

    return count_dict

input_number = int(input("Enter a number to check if its binary representation is palindrome: "))
binary_form = bin(input_number)
palindrome_flag = check_binary_palindrome(binary_form[2:])
count_binary_dict = get_consecutive_10_binary(binary_form[2:])
print(count_binary_dict)
print("The binary representation {} of the number {} is a palindrome: {}".format(binary_form[2:], input_number, palindrome_flag))
