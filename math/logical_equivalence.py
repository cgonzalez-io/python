def implies(p, q):
    return not p or q

# Print header


print("a | b | c | d | (a → b) → (c → d) | (a → (b → c)) → d | Different")
print("---------------------------------------------------------")

for a in [True, False]:
    for b in [True, False]:
        for c in [True, False]:
            for d in [True, False]:
                # Calculate values for the statements
                stmt1 = implies(implies(a, b), implies(c, d))
                stmt2 = implies(implies(a, implies(b, c)), d)
                
                # Check if values are different
                different = "Yes" if stmt1 != stmt2 else "No"
                
                # Print row
                print(f"{int(a)} | {int(b)} | {int(c)} | {int(d)} | {int(stmt1)} | {int(stmt2)} | {different}")
