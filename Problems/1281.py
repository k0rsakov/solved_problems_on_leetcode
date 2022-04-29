n = 4421

arr = list(map(int,str(n)))
multi, add = 1,0
for i in arr:
    multi*=i
for i in arr:
    add+=i

res = multi-add

print(multi,add,res)
