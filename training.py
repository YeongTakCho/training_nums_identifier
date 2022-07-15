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

from re import A, L
from gitignore.user_data import path
import numpy as np
from struct import unpack, pack


print('-------------------------')
print('Tarining Program Started')
print('-------------------------')

fp_image = open('train-images.idx3-ubyte', 'rb')        # read image file
fp_label = open('train-labels.idx1-ubyte', 'rb')        # read label file
if fp_image and fp_label:
    print('image, label file normally opened')

w_path = path
fp_w1 = open(w_path + 'w1.idx2-ubtye', 'rb+')
fp_w2 = open(w_path + 'w2.idx2-ubtye', 'rb+')
fp_w3 = open(w_path + 'w3.idx2-ubtye', 'rb+')
fp_b1 = open(w_path + 'b1.idx1-ubtye', 'rb+')
fp_b2 = open(w_path + 'b2.idx1-ubtye', 'rb+')
fp_b3 = open(w_path + 'b3.idx1-ubtye', 'rb+')

if fp_w1 and fp_w2 and fp_w3 and fp_b1 and fp_b2 and fp_b3:
    print('weight, bias file noarmally opened')


fp_image.read(4)  # read first 16byte
n_images = int(unpack('>i', fp_image.read(4))[0])
fp_image.read(8)
l = fp_label.read(8)  # read first  8byte


# will add to get data of type of data, number of dimensions, size of dimentions
fp_w1.read(12)
fp_w2.read(12)
fp_w3.read(12)
fp_b1.read(8)
fp_b2.read(8)
fp_b3.read(8)


def binaryfile_to_list(fp, *d):
    size = 1
    len_d = len(d)
    for i in range(len_d):
        size *= d[i]
    return np.reshape(unpack(size * 'f', fp.read(size * 4)), (d))


w1 = binaryfile_to_list(fp_w1, 784, 16)
w2 = binaryfile_to_list(fp_w2, 16, 16)
w3 = binaryfile_to_list(fp_w3, 16, 10)
b1 = binaryfile_to_list(fp_b1, 16)
b2 = binaryfile_to_list(fp_b2, 16)
b3 = binaryfile_to_list(fp_b3, 10)

times_to_study = 10
for study_seq in range(times_to_study):
    for i in range(n_images):
        s = fp_image.read(784)
        l = fp_label.read(1)

        if not s:
            break
        if not l:
            break

        index = int(l[0])

        # struct.unpack(format, buffer) => unpack buffer(may packed same foramt) with given foramt
        # int img_data[784]
        img_data = list(map(lambda val: val/256, unpack(len(s)*'B', s)))
        # numpy.reshape(a, newshape, order='C') => Gives a new shape to an array without changing its data.
        # img = np.reshape(img_data, (28, 28))
        # print(index)
        # for line in img:
        #     for d in line:
        #         print('%02x' % (d), end=" ")
        #     print()

        @staticmethod
        def get_cost(image, index):
            def relu(x):
                return max(0, x)

            def sigmoid(x):
                return 1 / (1 + np.exp(-x))

            def getCal():
                a = np.dot(image, w1) + b1
                a = list(map(relu, a))

                a = np.dot(a, w2) + b2
                a = list(map(relu, a))

                a = np.dot(a, w3) + b3
                a = list(map(sigmoid, a))

                return a

            def get_chaning_desire(valCal):
                ans = list()
                for i in range(10):
                    if i == index:
                        ans.append(1-valCal[i])
                    else:
                        ans.append(-valCal[i])
                return ans

            def get_cost(to_be_changed):
                return sum(map(lambda val: val**2), to_be_changed)

            def backward():
                pass

            valCal = getCal()
            deseire_to_change = get_chaning_desire(valCal)
            total_cost = get_cost(deseire_to_change)
            backward()
            return total_cost

            # ans = np.dot(np.dot(np.dot(image, w1) + b1, w2) + b2, w3) + b3
            # def Backpropagation(cost):
        cost = get_cost(img_data, index)
