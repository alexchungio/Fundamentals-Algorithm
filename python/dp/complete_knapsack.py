
from typing import List


def complete_knapsack_with_recursion(capacity: int, weights: List[int], values: List[int]):
    """
     Solve the complete Knapsack problem using top-down recursion with memoization.
    Args:
        capacity: Maximum capacity of the knapsack.
        weights: Weight of each item.
        values: Weight of each item.

    Returns:

    """
    n = len(weights)
    memo = {}

    def dfs(i: int, cap: int) -> int:
        """
        Returns the maximum value obtainable using items
        from index i to n-1 with remaining capacity cap.
        """
        # No items left or no remaining capacity.
        if i == n or cap == 0:
            return 0
        # return the cached result if the state has been visited.
        if (i, cap) in memo:
            return memo[(i, cap)]

        # Option 1: Skip the current item.
        res = dfs(i+1, cap)

        # Option 2: Take the current item if it fits.
        if weights[i] <= cap:
            res = max(res, dfs(i, cap - weights[i]) + values[i])

        memo[(i, cap)] = res

        return res

    return dfs(0, capacity)


def complete_knapsack_with_2d(capacity: int, weights: List[int], values: List[int]):
    """
    Solve the complete Knapsack problem using bottom-up dynamic programming.

    dp[i][c] denotes the maximum value achievable
    using the first i items with capacity c.
    """
    n = len(weights)

    # dp[i][c] -> dp[i][c] denotes the maximum value for the first i items (0..i-1) under capacity c

    # initial dp table
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for i in range(n):
        w = weights[i]
        v = values[i]
        for c in range(1, capacity+1):
            #  Current item cannot fit into the knapsack.
            if c < w:
                dp[i+1][c] = dp[i][c]
            else:
                # Choose the better of:
                # 1. Skip the current item.
                # 2. Take the current item.
                dp[i+1][c] = max(dp[i][c], dp[i+1][c-w] + v)

    return dp[n][capacity]


def complete_knapsack_with_1d(capacity: int, weights: List[int], values: List[int]):
    """
    Solve the complete Knapsack problem using one-dimensional dynamic programming.

    dp[c] denotes the maximum value achievablewith knapsack capacity c.
    """

    n = len(weights)

    # # Initialize DP array.
    dp = [0 for _ in range(capacity + 1)]

    for i in range(n):
        w = weights[i]
        v = values[i]
        # Traverse capacities in forward order so that
        # the current item can be selected multiple times.
        for c in range(w, capacity+1):
            # dp equation
            # if c < w:
            #     p[i + 1][c] = dp[i][c]
            #     # remove i -> d[c] = dp[c]
            dp[c] = max(dp[c], dp[c-w]+v)

    return dp[capacity]


if __name__ == "__main__":
    capacity = 10
    weights = [2, 3, 5]
    values = [4, 5, 10]

    res_recursion = complete_knapsack_with_recursion(
        capacity, weights, values
    )
    res_2d = complete_knapsack_with_2d(
        capacity, weights, values
    )
    res_1d = complete_knapsack_with_1d(
        capacity, weights, values
    )

    print(f"Recursion + Memoization : {res_recursion}")
    print(f"2D Dynamic Programming : {res_2d}")
    print(f"1D Dynamic Programming : {res_1d}")



