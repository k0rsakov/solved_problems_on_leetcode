sentence = "thequickbrownfoxjumpsoverthelazydog"

s = list(set(sentence))
s.sort()

a = [chr(i) for i in range(97,123)]
if a == s:
    print(True)
else:
    print(False)