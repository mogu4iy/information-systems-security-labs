from caesar import Caesar
from vigenere import Vigenere


class Babage:
    @staticmethod
    def clear_data(alphabet: list, data: list):
        return list(filter(lambda el: el in alphabet, data))

    @staticmethod
    def slice_data(key: int, data: list) -> list:
        # Slice data to <key> parts
        # Each part is encrypted by Caesar
        slices = [[data[i * key + j] for i in range(0, len(data) // key)] for j in range(0, key)]
        j = 0
        i = len(data) - len(data) % key
        while j < key and i < len(data):
            if j == key:
                j = 0
            slices[j].append(data[i])
            i += 1
        return slices

    @staticmethod
    def coincidence(data1: list, data2: list) -> int:
        return len([1 for d1, d2 in zip(data1, data2) if d1 == d2])

    @staticmethod
    def shift_data(shift: int, data: list) -> list:
        return data[shift: len(data)] + data[0: shift]

    @staticmethod
    def get_key_length_list(data: list) -> list:
        key_coincidence_list = [[i, Babage.coincidence(data, Babage.shift_data(i, data))] for i in range(1, len(data))]
        coincidence_list = list(map(lambda index_value: index_value[1], key_coincidence_list))
        return list(
            sorted(
                map(lambda index_value: index_value[0],
                    filter(lambda index_value: index_value[1] > sum(coincidence_list) / len(coincidence_list),
                           key_coincidence_list)
                    )
            ))

    @staticmethod
    def get_data_frequency(alphabet: list, data: list) -> dict:
        return {el: data.count(el) / len(data) for el in alphabet}

    @staticmethod
    def frequency_analysis(alphabet: list, frequency: dict, data: list) -> str:
        difference_min = len(alphabet)
        data_key = 0
        # check all available keys
        for key in range(len(alphabet)):
            data_offset = Caesar.decrypt(key, alphabet, data)
            data_offset_frequency = Babage.get_data_frequency(alphabet, data_offset)
            # Find the most likely variant of key, by minimizing the difference between alphabet elements frequencies
            # and decrypted data elements frequencies
            difference = sum([(frequency[el] - data_offset_frequency[el]) ** 2 for el in alphabet])
            if difference_min > difference:
                difference_min = difference
                data_key = key

        return alphabet[data_key]

    @staticmethod
    def decrypt(alphabet: list, frequency: dict, data: list) -> list:
        variants = []
        cleared_data = Babage.clear_data(alphabet, data)
        key_lengths = Babage.get_key_length_list(cleared_data)
        # Check variant of secret code for every available key (I check only for most likely one)
        for key in key_lengths[:1]:
            variants.append(list(map(lambda el: Babage.frequency_analysis(alphabet, frequency, el),
                                     Babage.slice_data(key, cleared_data))))
        return Vigenere.decrypt(variants[0], alphabet, data)
