# -*- coding: utf-8 -*-
"""
计算自由落体多次反弹的高度、经过的总距离和运动时间
假设重力加速度 g = 9.8 m/s^2
"""


def bouncing_ball(n, h0=100, g=9.8):
    """
    计算第 n 次反弹后的最高高度、总运动距离和运动时间
    :param n: 反弹次数
    :param h0: 初始高度（默认100米）
    :param g: 重力加速度（默认9.8 m/s^2）
    :return: (反弹高度, 总经过的距离, 总运动时间)
    """
    height = h0 * (0.5 ** n)  # 计算第 n 次反弹的高度

    # 计算总经过的距离
    total_distance = h0  # 第一次下落的距离
    for i in range(1, n + 1):
        total_distance += 2 * (h0 * (0.5 ** i))  # 每次反弹上升和下降的距离

    # 计算总运动时间
    time = (2 * (2 ** 0.5 - 1) * (h0 / g) ** 0.5)  # 第一次运动的时间
    for i in range(1, n + 1):
        time += 2 * ((h0 * (0.5 ** i)) / g) ** 0.5  # 计算后续反弹时间

    return height, total_distance, time


# 计算第 10 次反弹的结果
n = 10
height, total_distance, total_time = bouncing_ball(n)

# 输出结果
print(f"第 {n} 次反弹的高度: {height:.6f} m")
print(f"球一共经过的距离: {total_distance:.6f} m")
print(f"球运动的总时间: {total_time:.6f} s")
