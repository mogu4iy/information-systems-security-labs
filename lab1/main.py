from vigenere import Vigenere
from babbage import Babage
import string

KEY = list('PROPAGANDA')
# DATA = 'GOD IS ON OUR SIDE LONG LIVE THE KING'
ALPHABET = string.ascii_letters
ALPHABET_FREQUENCY = {
    "a": 0.08167,
    "b": 0.01492,
    "c": 0.02782,
    "d": 0.04253,
    "e": 0.12702,
    "f": 0.02228,
    "g": 0.02015,
    "h": 0.06094,
    "i": 0.06966,
    "j": 0.00153,
    "k": 0.00772,
    "l": 0.04025,
    "m": 0.02406,
    "n": 0.06749,
    "o": 0.07507,
    "p": 0.01929,
    "q": 0.00095,
    "r": 0.05987,
    "s": 0.06327,
    "t": 0.09056,
    "u": 0.02758,
    "v": 0.00978,
    "w": 0.02360,
    "x": 0.00150,
    "y": 0.01974,
    "z": 0.00074
}

if __name__ == '__main__':
    with open('encoded.txt', 'w') as encoded_file:
        with open("code.txt", 'r') as code_file:
            data = code_file.read()
            encrypted = Vigenere.encrypt(key=KEY, alphabet=list(ALPHABET), data=list(data))
            decrypted = Vigenere.decrypt(key=KEY, alphabet=list(ALPHABET), data=encrypted)
            babage_decrypted = Babage.decrypt(alphabet=list(ALPHABET_FREQUENCY.keys()),
                                              frequency=ALPHABET_FREQUENCY,
                                              data=list(''.join(encrypted).lower()))
            encoded_file.write(''.join(encrypted))
            print(('\n' + '-' * 50 + '\n').join(
                ['Data :', data,
                 '\nEncrypted data :', ''.join(encrypted),
                 '\nDecrypted data :', ''.join(decrypted),
                 '\nBabage attack data :', ''.join(babage_decrypted)]))
