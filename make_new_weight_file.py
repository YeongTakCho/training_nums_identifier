# reference https://seongkyun.github.io/study/2019/05/20/weight_init/
# idx file format https://www.fon.hum.uva.nl/praat/manual/IDX_file_format.html
# first ReLU weight setting method: He

import numpy as np
from struct import pack
from gitignore.user_data import path


def make_new_weight_file(level, fan_in, fan_out):
    title = 'w' + str(level) + '.idx2-ubtye'

    file_name = path + title
    print("file name: ", file_name)

    try:
        fp = open(file_name, 'wb')
        # <idx3 first bytes format>
        # 0x00\00\0D\02 (type of data: float)(number of dimensions: 2)
        # size of dimension 1 (4bytes)
        # size of dimension 2 (4bytes)
        if fp:
            arr = [0x000d02, fan_in, fan_out]
            val = pack('>iii', *arr)
            fp.write(val)
            print('idx3 foramt -  complete')

            W = np.random.randn(fan_out, fan_in) * np.sqrt(2 / fan_in)
            # print(W. sum() / (fan_in * fan_out))
            for line in W:
                # print(line)
                fp.write(pack('f' * len(line), *line))

            print('random weight stored - complete')

        else:
            print('file not open')

    except:
        print('error')


def make_new_bias_file(level, length):
    title = 'b' + str(level) + '.idx1-ubtye'
    file_name = path + title
    print("file name: ", file_name)
    try:
        fp = open(file_name, 'wb')
        # <idx1 first bytes format>
        # 0x00\00\0D\01 (type of data: float)(number of dimensions: 1)
        # size of dimension 1 (4bytes)
        if fp:
            arr = [0x000d01, length]
            val = pack('>ii', *arr)
            fp.write(val)
            print('idx3 foramt -  complete')

            for _ in range(length):
                fp.write(pack('f', (0.01)))

            print('bias stored - complete')

        else:
            print('file not open')

    except:
        print('error')


if __name__ == '__main__':
    # make_new_weight_file(1, 784, 16)
    # make_new_weight_file(2, 16, 16)
    # make_new_weight_file(3, 16, 10)
    # make_new_bias_file(1, 16)
    # make_new_bias_file(2, 16)
    # make_new_bias_file(3, 10)
    pass
