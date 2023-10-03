def pg(n, r, t1):
    if n == 1:
        return t1
    else:
        return pg(n-1, r, t1) * r


print(pg(5, 4, 4))