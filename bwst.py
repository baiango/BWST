def duval(text):
    current_factor_i = 0
    lyndon_factors = []
    while current_factor_i < len(text):
        scan_i = current_factor_i + 1
        candidate_start = current_factor_i
        while scan_i < len(text) and text[candidate_start] <= text[scan_i]:
            if text[candidate_start] < text[scan_i]:
                candidate_start = current_factor_i
            else:
                candidate_start += 1
            scan_i += 1
        while current_factor_i <= candidate_start:
            lyndon_factors.append(text[current_factor_i:current_factor_i + scan_i - candidate_start])
            current_factor_i += scan_i - candidate_start
    return lyndon_factors

def bwst(text):
    rotations = []
    for text in duval(text):
        for i in range(len(text)):
            rotations.append(text[-i:] + text[:-i])
    return [x[-1] for x in sorted(rotations)]

def ibwst(text):
    sorted_text = sorted(text)
    count = []
    start = []
    for i, x in enumerate(text):
        count.append(start.count(sorted_text.index(x)) if sorted_text.index(x) in start else 0)
        start.append(sorted_text.index(x))

    positions = [x + y for x, y in zip(start, count)]
    map_ = [positions.index(i) for i, _ in enumerate(positions)]

    visited = [False] * len(text)
    restored = []
    while not all(visited):
        collect = []
        init_index = visited.index(False)
        index = init_index
        first_equal = True
        while index != init_index or first_equal:
            first_equal = False
            visited[index] = True
            collect.append(sorted_text[index])
            index = map_[index]
        restored.append(collect)

    reconstructed = []
    for x in sorted(restored, reverse=True):
        reconstructed.extend(x)

    return reconstructed

print(duval("FOOBAR2000"))
print(duval("duck cement biology"))
a = bwst("duck cement biology")
print("".join(a))
a = ibwst(a)
print("".join(a))

text = 'From that day on, Eeryn was known as the hero of Eery, ' \
	+ 'a tale passed down through generations. ' \
	+ 'And in the heart of the village, the Erezanne continued to shine brightly, ' \
	+ 'a symbol of hope and the enduring spirit of Eeryn and her beloved village.'
a = bwst(text)
print(duval(text))
print("".join(a))
a = ibwst(a)
print("".join(a))
