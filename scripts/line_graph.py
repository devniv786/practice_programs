# import pandas as pd
# import matplotlib.pyplot as plt
# # df = pd.DataFrame({'Count':[100, 200, 500],'HTTP Response Time':[3500, 3600, 3900],'Processed Time':[3100, 3300, 3500],'Published Time':[4500, 4700, 5100],'Confirmed Time':[5600, 5900, 6500]})
# df = pd.read_excel('Data.xlsx')
# x = list(df['Count'].values)
# y1 = list(df['HTTP Response Time'].values)
# y2 = list(df['Processed Time'].values)
# y3 = list(df['Published Time'].values)
# y4 = list(df['Confirmed Time'].values)
#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.plot(x, y4)
#
# plt.legend(['HTTP Response Time', 'Processed Time', 'Published Time',
#        'Confirmed Time'], loc='upper right')
#
# plt.show()
#
#


# def wrapper(func):
#        def caller(a,b):
#               if(b==0):
#                      raise ZeroDivisionError
#               else:
#                      func(a,b)
#        return caller
#
#
# def divide(a,b):
#        print(a/b)
#
# divide(4,0)


# def print_pairs(arr, N):
#        # hash set
#        hash_set = set()
#
#        for i in range(0, len(arr)):
#               val = N - arr[i]
#               if (val in hash_set):  # check if N-x is there in set, print the pair
#                      print("Pairs " + str(arr[i]) + ", " + str(val))
#               hash_set.add(arr[i])
#
#
# # driver code
# arr = [1, 2, 40, 3, 9, 4]
# N = 3
# print_pairs(arr, N)


# def add_nums(num1, num2):
#    while num2 != 0:
#        data = num1 & num2
#        num1 = num1 ^ num2
#        num2 = data << 1
#    return num1
# print(add_nums(2, 10))
#
#
# class A:
#        def __init__(self, a):
#               self.a = a
#
#        # Overloading ~ operator, but with two operands
#        def __invert__(self, other):
#               return "This is the ~ operator, overloaded as binary operator."
#
#
# ob1 = A(2)
# ob2 = A(3)
#
# print(ob1~ob2)


class A:
       def __init__(self):
	          self.__x = 1
class B(A):
       def display(self):
              print(self.__x)
def main():
       obj = B()
       obj1 = A()
       print(obj1.__x)
       obj.display()
main()

# values = ["823", "863"]
# num = values[0][0:]
# for row in range(0,len(values)):
#     for column in range(0, len(values[row])):
#         if num > values[row][column:]:
#             num = values[row][column:]
# print(num)


# def function(string,list1):
#     #line1
#     while(num!=len(string)):
#         if len(string)%2==0 or (string[num] in ('a','e','i','o','u')):
#             list1.append(string[num])
#         #line2
#         #line3
#         break
#     return list1
# print(function("Epoch",[]))


# class A:
# 	def __init__(self,x=3):
# 		self.__x = x
# class B(A):
# 	def __init__(self):
# 		super().__init__(5)
# 	def display(self):
# 		print(self._A__x)
# def main():
# 	obj = B()
# 	obj.display()
# main()


# class Test:
# 	def __init__(self):
# 		self.x = 0
#
# class Derived_Test(Test):
#        def __init__(self):
#               #super().__init__(5)
#               self.y = 4
#
# def main():
# 	b = Derived_Test()
# 	print(b.x,b.y)
#
# main()


# class Demo:
# 	def __init__(self):
# 		self.x = 1
# 	def change(self):
# 		self.x = 10
# class Demo_derived(Demo):
# 	def change(self):
# 		self.x=self.x+1
# 		return self.x
# def main():
# 	obj = Demo_derived()
# 	print(obj.change())
# main()


# def fun(n):
# 	stack = Stack(100)
# 	while (n > 0):
# 		stack.push(n%10)
# 		n =int (n/10)
# 	result=0
# 	while (not stack.is_empty()):
# 		result+=stack.pop()
# 	return result


# class InvalidSkillException(Exception):
#     pass
# class Educator:
#     total_allocations=101
#     def __init__(self,skill):
#         self.__skill=skill
#     def validate_skill(self,skill_required):
#         if(skill_required == self.__skill):
#             Educator.total_allocations+=1
#             return True
#         else:
#             raise InvalidSkillException
# class ClassRoom:
#     def __init__(self,educator):
#         self.__educator=educator
#         self.class_room_no=None
#     def allocate_educator(self,skill_required,class_room_no):
#         try:
#             if(self.__educator.validate_skill(skill_required)):
#                 self.class_room_no=class_room_no
#         except Exception:
#             print("Something wrong")
#         except InvalidSkillException:
#             Educator.total_allocations-=1
#             print("Invalid Skill")
# edu = Educator("Java")
# class_room1 = ClassRoom(edu)
# class_room1.allocate_educator("Java","L2-73")
# class_room2 = ClassRoom(edu)
# class_room2.allocate_educator("C++","L1-75")
# print(class_room1.class_room_no,class_room2.class_room_no)
# print(Educator.total_allocations)


# class class1:
# 	def __init__():
# 		print("class1's __init__")
# class class2(class1):
# 	def __init__():
# 		print("class2's __init__")
# ob=class2()


# class test:
# 	def __init__(self):
# 		print("Hello World")
# 	def __init__(self):
# 		print ("Bye World")
# obj=test()
#
#
# int = 1
# def randommethod():
# 	global int
# 	for i in (1, 2, 3):
# 		int += 1
# randommethod()
# print(int)
#
# def f(x):
# 	def f1(*args, **kwargs):
# 		print("*" * 5)
# 		x(*args, **kwargs)
# 		print("*" * 5)
# 	return f1
# @f
# def p(m):
# 	print('Got:', m)
# print("hello")
#
# p(2)


# class A:
# 	def test(self):
# 		print("test of A called")
# class B(A):
# 	def test(self):
# 		print("test of B called")
# 		super().test()
# class C(A):
# 	def test(self):
# 		print("test of C called")
# 		super().test()
# class D(B,C):
# 	def test2(self):
# 		print("test of D called")
# obj=D()
# obj.test()
#
#
# def func():
#        a = 10
#        def func1():
#               b = 10
#        return func1

#
# class InvalidLengthException(Exception):
#     pass
# class Mobile:
#     def __init__(self,mob_no):
#         self.__mob_no=mob_no
#     def validate_mobile_number(self):
#         try:
#             if(len(self.__mob_no)!=10):
#                 raise InvalidLengthException
#             else:
#                 print("Valid Mobile Number")
#         except InvalidLengthException:
#             print("Invalid Length - inside class")
#         print("Inside the class")
# mob = Mobile("987665")
# try:
#     mob.validate_mobile_number()
#     print("Outside the class")
# except InvalidLengthException:
#     print("Invalid Length - outside class")


# class stud:
#   def __init__(self, roll_no, grade):
#     self.roll_no = roll_no
#     self.grade = grade
#   def display (self):
#     print("Roll no : ", self.roll_no, ", Grade: ", self.grade)
#     stud1 = stud(28, ‘acode’)
# stud1.age=24
# print(hasattr(stud1, 'age'))

# dicts = dict()
# for l in enumerate(range(2)):
#     dicts[l[0]] = l[1]
#     dicts[l[1]+7] = l[0]
# print(dicts)

# L1 = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True]
# val1, val2 = 0, ''
# for x in L1:
#     if(type(x) == int or type(x) == float):
# 	    val1 += x
#     elif(type(x) == str):
# 	    val2 += x
#     else:
# 	    break
# print(val1, val2)
#
# sum(1,2,3)


class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)