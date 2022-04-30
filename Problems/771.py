jewels = "aA"
stones = "aAAbbbb"
common = list(set(jewels).intersection(set(stones)))
counter = 0
for i in common:
    if stones.count(i) > 0:
        counter += stones.count(i)
print(counter)