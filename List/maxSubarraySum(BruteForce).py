def max_subarray_sum_brute_force(arr):
    n = len(arr)
    max_sum = float("-inf")

    # Iterate over all possible subarray starting points
    for i in range(n):
        # Iterate over all possible subarray ending points
        for j in range(i, n):
            # Calculate the sum of the subarray from i to j
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += arr[k]
            # Update max_sum if the current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum is:", max_subarray_sum_brute_force(arr))
