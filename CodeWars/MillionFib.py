import ipdb

'''
Solution to:

https://www.codewars.com/kata/53d40c1e2f13e331fc000c26


fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)


Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n) 
if you already know fib(n + 1) and fib(n + 2)? Use this to reason what value 
fib has to have for negative values.


fib(n + 2) = fib(n + 1) + fib(n)

fib(n) = fib(n + 2) - fib(n + 1)

specific case ...

    fib(1) must equal fib(0) + fib(-1), implying
    1 = 0 + fib(-1), and thus fib(-1) = 1


    fib(0) = fib(-1) + fib(-2)
    0 = 1 + fib(-2), thus fib(-2) = -1


    fib(-1) = fib(-2) + fib(-3)
    1 = -1







'''


def fib(n):
    return fib_iter(a = 1, b = 0, p = 0, q = 1, times = n)


def fib_iter(a, b, p, q, times):
    '''Doesn't seem that p' = q and q' = p + q
    '''

    if times == 0:
        return b
    elif times % 2 == 0:
        return fib_iter(a, b, q, q + p, times / 2)
    return fib_iter(q * (a + b) + (p * a), b * p  + a *q, p, q, times - 1)




if __name__ == "__main__":

    ipdb.set_trace()