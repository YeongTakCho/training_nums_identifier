# reference https://seongkyun.github.io/study/2019/05/20/weight_init/
# idx file format https://www.fon.hum.uva.nl/praat/manual/IDX_file_format.html

# used first ReLU weight setting method: He
import numpy as np
from struct import pack
# <idx3 first bytes format>
# 0x00 00 0D 02 (type of data: float)(number of dimensions: 2)
# size of dimension 1 (4bytes)
# size of dimension 2 (4bytes)


def make_new_weight_file(level, fan_in, fan_out):
    title = 'w' + str(level) + '.idx3-ubtye'
    path = 'C:\\Users\\s_andycho1120\\Desktop\\training_nums_identifier\\'

    file_name = path + title
    print(file_name)

    try:
        fp = open(file_name, 'wb')
        # <idx3 first bytes format>
        # 0x00\00\0D\02 (type of data: float)(number of dimensions: 2)
        # size of dimension 1 (4bytes)
        # size of dimension 2 (4bytes)
        if fp:
            arr = [0x000d02, fan_out, fan_in]
            val = pack('>iii', *arr)
            print(val)
            fp.write(val)
            print('idx3 foramt compelete')
        else:
            print('file not open')

    except:
        print('error')

    def new_weight(fan_in, fan_out):
        # float matrix[fan_out][fan_in]
        W = np.random.randn(fan_out, fan_in) / np.sqrt(2/fan_in)


make_new_weight_file(1, 20, 20)
