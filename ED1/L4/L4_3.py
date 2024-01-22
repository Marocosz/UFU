import copy

L1 = [['c','d'],'a']

L2 = copy.deepcopy(L1)  # Independentes uma da outra

print(L1)  # ['c', 'd'], 'a']
print(L2)  # ['c', 'd'], 'a']

print('-------------------')

L1[1] = 'z'

print(L1)  # [['c', 'd'], 'z']
print(L2)  # [['c', 'd'], 'a']

print('-------------------')

L2[0][1] = 'y'

print(L1)  # [['c', 'd'], 'z']
print(L2)  # [['c', 'y'], 'a']
