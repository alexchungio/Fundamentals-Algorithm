import sys

# 描述从第一个跳到最后一个， 每一步至少跳一格， 每个数的值表示这个位置可以跳跃的最大长度，计算如何以最少的跳跃次数跳到最后一个数

# 解决思路: 贪心算法，广度遍历(BFS), 动态规划
# https://www.jianshu.com/p/1c3ba23a522e
# leetcode 45


def greedy_calculate_step(lyst):
    """
    在不得不跳时再跳
    :param lyst:
    :return:
    """
    if not len(lyst) or len(lyst) < 0:
        return 0

    cur_max = 0  # 当前所能到达的最远坐标
    next_max = 0  # 上一位置能够跳到的最远坐标

    step = 0
    for i in range(len(lyst)):
        next_max = max(lyst[i] + i, next_max)
        if next_max >= len(lyst) - 1:
            return step + 1
        if i == cur_max:
            step += 1
            cur_max = next_max


if __name__ == "__main__":

    # while True:
    #     try:
    #         num = int(input())
    #         lyst = []
    #         for i in range(num):
    #             lyst.append(int(input()))
    #         min_step = calculate_step(lyst)
    #         print(min_step)
    #     except Exception as e:
    #         break

    lyst = [2, 3, 1, 1, 4]
    print(greedy_calculate_step(lyst))


