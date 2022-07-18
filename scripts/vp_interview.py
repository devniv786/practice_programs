
def fibo(n):
    fibo_list = []
    if(n==1):
        return 0
    if(n==2):
        return 0,1
    a,b = 0,1
    fibo_list.append(a)
    fibo_list.append(b)
    for i in range(n-2):
        c = a +b
        fibo_list.append(c)
        a= b
        b = c

    return fibo_list


print(fibo(5))
print(fibo(1))
print(fibo(2))






a = {'orange':3, 'mango':1, 'lemon':5}
keys = sorted(list(a.keys()))
values = sorted(list(a.values()))
for key in keys:
    print(f'{key}:{a[key]}', end=',')
for value in values:
    print()

from collections import OrderedDict
dic = OrderedDict({'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'})
OrderedDict()

from collections import OrderedDict

dict = {'ravi': '10', 'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)

from collections import defaultdict
test_dict = defaultdict(lambda : "Key not present")
test_dict['orange'] = 3
test_dict['mango'] = 5
print(test_dict['apple'])

# Python program to display all integers within the range 100-200 whose sum of digits is an even number

for i in range(100,201):
    sum = 0
    temp = i
    while(temp!=0):
        sum = sum + (temp%10)
        temp = temp//10
    #print(i)
    # print(sum)
    if(sum%2==0):
        print(i)


def binary_search(numbers, x):
    low = 0
    high = len(numbers) - 1
    if(x==numbers[(low+high)//2]):
        return (low+high)//2
    elif(x<numbers[(low+high)//2]):
        binary_search(numbers[:((low+high)//2)], x)
    elif (x > numbers[(low + high) // 2]):
        binary_search(numbers[((low + high) // 2)+1:], x)
    else:
        return -1

a = binary_search([ 1,4,6,7,12,17,25 ], 17)
print(a)