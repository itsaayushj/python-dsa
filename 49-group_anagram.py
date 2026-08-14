# medium difficulty 
# for str in strs : 
# from collections import defaultdict
# res = defaultdict(list)

from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
hashmap = defaultdict(list)

for str in strs :
    count = [0] * 26
    for i in str : 
        count[ord(i) - ord("a")] += 1 

    key = tuple(count)
    hashmap[key].append(str)
print(hashmap.values())
