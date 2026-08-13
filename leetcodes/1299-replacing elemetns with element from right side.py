arr = [17,18,4,5,6,1]
#bruteforce
# newarr = []
# for i in range(len(arr)) : 
#     biggest = 0   
#     if not i == len(arr) -1 :   
#         for j in range(i +1  , len(arr)):
#             if arr[j] > biggest : 
#                 biggest = arr[j] 
#         newarr.append(biggest)
#     else : 
#         newarr.append(-1) 

# arr = newarr

# print(arr)


#optimised hopefully
right_biggest = 0 
for i in reversed(range(len(arr))):
    if i == len(arr) - 1 : 
        right_biggest = arr[i]
        arr[i] = -1 
    else : 
        if right_biggest < arr[i]: 
            temp = arr[i]
            arr[i] = right_biggest
            right_biggest = temp 
        else : 
            arr[i] = right_biggest

print(arr)
