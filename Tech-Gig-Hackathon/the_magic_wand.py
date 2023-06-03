#!/bin/python3

import os
import sys
def calculate_costs(arr, queries):
    costs = []
    for query in queries:
        total_cost = sum(abs(num - query) for num in arr)
        costs.append(total_cost)
    return costs

# Read input values
N, M = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

# Call the function to calculate the costs
costs = calculate_costs(arr, queries)

# Print the costs
print(*costs)
B
B
B
B
B
B
B
B
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A

