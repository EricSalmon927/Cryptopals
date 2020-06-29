import codecs
from utils import most_common_english_letters


s1c3_input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'


def single_byte_xor_decipher(input_bytes):
    chars = range(32, 127)
    result = ('character', 'plaintext', -1)
    for c in chars:
        plaintext = codecs.decode(bytes([a ^ c for a in input_bytes]))
        score = sum([1 for a in plaintext.upper() if a in most_common_english_letters])
        result = (chr(c), plaintext, score) if score >= result[2] else result
    return result
