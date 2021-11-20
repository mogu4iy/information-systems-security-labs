import copy


class Vigenere:
    @staticmethod
    def encrypt_shift(el, key_shift, key, alphabet):
        key_index = key_shift % len(key)
        alphabet_shift = alphabet.index(el) + alphabet.index(key[key_index])
        alphabet_index = alphabet_shift % len(alphabet)

        return alphabet[alphabet_index]

    @staticmethod
    def decrypt_shift(el, key_shift, key, alphabet):
        key_index = key_shift % len(key)
        alphabet_shift = alphabet.index(el) - alphabet.index(key[key_index])
        alphabet_index = alphabet_shift % len(alphabet)

        return alphabet[alphabet_index]

    @staticmethod
    def encrypt(key: list, alphabet: list, data: list) -> list:
        encrypted = copy.deepcopy(data)

        j = 0
        for i in range(len(data)):
            if data[i] not in alphabet:
                continue
            encrypted[i] = Vigenere.encrypt_shift(data[i], j, key, alphabet)
            j += 1

        return encrypted

    @staticmethod
    def decrypt(key: list, alphabet: list, data: list) -> list:
        decrypted = copy.deepcopy(data)

        j = 0
        for i in range(len(data)):
            if data[i] not in alphabet:
                continue
            decrypted[i] = Vigenere.decrypt_shift(data[i], j, key, alphabet)
            j += 1

        return decrypted
