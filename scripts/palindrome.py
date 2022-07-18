
def check_make_palindrome(word:str):
    l = len(word)
    word = list(word)
    if(word==word[::-1]):
        return 0
    else:
        match = True
        count = 0
        for i in range(len(word)//2):
            left_pointer = i
            right_pointer = len(word) - left_pointer - 1
            while right_pointer > left_pointer:
                if(word[right_pointer]==word[left_pointer]):
                    break
                else:
                    right_pointer -=1

            if right_pointer==left_pointer:
                match = False
                return -1
            else:
                for j in range(right_pointer, len(word) - left_pointer - 1):
                    (word[j], word[j + 1]) = (word[j + 1], word[j])

                    count += 1
        if match:
            return (count)
        else:
            return -1








if __name__=="__main__":
    input_str = input('Enter a word')
    output = check_make_palindrome(input_str)
    print(output)