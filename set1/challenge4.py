import codecs
from set1.challenge3 import single_byte_xor_decipher


def detect_single_character_xor():
    best_shot = ('line', 'character', 'plaintext', -1)
    with open('resources/s1c4.txt') as s1c4:
        for line in s1c4.read().splitlines():
            try:
                result = single_byte_xor_decipher(codecs.decode(line, 'hex'))
                best_shot = (line, result[0], result[1], result[2]) if result[2] >= best_shot[3] else best_shot
            except UnicodeDecodeError:
                pass
    return best_shot
