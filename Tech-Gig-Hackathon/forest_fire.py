import sys
import os

def find_min_energy_level(N, X, energy_levels):
    energy_levels.sort()
    left = 0
    right = energy_levels[-1]
    min_energy = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        
        for energy in energy_levels:
            if energy > mid:  # Updated condition to strictly greater than mid
                count += 1
        
        if count >= X:
            min_energy = min(min_energy, mid)
            left = mid + 1
        else:
            right = mid - 1
    
    if min_energy == float('inf'):
        return -1
    else:
        return min_energy

if __name__ == '__main__':
    # Read input
    N, X = map(int, sys.stdin.readline().split())
    energy_levels = list(map(int, sys.stdin.readline().split()))

    # Call the function and print the result
    result = find_min_energy_level(N, X, energy_levels)
    print(result)

