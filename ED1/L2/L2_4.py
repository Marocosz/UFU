def pg(n, r, t1):
    if n == 1:
        return t1
    else:
        return r * pg(n - 1, r, t1)

def pg_list(n, r, t1):
    if n <= 0:
        return []
    else:
        termo_atual = pg(n, r, t1)
        return pg_list(n - 1, r, t1) + [termo_atual]


print(pg_list(5, 4, 4))