import random

with open("data.txt", "r") as f:
    arrays = [line.split() for line in f]

array1 = arrays[0]
array2 = arrays[1]
array3 = arrays[2]

new_array = []
for i in range(len(array1)):
    new_array.append(f'"{array1[i]}", "{array2[i]}", "{array3[i]}"')

random.shuffle(new_array)

result = "\n".join(new_array)
print(result)
