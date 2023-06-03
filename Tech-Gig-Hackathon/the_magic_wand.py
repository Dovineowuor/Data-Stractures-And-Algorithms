#!/bin/python3
import os
import sys

def calculate_min_cost(N, M, arr, queries):
    arr.sort()  # Sort the array in ascending order

    prefix_sum = [0] * (N + 1)  # Prefix sum array
    cost = []  # List to store the minimum cost for each query

    # Calculate prefix sum of the sorted array
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    for query in queries:
        # Find the index where the value becomes equal to or greater than the query
        index = binary_search(arr, query)

        # Calculate the minimum cost for the current query
        left_sum = prefix_sum[index]  # Sum of elements to the left of the index
        right_sum = prefix_sum[N] - prefix_sum[index]  # Sum of elements to the right of the index
        left_count = index  # Number of elements to the left of the index
        right_count = N - index  # Number of elements to the right of the index
        min_cost = (left_count * query - left_sum) + (right_sum - right_count * query)

        cost.append(min_cost)  # Append minimum cost to the list

    return cost


def binary_search(arr, query):
    # Binary search to find the index where the value becomes equal to or greater than the query
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == query:
            return mid
        elif arr[mid] < query:
            low = mid + 1
        else:
            high = mid - 1

    return low


if __name__ == "__main__":
    # Read input from STDIN
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    # Calculate the minimum cost for each query
    min_cost_list = calculate_min_cost(N, M, arr, queries)

    # Print the minimum cost for each query
    print(*min_cost_list)

