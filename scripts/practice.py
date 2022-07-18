def var_args(*args):
    for i in args:
        print(i)

var_args(3,4,5,'Hello')

def ret_mul_values(a,b):
    return a+b, a-b

sum_op, sub_op = ret_mul_values(6,3)
print(sum_op, sub_op)

def name_sal(name, salary=9000):
    print(f'Name={name}')
    print(f'Name={salary}')

name_sal('Nivesh', 50000)
name_sal('Nivesh')

def outer_add(a,b):
    def inner_add():
        c = a + b
        return c
    d = inner_add()
    return (d+5)

s = outer_add(5,3)
print(s)

def rec_add(n):
    if n:
        return n + rec_add(n-1)
    else:
        return 0

s = rec_add(10)
print(s)