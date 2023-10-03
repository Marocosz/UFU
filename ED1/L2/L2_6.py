def somatorio(n):
    if n == 1:
        return 1
    else:
        return n + somatorio(n-1)
    

print(somatorio(10))