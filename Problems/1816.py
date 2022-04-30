s = "Hello how are you Contestant"
k = 4



s_res = []
a = ''
s_split = s.split(' ')
for i in range(0,k):
    s_res.append(s_split[i])

a = ' '.join(s_res)
print(a)