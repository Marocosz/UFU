#!/usr/bin/python3
import sys


def fib(n, i=0):
    x = "." * i
    print(f'{x}fib({n})')
    if n <= 2:
        print(f'{x}return: 1')
        return 1
    else:
        res = fib(n - 1, i + 1) + fib(n - 2, i + 1)
        print(f'{x}return: {res}')
        return res


if len(sys.argv) > 1:
    operando = int(sys.argv[1])
    print(fib(operando))
