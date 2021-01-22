import numpy
import multiprocessing as mp

#calculate and print the factorization of each number
def imprimir(number):

    a = []
    i = 2
    j = 0

    print(number,"= ",end="")

    while number > 1:
        if (number % i == 0):
            number = number / i
            a.append(i)
            j += 1
            i = 2
        else:
            i += 1

    for x in range(j):
        if(x == 0):
            print(a[x], end="")
        else:
            print(" * ", a[x], end="")
    print()

#calculates fibonacci recursively
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2) 


#threads are created with the number of threads of the cpu
thread = mp.Pool(mp.cpu_count())
n = 0
#number by number is given to calculate the fibonacci and then factor
while (n < 301):

  number = thread.apply(fib,[n])
  print(n,": ",end="")

  imprimir(number)
  n +=1

p.close()