n = 4
start = 3

nums = [start + n * 2 for n in range(n)]
ans = 0
for i in nums:
    ans = ans ^ i
