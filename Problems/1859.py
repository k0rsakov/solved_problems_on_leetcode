s = "is2 sentence4 This1 a3"

ss = s.split(' ')
res = ['']*len(ss)

for i in ss:
    res[(int(i[-1])-1)]=i[0:-1]


str1 = ' '.join(res)
print(str1)


