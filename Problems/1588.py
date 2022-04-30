arr = [10,11,12]

steps = [i for i in range(1,len(arr)+1,2)]
res = 0
for i in steps:
    for j in range(len(arr)):
        a = arr[j:j+i]
        if len(a) % 2 == 1 and len(a) == i:
            res += sum(a)
print(res)