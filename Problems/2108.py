words=["def","ghi"]
for i in words:
    r=''
    r=r.join(list(reversed(i)))
    if i == r:
        print(i)
        break
