import itertools

def is_derangement(perm):
    """Check if the permutation is a derangement."""
    return all(perm[i] != i for i in range(len(perm)))

def find_derangements(elements):
    """Find all derangements of the given list of elements."""
    return [perm for perm in itertools.permutations(elements) if is_derangement(perm)]

# List of elements
elements = [0, 1, 2, 3, 4]

# Find and print all derangements
derangements = find_derangements(elements)
for d in derangements:
    print(d)
