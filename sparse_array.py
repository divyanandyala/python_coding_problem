strings = ["aba", "baba", "aba", "xz"]
queries = ["aba", "xz", "ab"]

result = []

for q in queries:
    count = 0

    for s in strings:
        if q == s:
            count += 1

    result.append(count)

print(result)