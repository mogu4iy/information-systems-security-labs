import copy


class Caesar:
    @staticmethod
    def shift(alphabet, index, el):
        return alphabet[(alphabet.index(el) + index) % len(alphabet)]

    @staticmethod
    def shift_map(alphabet, index):
        return lambda el: Caesar.shift(alphabet, index, el)

    @staticmethod
    def encrypt(key: int, alphabet: list, data: list) -> list:
        return list(map(Caesar.shift_map(alphabet, key), copy.deepcopy(data)))

    @staticmethod
    def decrypt(key: int, alphabet: list, data: list) -> list:
        return list(map(Caesar.shift_map(alphabet, len(alphabet) - key), copy.deepcopy(data)))
