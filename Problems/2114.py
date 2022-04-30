sentences = ["please wait", "continue to fight", "continue to win"]

max = 0
for i in sentences:
    a = len(i.split(' '))
    if a > max:
        max = a

print(max)

# a = len(sentences[2].split(' '))

# print(len(sentences[2].split(' ')))
