import numpy as np

def dot(a, b):
    assert(isinstance(a, np.ndarray) and isinstance(b, np.ndarray))
    assert(a.ndim == 2 and b.ndim == 2)
    assert(a.shape[1] == b.shape[0])
    
    #这里假设自己来实现矩阵相乘，实际并不会这么做
    c = np.zeros((a.shape[0], b.shape[1]))
    for i in range (a.shape[0]):
        for j in range (b.shape[1]):
            v1 = a[i,:]
            v2 = b[:,j]
            for k in range(v1.shape[0]):  #这里本身有bug，假设a.shape[1] == b.shape[0]
                c[i][j] += v1[k] * v2[k]
    return c

#第一种情况
m1 = np.arange(1,5).reshape(2,2)
m2 = np.arange(0,9).reshape(3,3)
#m = dot(m1, m2)

#第二种情况
m = dot(m2, m1)

