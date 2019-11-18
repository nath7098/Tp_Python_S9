import numpy as np
import scipy as sci


if __name__ == '__main__':
    array_3 = np.random.randint(8,size=(4, 3, 2))
    array_4 = np.random.randint(2,10,size=(4, 3, 2))
    print(array_3)
    print("dimension : ", array_3.ndim)
    print("shape : ", array_3.shape)
    print("size : ", array_3.size)
    print("data type : ", array_3.dtype)
    print("item size : ", array_3.itemsize)
    print("data : ", array_3.data)

    print(" * : ", array_3 * array_4)
    print("dot : ", array_3.dot(array_4))