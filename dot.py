import numpy as np

def dot(a, b):
    #这里假设自己来实现矩阵相乘，实际并不会这么做
    c = np.zeros((a.shape[0], b.shape[1]))
    for i in range (a.shape[0]):
        for j in range (b.shape[1]):
            for k in range(a.shape[1]):  #这里本身有bug，假设a.shape[1] == b.shape[0]
                c[i][j] += (a[i, k] * b[k, j])

    return c

#第一种情况
m1 = np.zeros((2, 2))
m2 = np.zeros((3, 3))
m = dot(m1, m2)
#第二种情况
m1 = np.zeros((2, 3))
m2 = np.zeros((2, 3))
m = dot(m1, m2)

