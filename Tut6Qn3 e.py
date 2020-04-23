import math
n=1
eqn=(1-1/n)**n
while (1/math.e)-eqn > 0.0001:
    n+=1

print(n)