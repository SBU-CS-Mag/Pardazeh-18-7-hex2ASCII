def ASCII2Hex(asciiStr):  
    return asciiStr.encode('ascii').hex().upper()


def read_flag():
    file = open('flag.txt','r')
    flag = file.readline()
    file.close()
    return flag


def save_flag(flag):
    file = open('ciphertext.txt','w')
    file.write(flag)
    file.close()


if __name__ == '__main__':
    save_flag(ASCII2Hex(read_flag()))
