rings = "B9" \
        "R9" \
        "G0" \
        "R4" \
        "G6" \
        "R8" \
        "R2" \
        "R9" \
        "G9"





options = [{"color": rings[i], "rod": rings[i+1]} for i in range(0,len(rings),2)]
rod = list(set([rings[i] for i in range(1,len(rings),2)]))
counter = 0
for i in rod:
    a = []
    if rings.count(i) >= 3:
        for j in options:
            if j['rod'] == i:
                a.append(j['color'])
        a = ''.join(a)
        if 'R' in a and 'G' in a and 'B' in a:
            counter+=1

print(counter)
