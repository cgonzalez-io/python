import itertools


def check_for_reflexive(R):
    for x in range(1, 5):
        if (x, x) in R:  # check if R is reflexive
            return False
        for y in range(1, 5):
            for z in range(1, 5):
                if (x, y) in R and (y, z) in R and (x, z) not in R:  # check if R is transitive
                    return False
    return True


S = {1, 2, 3, 4}
count = 0

for subset in itertools.chain.from_iterable(itertools.combinations(S, r) for r in range(len(S) + 1)):
    R = {(x, y) for x in subset for y in subset if x != y}
    if check_for_reflexive(R):
        count += 1

print("Number of transitive but not reflexive relations on S:", count)
