def is_bijection(a, m):
    seen = set()
    for x in range(1, m):
        val = pow(a, x, m)
        if val in seen:
            return False
        seen.add(val)
    return len(seen) == m - 1


m = 101  # The modulo value
bijective_values = []

for a in range(1, m):
    if is_bijection(a, m):
        bijective_values.append(a)
        

print("The values of 'a' for which 'f_a(x) = a^x mod 101' is bijective are:")
print(bijective_values)
