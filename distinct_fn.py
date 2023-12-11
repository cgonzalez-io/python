f = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 0, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11,
     11: 12, 12: 6, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 13}

def find_cycles(f):
    visited = set()
    cycles = []
    
    for start in f:
        if start in visited:
            continue
        
        path = [start]
        while f[path[-1]] not in path:
            path.append(f[path[-1]])
            if path[-1] in visited:
                path = []
                break

        # If a cycle was found
        if path:
            cycle_start = path.index(f[path[-1]])
            cycles.append(path[cycle_start:])
        
        visited.update(path)
    
    return cycles


def distinct_powers(f):
    cycles = find_cycles(f)
    return sum(len(cycle) for cycle in cycles)
print("Number of distinct f^n:", distinct_powers(f))
