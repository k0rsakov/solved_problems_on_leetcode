items = [["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"],["qqqq","qqqq","qqqq"]]
ruleKey = "name"
ruleValue = "qqqq"



# element_index = 0

if ruleKey == 'type':
    element_index = 0
elif ruleKey == 'color':
    element_index = 1
else:
    element_index = 2

# for i in items:
#     if i[element_index] == ruleValue:
#         res = i
#
# print(i)
res = []
for i in range(len(items)):
    if items[i][element_index] == ruleValue:
        res = i

print(res)