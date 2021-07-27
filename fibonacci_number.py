# Uses python3

import random


def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    table=[]
    for i in range(0, n+1):
      if (i == 0):
          table.insert(i, 0)
      elif (i == 1):
          table.insert(i, 1)
      else:
          table.insert(i, (table[i-1] + table[i-2]))
      i += 1
    return table[n]

# n = int(input())
# print(calc_fib_fast(n))
    
def StressTest(m):
    while True:
        n = random.randint(0, m)
        print(n)
        result1 = calc_fib(n)
        result2 = calc_fib_fast(n)
        if (result1 == result2):
            print('OK', n)
        else:
            print('Wrong answer', result1, result2)
            return
 
StressTest(45)
