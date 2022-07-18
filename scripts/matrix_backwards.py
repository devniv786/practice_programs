import numpy as np

arr = np.arange(1, 17).reshape((4, 4))
print(f'Input Array:{arr}')
output_arr = []
for i in range(len(arr)-1, -1, -1):
    # print(arr[i])
    output_arr.extend(arr[i][::-1])
print(f'Output Array: {output_arr}')

# for i in output_arr:
#     print(int(i), end=",")
