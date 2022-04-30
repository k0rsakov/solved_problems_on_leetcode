
res = [''] * len(s)
for i in range(len(s)):
    res[indices[i]] = s[i]
con = ''.join(res)

