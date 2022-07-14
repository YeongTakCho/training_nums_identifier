# reference https://seongkyun.github.io/study/2019/05/20/weight_init/
# idx file format https://www.fon.hum.uva.nl/praat/manual/IDX_file_format.html
# first ReLU weight setting method: He

import numpy as np
from struct import pack


def make_new_weight_file(level, fan_out, fan_in):
    title = 'w' + str(level) + '.idx3-ubtye'
    path = 'C:\\Users\\s_andycho1120\\Desktop\\training_nums_identifier\\gitignore\\un_trained_values\\'

    file_name = path + title
    print("file name: ", file_name)
    # print(file_name)

    try:
        fp = open(file_name, 'wb')
        # <idx3 first bytes format>
        # 0x00\00\0D\02 (type of data: float)(number of dimensions: 2)
        # size of dimension 1 (4bytes)
        # size of dimension 2 (4bytes)
        if fp:
            arr = [0x000d02, fan_out, fan_in]
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


if __name__ == '__main__':
    make_new_weight_file(3, 10, 16)
