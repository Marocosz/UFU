dic1 = {'a': [1, 2], 'b': 2, 'c': 3}

if 'a' in dic1:
    a = dic1.get('a')
    print(a)
else:
    print('não existe')