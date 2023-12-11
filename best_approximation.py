def best_approximation():
    closest_diff = float('inf')  # Initialize with a very large difference
    best_p, best_q = 0, 0       # The best p and q values found

    for q in range(2, 100001):  # Loop over q values
        # Compute possible range for p
        lower_bound = int(1.4 * q)
        upper_bound = int(1.5 * q)

        # Check which p gives the closest approximation
        for p in range(lower_bound, upper_bound + 1):
            diff = abs(p/q - 1.414213)  # Approximated difference from sqrt(2)
            
            if diff < closest_diff:
                closest_diff = diff
                best_p, best_q = p, q

    return best_p, best_q


p, q = best_approximation()
print(f"The best approximation for √2 with q <= 100,000 is {p}/{q} = {p/q:.6f}")
