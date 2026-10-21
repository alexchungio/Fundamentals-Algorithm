"""
n 个 硬币， 总的面值式m , 硬币面值 1， 2， 5， 10， 输出硬币的组合方式总数
"""


def backpack(nums, amounts, coins):
    """

    Args:
        nums:
        amounts:
        coins:

    Returns:

    """
    # dp[k][j] += dp[k-1][j-c]

    dp = [[0] * (amounts + 1) for _ in range(nums + 1)]
    dp[0][0] = 1

    for c in coins:
        for k in range(1, nums + 1):
            for j in range(c, amounts + 1):
                dp[k][j] += dp[k - 1][j - c]

    return dp[nums][amounts]


if __name__ == "__main__":
    n = 3
    m = 12
    coints = [1, 2, 5, 10]
    ans = backpack(3, 12, coints)
    print(ans)