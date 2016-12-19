# -*- coding: utf-8 -*-

import numpy as np

# ndarray.ndim
# 数组轴的个数，在python的世界中，轴的个数被称作秩, 比如二维数组 ndim就是2, 三维数组 ndim就是3
#
# ndarray.shape
# 数组的维度。这是一个指示数组在每个维度上大小的整数元组。例如一个n排m列的矩阵，它的shape属性将是(n,m)
#
# ndarray.size
# 数组元素的总个数，等于shape属性中元组元素的乘积, n * m。
#
# ndarray.dtype
# 一个用来描述数组中元素类型的对象，可以通过创造或指定dtype使用标准Python类型。另外NumPy提供它自己的数据类型。
#
# ndarray.itemsize
# 数组中每个元素的字节大小。例如，一个元素类型为float64的数组itemsiz属性值为8(=64/8),又如，一个元素类型为complex32的数组item属性为4(=32/8).
#
# ndarray.data
# 包含实际数组元素的缓冲区，通常我们不需要使用这个属性，因为我们总是通过索引来使用数组中的元素。

a = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])

b = np.array([1,2,3,4])

print a.ndim
print a.shape
print a.size
print a.dtype
print a.itemsize
print a.data

print b.ndim
print b.shape
print b.size
print b.dtype
print b.itemsize
print b.data

a.shape = 4,7  # 修改数组shape属性
a.shape = 4,-1  # -1时自动计算此轴的长度
print a

c = b.reshape(2,2)   # reshape改变数组的尺寸, 但是原数组的shape值不变
print c
print b

b[1] = 100   # c和b 共享内存区域, 修改b数组中值, c也会同时被修改
print c
print b

e = np.array([1,2,3,4], dtype=np.float)
print e