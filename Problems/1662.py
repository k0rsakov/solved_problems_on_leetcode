word1 = ["ab", "c"]
word2 = ["a", "bc"]

s1,s2 = '',''

for i in word1:
    s1+=i
for i in word2:
    s2+=i
print(s1==s2)