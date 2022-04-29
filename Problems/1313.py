# nums = [
#     1 #0
#     ,2#1
#     ,3#2
#     ,4#3
#     ,5#4
#     ,6#5
# ]
# nums = [1,1,2,3,4,7]
nums = [1,2,3,4]
# multi = []
f_slice, s_slice, multi = 0,2,[]

for i in range(0,int(len(nums)/2)):
    empty = []
    # print(nums[f_slice:s_slice])
    n = nums[f_slice:s_slice]
    for i in range(0,n[0]):
        empty.append(n[1])
    multi.append(empty)
    f_slice+=2
    s_slice += 2

concat = []
for i in multi:
    for j in i:
        concat.append(j)


# print(n[0])
print(concat)