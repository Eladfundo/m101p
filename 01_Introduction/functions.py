f = ['a', 'p', 'b', 'p', 'b', 'k', 'b']


def count_fruits(l):
    counts = {}
    for i in l:
        if i in counts:
            counts[i] = counts[i] + 1
        else:
            counts[i] = 1
    return counts

counts = count_fruits(f)

print counts