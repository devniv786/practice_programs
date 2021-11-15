import numpy as np
li = np.arange(1, 21).reshape(4, 5)
print(li)
output_list = []
max_elements_list = max([len(l) for l in li])
print(max_elements_list)

for i in range(0, max_elements_list):
    temp_list = []
    for j in range(0, len(li)):
        temp_list.append(li[j][i])
    if i % 2 == 0:
        output_list.extend(temp_list)
    else:
        output_list.extend(list(reversed(temp_list)))
print(output_list)
