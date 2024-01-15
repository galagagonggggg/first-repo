import numpy
x = input().split()
dimension = [int(element) for element in x]
#print(dimension)
original_array = []
for _ in range(dimension[0]):
    original_array.append([int(j) for j in input().split()])
transform_array = my_array = numpy.array(original_array)
print(numpy.transpose(transform_array))
print(transform_array.flatten())