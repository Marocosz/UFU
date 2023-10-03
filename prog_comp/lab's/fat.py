#!/usr/bin/python3
import sys


def fat(n, i=0):
    x = i * "."
    print(f'{x}fat({n})')
    if n < 2:
        print(f'{x}return 1')
        return 1
    else:
        result = n * fat(n - 1, i + 1)
        print(f'{x}return: {str(result)}')
        return result


if len(sys.argv) > 1:
    operando = int(sys.argv[1])
    print(fat(operando))
