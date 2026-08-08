nums = [0,0,1,1,1,2,2,3,3,4]
write = 0 
read = 1 
def ImagineThisIsAFunction():
    if len(nums) == 0 : 
        return 0 
    
    while read < len(nums):
        if nums[read] == nums[write]:
            read += 1 
            
        else:
            write += 1
            nums[read] , nums[write] = nums[write] , nums[read]
            read += 1
    return write + 1
        
    

