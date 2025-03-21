def ball_falling(h0, n):
    """一球从 100 米的高度自由落体（忽略空气阻力），每次落地后反跳回原高度的一半，再落下。
    求：（1）第10次掉下并反弹到最高点时，反弹了多高？此时球一共经过多少米，运动了多少时间？
    （2）第n次掉下并反弹到最高点时，反弹了多高？此时球一共经过多少米，运动了多少时间？"""

    h = h0 * (0.5) ** n # 第n次反弹高度
    #距离求和逻辑 (100+50) + (50+25) + (25 + 12.5) + ...
    h_sum = h0 + h0 * 0.5  # 从第一次反弹后的结果150开始算
    h_bounce = h0 * 0.5  # 反弹高度从50开始

    for i in range(1, n):#距离求和
        h_sum += h_bounce + h_bounce * 0.5 
        h_bounce *= 0.5 

    g = 9.8
    t =  (2 * h0 / g) ** 0.5  # 第一次下落时间
    t_sum = t
    for i in range(1, n + 1): # n次下落时间求和
        t_sum += 2 * (2 * h0 * (1 / 2) ** i / g) ** 0.5

    return h, h_sum, t_sum

print(f"task1")
h0 =100
n = 10
h, h_sum, t_sum = ball_falling(100,10)
print(f"第 {n} 次掉下并反弹到最高点时，反弹高度: {h:.2f} 米")
print(f"第 {n} 次掉下并反弹到最高点时，经过了: {h_sum:.2f} 米")
print(f"第 {n} 次掉下并反弹到最高点时，运动了: {t_sum:.2f} 秒")


print(f"task2")
n= int (input ("第几次掉下并反弹到最高点？: ") )
h, h_sum, t_sum = ball_falling(100,n)
print(f"第 {n} 次掉下并反弹到最高点时，反弹高度: {h:.2f} 米")
print(f"第 {n} 次掉下并反弹到最高点时，经过了: {h_sum:.2f} 米")
print(f"第 {n} 次掉下并反弹到最高点时，运动了: {t_sum:.2f} 秒")
