# Define a memoization dictionary to store computed values for efficiency
memo = {0: 0, 1: 1}


# Define the recursive function with memoization
def f(n):
    if n in memo:
        return memo[n]
    
    # Recursively compute the values using the floor division for integer results
    result = f(n // 2) + f(n // 3)
    
    # Store the result in the memoization dictionary
    memo[n] = result
    return result


# Compute f(100000)
result = f(100000)
print(result)
