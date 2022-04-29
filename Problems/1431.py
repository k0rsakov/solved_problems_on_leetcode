candies = [2,3,5,1,3]
extraCandies = 3

max_candies = max(candies)
log_result = []

for i in candies:
    print(i+extraCandies)
    if i+extraCandies>=max_candies:
        log_result.append('true')
    else:
        log_result.append('false')

# print(bool(True))
print(log_result)
