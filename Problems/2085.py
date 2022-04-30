# words2 = ["leetcode","is","amazing","as","is"]
# words1 = ["amazing","leetcode","is"]

# words1 = ["b","bb","bbb"]
# words2 = ["a","aa","aaa"]
# #
# words1 = ["a","ab"]
# words2 = ["a","a","a","ab"]

words1 = ["ibxyatvglhltxngewrcrqbbnew","towokpjpkccmob","kdmtwngzpebwpnvlazhdcmtwpjh","muh","fzzlmacbbvoqdueutjqoutwd","ylluspdftxxqbwadivfdzulghq","hioiacezaiptpsvcojzckhxz","nzcjhjomaupevyekennyrfwyd","tdwtuinstwsfyjnfkxkbnsptisuifo","wrdwoxzsczzlnwjugopohxh","p","jkez","drisymx","fsva","myqc","aovjoxzpkylpecltwtottzidq","wqspbhpberqjabockesc","f","qostobxgfliil","gsekmhjpuedeivioudx","tzelzowtgnvjsxgbw","zgmpazgnioprk","fucybddarjcve","ldacfviysy","yxyjairoxtvbkljaokca","vxpiohhvjuwcpiceafcdzobalgpz","wyflbpmkfwftndgtnftajgla","xbxvvk","bnrwyshimjamltmlugeiviu","wsgqysmuakedrrmjk","ppqmgibqljkwgmiwi","fly","uf","tvvttzrsjbojve","ztxtnmljdhyz","vxonvloufeksfvg","wql","kotdenqjrdlgofubocb","wlaqceczd","mtmhtgvqwr","aymzxpfvbqxydmilafyqvapuxtnqe","ig","atetjlhdcigunmmit","enkdcxqnw","gtlcmkxwvdhumgfurxkesmekmnhjo","hurihasxncgtzleerslvwxkz","zked","xiaqvclhuhggcgoouzjgi","mzejuubgyhvlfbecpmggddby","boyotuukuiprtlvktypxboosw","vwfceei","gopsxsihawzhtlmdyiggljzggrhqr","bckuuqszgncdhkeghudflczm","e","yvhwysrunkxsppbqjf","lo","bze","kuzoqvgugnrpfkelktfg","ntjtlwwmuevtsqujpxswgx","zkdwtpdlvrfkbyktqsellmghaxj","u","rpmpq","ajhlzwfrbysqloduofr","gyfmhcskcrjepgeplbbj","fe","zyolvtetrdffy","apbkyczsuvde","fnkqf","qwwxpwbr","krkbnww","zkvqkugfpziawiokdzlpjomfarkor","jg","l","srbvxsnuhyqzmycvavmmakh","dhkgzjrstir","smaaptkzpwhukebwboysbnawgzgot"]
words2 = ["p","towokpjpkccmob","vflbjyecpzxnuay","fzas","fzzlmacbbvoqdueutjqoutwd","bwjjzw","va","manrvuldjzrdnwihzct","tdwtuinstwsfyjnfkxkbnsptisuifo","wrdwoxzsczzlnwjugopohxh","p","tylcyihdjruhaayzcwxrynnkch","uojzddpgyvqslha","fsva","rucvbjzfewjlhddxefhf","tfihr","wqspbhpberqjabockesc","f","bmfo","zsjbzjmbloaybdofsrqvzwoizz","tzelzowtgnvjsxgbw","tproznqma","lmryjiyvkgsxsaylkdmmxeub","ldacfviysy","xpamoswlugwjxyny","rmfvgm","wm","xbxvvk","ubawz","jbrabb","rgegpb","fly","aofydpklgjqmxhvxuhq","tvvttzrsjbojve","wj","vxonvloufeksfvg","wql","vu","nhuxqdfyftrbbodztyydb","mtmhtgvqwr","aymzxpfvbqxydmilafyqvapuxtnqe","fqksatpfo","ylzkfvvzdsryl","enkdcxqnw","gtlcmkxwvdhumgfurxkesmekmnhjo","nccwybkxuawwdqyhrhmbt","zked","eyzwtvsjt","qy","boyotuukuiprtlvktypxboosw"]

common = list(set(words1).intersection(set(words2)))

print(common)
print(len(common))

len1 = len(words1)
len2 = len(words2)

# print(f'len1={len1} len2={len2}')
min_len = min(len1,len2)

counter = 0
dict_check = []

if min_len == len1:
    for i in range(0, len(words1)):
        if words2.count(words1[i]) == 1:
            counter += 1
            dict_check.append(words1[i])
        # print(f'words1[{i}]={words1[i]} _|_ counter_in={words2.count(words1[i])}')
else:
    for i in range(0, len(words2)):
        if words1.count(words2[i]) == 1:
            counter += 1
            dict_check.append(words2[i])
        # print(f'words2[{i}]={words2[i]} _|_ counter_in={words1.count(words2[i])}')

print(counter)
