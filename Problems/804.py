alphabet_morse = {'A': '.-'
    , 'B': '-...'
    , 'C': '-.-.'
    , 'D': '-..'
    , 'E': '.'
    , 'F': '..-.'
    , 'G': '--.'
    , 'H': '....'
    , 'I': '..'
    , 'J': '.---'
    , 'K': '-.-'
    , 'L': '.-..'
    , 'M': '--'
    , 'N': '-.'
    , 'O': '---'
    , 'P': '.--.'
    , 'Q': '--.-'
    , 'R': '.-.'
    , 'S': '...'
    , 'T': '-'
    , 'U': '..-'
    , 'V': '...-'
    , 'W': '.--'
    , 'X': '-..-'
    , 'Y': '-.--'
    , 'Z': '--..'}


# print(alphabet_morse['A'])

words = ["gin","zen","gig","msg"]


res = []
for i in words:
    s = ''
    res_code = []
    for j in i:
        res_code.append(alphabet_morse[j.upper()])
    s = s.join(res_code)
    res.append(s)

print(len(set(res)))