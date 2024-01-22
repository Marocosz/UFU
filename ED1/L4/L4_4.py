L = [0]
L1 = L*3

print(L)  # [0]
print(L1)  # [0, 0, 0]

print('--------------------')

# L[0] = -2

print(L)  # [-2]
print(L1)  # [0, 0, 0]

print(id(L[0]))
print(id(L1[1]))
