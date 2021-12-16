from lab2.des import DES
from lab2.triple_des import TRIPLE_DES
from pyDes import *

if __name__ == '__main__':
    with open('code.txt', 'r') as file:
        data = file.read()
        name = 'Нікітін Богдан Денисович'
        des_key = DES.generate_key(bytes(name, 'windows-1251').hex())
        print('DES key')
        print(des_key)
        des_cipher = des(des_key, ECB, padmode=PAD_PKCS5)
        print('DES_CIPHER')
        print(des_cipher.encrypt(bytes(data, 'utf-8')))

        triple_des_key = TRIPLE_DES.generate_key(bytearray(name, 'windows-1251').hex())
        print('TRIPLE_DES key')
        print(triple_des_key)
        triple_des_cipher = triple_des(triple_des_key, ECB, padmode=PAD_PKCS5)
        print('TRIPLE_DES_CIPHER')
        print(triple_des_cipher.encrypt(bytes(data, 'utf-8')))
