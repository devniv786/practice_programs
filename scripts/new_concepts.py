from itertools import groupby
from collections import defaultdict

# ---Itertools groupby function
l = [1,2,3,4,-5,-6,-7]
for key,value in groupby(l, lambda x : "positive" if x > 0 else "Negative"):
    print(key+":",list(value))

test_list = [4, 5, -4, -1, -7, 2, 5, 6, -2, -9, -10]
counter = defaultdict(list)
for key, val in groupby(test_list, lambda ele: "plus" if ele >= 0 else "minus"):
    counter[key].append(len(list(val)))
res = []
for key in ('plus', 'minus'):
    res.append(counter[key])

#-----Counter------

from collections import Counter
test_list1 = [1, 2, 3, 1, 4, 3, 5, 6, 7, 2, 1, 3, 4]
print(Counter(test_list1))

"""The most_common() Function
The Counter() function returns a dictionary which is unordered.
You can sort it according to the number of counts in each element using most_common() function of the Counter object"""

print(Counter(test_list1).most_common())

"""The subtract() Function
The subtract() takes iterable (list) or a mapping (dictionary) as an argument and deducts elements count using that argument.
Check the following example:"""

cnt = Counter({1:3,2:4})
deduct = {1:1, 2:2}
cnt.subtract(deduct)
print(cnt)

"""Output:
Counter({1: 2, 2: 2})"""


"""The defaultdict works exactly like a python dictionary, except for it does not throw KeyError when you try to access a non-existent key.
Instead, it initializes the key with the element of the data type that you pass as an argument at the creation of defaultdict.
The data type is called default_factory."""

from collections import defaultdict

nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])

"""Output:
    0
    """

"""Chain multiples sequences into one sequence object. Returns a chain object which can be converted to list"""""
from itertools import chain
a = "Hello"
b = "World"
c = "People"

d = chain(a, b, c)
print(d)

class Person:
    def __init__(self, id):
        self.id = id

sam = Person(100)
sam.__dict__['age'] = 49
print(sam.age + len(sam.__dict__))

class Demo:
    def __init__(self, age):
        self.age = age

d = Demo(50)
print(d.__dict__)