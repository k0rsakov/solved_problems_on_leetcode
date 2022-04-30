allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc",'cba']

allowed = set(allowed)
res = 0

for i in words:
    if set(i).issubset(allowed):
        res+=1

print(res)