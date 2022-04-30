# nums = [
#     1 #0
#     ,2 #1
#     ,3 #2
#     ,1 #3
#     ,1 #4
#     ,3 #5
# ]

nums = [1,1,1,1]

''' There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed. '''

counter, move = 0, 0
while move < len(nums):
    for i in range(move,len(nums)-1):
        if nums[move] == nums[i+1]:
            counter+=1
    move+=1
print(counter)