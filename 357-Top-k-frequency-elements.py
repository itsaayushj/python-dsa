nums = [1, 1, 1, 2, 2, 3]
hashmap = {}
k = 2 
for i in nums : 
    if i in hashmap : 
        hashmap[i] += 1 
    else : 
        hashmap[i] = 1 

for key , value in hashmap.items(): 
    print(key , ":" , value)

valuelist = list(hashmap.values())
print(valuelist)
valuelist.sort(reverse=True)
print(valuelist)
answer_values = valuelist[:k]
answer_keys = []
for i in answer_values : 
    for key in hashmap.keys():
        if hashmap[key] == i and key not in answer_keys: 
            answer_keys.append(key)
        if len(answer_keys) == k : 
            break 
    if len(answer_keys) == k : 
        break 
print(answer_keys)