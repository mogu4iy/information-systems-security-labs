import rsa


def main():
    (public, private) = rsa.newkeys(1024)
    print("Public key:", public)
    print("Private key", private)
    with open("./code.txt", "r") as file:
        message = file.read()
    rsa_encrypt = rsa.encrypt(message.encode("utf-8"), public)
    print("Encrypted message:", rsa_encrypt)
    rsa_decrypt = rsa.decrypt(rsa_encrypt, private)
    print('Decrypted message:', rsa_decrypt.decode('utf8'))


if __name__ == '__main__':
    main()
