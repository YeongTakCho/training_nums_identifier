# n_input =  784 (28**2), (hidden) n_layer1= 16, (hidden) n_layer 2 = 16, n_output = 10 (0~9)

# a0. input: int a[784][1] (*6000) => 0.784(4704) kb
# a1. layer1: float weight1[16][784], float bias1[16][1] (12544,16) => 50.192 kb
# a2. layer2: float weight2[16][16], float bias2[16][1] (256,16) => 1.088 kb
# a3. output: float weight3[10][16], float bias3[10][1] (160,10) => 0.68 kb
# total: n_weight = 12960, n_bias = 42

# a(N+1) = ReLU(W* a(N) + b)
# a(3) = Sigmoid(W * a(2) + b

# <foramt character>     - used (un)packing
# B: unsigned char: 1byte
# f: float: 4byte

import numpy as np
from struct import unpack, pack


print('-------------------------')
print('Tarining Program Started')
print('-------------------------')

fp_image = open('train-images.idx3-ubyte', 'rb')        # read image file
fp_label = open('train-labels.idx1-ubyte', 'rb')        # read label file
if fp_image and fp_label:
    print('image, label file normally opened')

w_path = 'C:\\Users\\s_andycho1120\\Desktop\\training_nums_identifier\\gitignore\\un_trained_values\\'
w1 = open(w_path + 'w1.idx2-ubtye', 'rb+')
w2 = open(w_path + 'w2.idx2-ubtye', 'rb+')
w3 = open(w_path + 'w3.idx2-ubtye', 'rb+')
b1 = open(w_path + 'b1.idx1-ubtye', 'rb+')
b2 = open(w_path + 'b2.idx1-ubtye', 'rb+')
b3 = open(w_path + 'b3.idx1-ubtye', 'rb+')

if w1 and w2 and w3 and b1 and b2 and b3:
    print('weight, bias file noarmally opened')

s = fp_image.read(4)  # read first 16byte
n_images = int(unpack('>' + len(s)//4 * 'i', fp_image.read(4))[0])
s = fp_image.read(8)
l = fp_label.read(8)  # read first  8byte

while(True):
    for i in range(n_images):
        s = fp_image.read(784)
        l = fp_label.read(1)

        if not s:
            break
        if not l:
            break

        index = int(l[0])

        # struct.unpack(format, buffer) => unpack buffer(may packed same foramt) with given foramt
        img_data = unpack(len(s)*'B', s)  # int img_data[784]
        print(index, img_data[0])
        # numpy.reshape(a, newshape, order='C') => Gives a new shape to an array without changing its data.
        # img = np.reshape(img_data, (28, 28))
        # print(index)
        # for line in img:
        #     for d in line:
        #         print('%02x' % (d), end=" ")
        #     print()


# def get_cost(index, img_data):


# def Backpropagation(cost):
