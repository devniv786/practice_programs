from itertools import combinations_with_replacement

def calculate_phone_number(N:str):
    index_missing = []
    for i, v in enumerate(N):
        if v == '?':
            index_missing.append(i)
    comb_input = []
    for i in range(0,10):
        comb_input.append(i)
        combinations = list(combinations_with_replacement(comb_input, len(index_missing)))
        combinations.sort(key=sum)
        print((combinations))
        for com in combinations:
            temp = N
            for val in com:
                temp = temp.replace('?', str(val), 1)
                print(temp)
            if(int(temp)%3==0):
                print('Number is:', temp)
                break

if __name__=='__main__':
    number = input('Enter a missing phone number')
    calculate_phone_number(number)