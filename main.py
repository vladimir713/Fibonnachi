#!/usr/bin/env python3
#----------------------------------------------------------------
# Вычисление ряда четных чисел Фибоначи тремя разными способами
#-----------------------------------------------------------------

def f(n):
	a = [0, 1]
	for i in range(2, 3*n):
		a.append(a[i-2]+a[i-1])
	return 	[i for i in a if i%2 == 0]

def f2(n):
	a, b = 0, 1
	for __ in range(n):
		yield a
		a,b = b, a+b

def f3(n):
	fib = [0]
	a, b = 0, 1
	def ff(n, a, b):
		a, b = b, a + b
		fib.append(a)
		if n:
			ff(n-1, a, b)		
	ff(n*3-2, a, b)
	return [i for i in fib if i%2 == 0]

items = 8 #Количество выводимых четных значений

print (f(items))
print ([i for i in list(f2(items*3)) if not(i%2)])
print(f3(items))