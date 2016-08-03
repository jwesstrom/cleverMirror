from math import cos, sin, pi
import random



# vertices = []
# indices = []
# step = 10
# istep = (pi * 2) / float(step)
# for i in range(step):
#     x = 300 + cos(istep * i) * 100
#     y = 300 + sin(istep * i) * 100
#     vertices.extend([x, y, 0, 0])
#     indices.append(i)

vertices = []
indices = []
for i in range(20):
    x = 10*i
    y = 200+random.randint(1,30)
    vertices.extend([x, y, 0, 0])
    indices.append(i)
    print x
