#O(n)
# time complexity
for i in range(1 , n+1):
    print(i)
# space complexity 
array = [1 , 2 , 3 , 4]
new_array = []
for i in range(len(array)):
    new_array.append(array[i] * array[i])

#O(n²)
# time 
for i in range (1 , n+1):
    for j in range(i , n+1):
        print(i ,j)
# space complexity
new_array = []
array = [1 , 2 , 3 , 4]
for i in range (1 , n+1):
    for j in range(i , n+1):
        new_array.append((i ,j))

#O(1)
# time 
print("Hello")
#space
array = [1 ,2 ,3 ,4]
for i in range(len(array)):
    array[i] = array[i] * array[i]
