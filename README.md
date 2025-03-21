# 小球运动问题
一球从 100 米的高度自由落体（忽略空气阻力），每次落地后反跳回原高度的一半，再落下。
    求：（1）第10次掉下并反弹到最高点时，反弹了多高？此时球一共经过多少米，运动了多少时间？ 
    （2）第n次掉下并反弹到最高点时，反弹了多高？此时球一共经过多少米，运动了多少时间？

解：
高度计算：每次反弹高度为一半，第n次对应(1/2)^n。
总距离计算：第一次下落高度(h0)+之后每次高度(h_bounce)。(100+50)+(50+25)+...
时间计算：物理公式h=1/2gt^2；进而得到t公式，再进行每段距离对应时间的求和。
