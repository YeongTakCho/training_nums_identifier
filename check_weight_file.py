# checking weight file
# check list: type of data, number of dimensions, size of dimention 1, size of dimention 2, *
from struct import unpack

data_type_dict = {0x8: 'unsigned byte',
                  0x9: 'sugbed byte',
                  0xB: 'short',
                  0xC: 'int',
                  0xD: 'float',
                  0xE: 'double'}


def byte_to_int(val):
    unpack(len(val) * '')


def check_weight_file(level):
    return_val = list()

    title = 'w' + str(level) + '.idx2-ubtye'
    path = 'C:\\Users\\s_andycho1120\\Desktop\\training_nums_identifier\\gitignore\\un_trained_values\\'

    file_name = path + title
    fp = open(file_name, 'rb')

    s = fp.read(4)
    n = int(unpack('>' + len(s)//4 * 'i', s)[0])

    data_type = data_type_dict[n // 256]
    n_dimention = n - n//256 * 256

    if __name__ == "__main__":
        print("----------------------------------------")
        print(f"title: {title}")
        print(f"data type: {data_type}")
        print(f"number of dimention: {n_dimention}")

    return_val = [data_type, n_dimention]

    for i in range(n_dimention):
        val = int(unpack('>' + len(s)//4 * 'i', fp.read(4))[0])
        return_val.append(val)

        if __name__ == "__main__":
            print(f"size of dimention {i+1}. {val}")

    return return_val


if __name__ == "__main__":
    check_weight_file(1)
    check_weight_file(2)
    check_weight_file(3)
