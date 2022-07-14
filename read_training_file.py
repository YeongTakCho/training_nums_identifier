''' read mnist '''
import numpy as np
import sys
import os
from array import array

from struct import *
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fp_image = open('train-images.idx3-ubyte', 'rb')        # read image file
fp_label = open('train-labels.idx1-ubyte', 'rb')        # read label file


# image resolution (28 x 28)
img = np.zeros((28, 28))

lbl = [[], [], [], [], [], [], [], [], [], []]
d = 0
l = 0
index = 0


s = fp_image.read(16)  # read first 16byte
l = fp_label.read(8)  # read first  8byte

# print(s)
# print("s_len:",len(s))
# print(l)
# print("l_len:",len(l))

"""
#single example - no loop
s = fp_image.read(784)
l = fp_label.read(1)
print("number:",int(l[0]))
img = np.reshape( unpack(len(s)*'B',s), (28,28))

#print(img)
plt.imshow(img,cmap = cm.binary)
plt.show()
"""


k = 0
# read mnist and show character
while True:
    s = fp_image.read(784)
    l = fp_label.read(1)

    if not s:
        break
    if not l:
        break

    index = int(l[0])
    # print(k,":",index)

    # no-loop
    img = np.reshape(unpack(len(s)*'B', s), (28, 28))

    # """
    # #loop
    # for i in range(0, 28):
    #     for j in range(0, 28):
    #         d = s[(i*28)+j]
    #         print('%02x' % (d), end=" ")
    #     print(" ")
    # """

    lbl[index].append(img)

    k = k+1
# print(img)
print(k)
plt.imshow(img, cmap=cm.binary)
plt.show()

print(np.shape(lbl))

print("read done")
