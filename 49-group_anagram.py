# medium difficulty 
# for str in strs : 
# from collections import defaultdict
# res = defaultdict(list)

# from collections import defaultdict
# strs = ["eat","tea","tan","ate","nat","bat"]
# hashmap = defaultdict(list)

# for str in strs :
#     count = [0] * 26
#     for i in str : 
#         count[ord(i) - ord("a")] += 1 

#     key = tuple(count)
#     hashmap[key].append(str)
# print(hashmap.values())

strs = ["eat","tea","tan","ate","nat","bat"]
from collections import defaultdict
hashmap = defaultdict(list)
for str in strs : 
    count_key = [0] * 26 # 26 as in 26 words in alphabet , we will do +1 on 0 if the word is inside str...it will be used as key later in dictionary 
    for i in str : 
        count_key[ord(i) - ord("a")] += 1 
    count_key = tuple(count_key)
    hashmap[count_key].append(str)

print(hashmap.values())



