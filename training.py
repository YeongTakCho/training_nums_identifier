# n_input =  784 (28**2), (hidden) n_layer1= 16, (hidden) n_layer 2 = 16, n_output = 10 (0~9)

# a0. input: int a[784][1] (*6000) => 0.784(4704) kb
# a1. layer1: float weight[16][784], float bias[16][1] (12544,16) => 50.192 kb
# a2. layer2: float weight[16][16], float bias[16][1] (256,16) => 1.088 kb
# a3. output: float weight[10][16], float bias[10][1] (160,10) => 0.68 kb
# total: n_weight = 12960, n_bias = 42

# a(N+1) = ReLU(W* a(N) + b)
# a(3) = Sigmoid(W * a(2) + b

# <foramt character>     - used (un)packing
# B: unsigned char: 1byte
# f: float: 4byte

import numpy as np
from struct import *

fp_image = open('train-images.idx3-ubyte', 'rb')        # read image file
fp_label = open('train-labels.idx1-ubyte', 'rb')        # read label file

s = fp_image.read(16)  # read first 16byte
l = fp_label.read(8)  # read first  8byte

while(True):
    s = fp_image.read(784)
    l = fp_label.read(1)

    if not s:
        break
    if not l:
        break

    index = int(l[0])
    # print(k,":",index)

    # struct.unpack(format, buffer) => unpack buffer(may packed same foramt) with given foramt
    img_data = unpack(len(s)*'?', s)
    # numpy.reshape(a, newshape, order='C') => Gives a new shape to an array without changing its data.
    img = np.reshape(img_data, (28, 28))
    for line in img:
        for d in line:
            print('%02x' % (d), end=" ")
