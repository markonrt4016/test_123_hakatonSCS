import numpy as np

# a_3d_array = np.array([[2,4],[10,20]])
#
# print(a_3d_array)

n = 10
koefiicjentUvecanja = 20



matrica = np.random.uniform(5, 10, size=(7,7))


#
# for row in matrica:
#     for col in row:
#         print('vrednost: matrica[{}][{}]'.format(row,col))
#
# print('formirana matrica:')
#
print(matrica)

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(matrica):
  print(idx, x)


print(np.sort(np.random.uniform(5,50,60)).tolist())