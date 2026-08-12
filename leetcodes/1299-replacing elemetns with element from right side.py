arr = [17,18,4,5,6,1]
newarr = []
for i in range(len(arr)) : 
    biggest = 0   
    if not i == len(arr) -1 :   
        for j in range(i +1  , len(arr)):
            if arr[j] > biggest : 
                biggest = arr[j] 
        newarr.append(biggest)
    else : 
        newarr.append(-1) 

arr = newarr.copy()

print(arr)


