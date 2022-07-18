class A:
	def add(self, a, b):
		return (a + b)


a = A()
a.add = lambda x, y: x * y
print(a.add(1, 3))
a.add = 10
a.add(1, 3)
a.b = 10
print(a.b)


def gen(n):
	print('Print before for loop')
	for i in range(1, n):
		print(f'Print before yield:{i}')
		yield i
		print(f'print after yield:{i}')

	print('Print outside the for loop')


n = 11
gen_obj = gen(n)

a = [1,2,3,4,5]
n = 5

b = 'abcba'



for i, v in enumerate(a):
	for j in range(i+1, len(a)):
		if(v + a[j] == 5):
			print(v, a[j])
		else:
			continue


class A:
    def add(self, a, b):
        return (a + b)


a = A()
a.add = lambda x, y: x * y
a.add(1, 3)
a.add = 10
a.add(1, 3)
a.b = 10
print(a.b)
