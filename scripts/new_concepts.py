import itertools
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


class A:
    def __init__(self, i=0):
        self.i = i
        # pass

    def hello(self):
        print("Hello world")

class B(A):
    def __init__(self, j =0):
        self.j = j

b = B()
print(b.j)
print(b.__dir__())
a = A()
print(b.hello())
print(b.i)

#What will be the output ?
data = [2, 3, 4]
temp = [[x for x in [data]] for x in range(3)]
print(temp)

# Returning class objects

def sequence_class(immutable:bool):
    if immutable:
        cls = tuple
    else:
        cls = list

    return cls

seq = sequence_class(immutable=True)
seq1 = sequence_class(immutable=False)
print(seq('Nivesh'))
print(seq1('Nivesh'))

#Detecting callable objects

def is_even(x):
    return x % 2 == 0

callable(is_even(2))
is_odd = lambda x: x%2 == 1
callable(is_odd(2))
callable(list)

#nonlocal

message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'
    print('Enclosing message:',message)
    local()
    print('Enclosing message:', message)

#print('Global message:', message)
enclosing()
#print('Global message:', message)

#Multiple decorators

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x.encode('unicode-escape').decode('ascii')
    return wrap

class Tracer:
    def __init__(self):
        self.enabled = True
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Tracer()

@tracer
@escape_unicode
def norwegian_island_maker(name):
    return name + 'oy'

#Map with multiple iterables
list(map(lambda x,y,z: x+y+z, [1,2,3],[1,2,3],[1,2,3]))

#Multiple if-clauses comprehensions
values = [x/(x-y) for x in range(100) if x > 50 for y in range(100) if x - y !=0]
#Equivalent for loop code
values = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x - y !=0:
                values.append(x/(x-y))
print(values)


#Decimal module
from decimal import Decimal

#Get size of a Python object
import sys
a = [10,20,30]
print(sys.getsizeof(a))

class A:
    def __init__(self,age):
        self.age = age

a = A(15)
a1 = A(25)

l = [a1,a]
print(l)


class A:
    pass
class B(A):
    pass
class C(A,B):
    def print(self):
        print("Hello")
c = C()
c.print()

# Abstract classes - cannot create an instance of an abstract class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


c = Animal()

# Abstract class example

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()


def f():
    yield 10
    return 20

g = f()
print(next(g))
print(next(g))

#Find 3 largest and smallest numbers in a list

import heapq
test_scores = [51, 88, 22, 67, 99, 100, 87, 75, 100]
print(heapq.nsmallest(3, test_scores))
print(heapq.nlargest(3, test_scores))

#Itertools
for i in itertools.starmap(pow, [(2,5), (3,2), (10,3)]):
    print(i)

for i in itertools.accumulate([2,3,4,5,6], lambda a,b: a*b):
    print(i)



class ABCD:
    def __int__(self):
        self.name = 'Nivesh'

    @staticmethod
    def multiply(a,b):
       print(a*b)

a =ABCD()
ABCD.multiply(2,3)

some_string = 'Python'
some_dict = {}
for i, some_dict[i] in enumerate(some_string):
    i = 10
print(some_dict)

#MultiIndex columns:      use get_level_values()
import pandas as pd

df = pd.DataFrame({
    'name': ['Tom', 'James', 'Allan', 'Chris'],
    'year': ['2000', '2000', '2001', '2001'],
    'math': [67, 80, 75, 50],
    'star': [1, 2, 3, 4]
})
df_grouped = df.groupby('year').agg(
    { 'math': ['mean', 'sum'], 'star': 'sum'}
)

print(df_grouped.columns)
df_grouped.columns = df_grouped.columns.get_level_values(0)
print(df_grouped.columns)

#MultiIndex: FLatten columns use: to_flat_index()

import pandas as pd

df = pd.DataFrame({
    'name': ['Tom', 'James', 'Allan', 'Chris'],
    'year': ['2000', '2000', '2001', '2001'],
    'math': [67, 80, 75, 50],
    'star': [1, 2, 3, 4]
})
df_grouped = df.groupby('year').agg(
    { 'math': ['mean', 'sum'], 'star': 'sum'}
)

df_grouped.columns = df_grouped.columns.to_flat_index()
print(df_grouped.columns)

#MultiIndex: Flatten column: join column labels

import pandas as pd

df = pd.DataFrame({
    'name': ['Tom', 'James', 'Allan', 'Chris'],
    'year': ['2000', '2000', '2001', '2001'],
    'math': [67, 80, 75, 50],
    'star': [1, 2, 3, 4]
})
df_grouped = df.groupby('year').agg(
    { 'math': ['mean', 'sum'], 'star': 'sum'}
)

df_grouped.columns = ['_'.join(col) for col in df_grouped.columns.values]
print(df_grouped.columns)

#MultiIndex: Flatten rows: flatten all levels
#We can simply call reset_index() to flatten every level of the MultiIndex

multi_index = pd.MultiIndex.from_tuples([
  ('Oxford', 'A', '01-01-2022'),
  ('Oxford', 'B', '01-01-2022'),
  ('Oxford', 'A', '02-01-2022'),
  ('Oxford', 'B', '02-01-2022'),
  ('London', 'C', '01-01-2022'),
  ('London', 'D', '01-01-2022'),
  ('London', 'C', '02-01-2022'),
  ('London', 'D', '02-01-2022')],
  names=['Location','Store', 'Date']
)
data = {
  'Num_employee': [1,2,3,4,5,6,7,8],
  'Sales': [11,22,33,44,55,66,77,88]
}
df = pd.DataFrame(data, index=multi_index)
print(df)
print(df.reset_index())

print(df.reset_index(level=0))
print(df.reset_index(level=[1,2]))
print(df.reset_index(['Store','Date']))

#MultiIndex: flatten rows: join row labels

df.index = ['_'.join(col) for col in df.index.values]
print(df)

#Metaclasses

PythonClass = type('PythonClass', (), {'start_date': 'August 2018', 'instructor': 'John Doe'})
PythonClass = type('PythonClass', (DataCamp,), {'start_date': 'August 2018', 'instructor': 'John Doe'})

array = [1,8,15]
gen = (x for x in array if array.count(x) > 0)
# print(list(gen))
array = [2,8,2]
print(list(gen))


import pandas as pd

import numpy as np

ser = {'a' : 1, 'b' : 2, 'c' : 3}

ans = pd.Series(ser)

print(ans)