import codecs
import base64
import string
from set1.challenge3 import single_byte_xor_decipher
from utils import english_letter_frequency_dict

s1c6_input1 = 'this is a test'
s1c6_input2 = 'wokka wokka!!!'


def string_to_binary(string_input):
    return ''.join(format(ord(c), 'b').zfill(8) for c in string_input)


def bytes_to_binary(bytes_input):
    return ''.join(format(i, 'b').zfill(8) for i in bytes_input)


def get_hamming_distance(input1, input2):
    if type(input1) == str and type(input2) == str:
        input1_binary = string_to_binary(input1)
        input2_binary = string_to_binary(input2)
    else:
        input1_binary = bytes_to_binary(input1)
        input2_binary = bytes_to_binary(input2)
    return sum([0 if a == b else 1 for a, b in zip(input1_binary, input2_binary)])


def list_to_n_sized_chunks(lst, n):
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i + n])
    return result


def generate_histogram_dict(s):
    freq = {}
    for c in s.lower():
        if c in string.ascii_letters:  # + string.digits:
            freq[c] = freq.get(c, 0) + 1
    total = sum(freq.values())
    return {k: v/total for k, v in freq.items()}


def calculate_histogram_diff(h):
    result = 0
    for c in h.keys():
        result += abs(h[c] - english_letter_frequency_dict[c])
    return result


def guess_potential_key_sizes(cipher):
    hamming_distances = []
    for key_size in range(2, 41):
        chunks = list_to_n_sized_chunks(cipher, key_size)
        prev = None
        distances = []
        for curr in chunks:
            if prev is not None and len(prev) == len(curr):
                distances.append(get_hamming_distance(prev, curr) / key_size)
            else:
                prev = curr
        hamming_distances.append((key_size, sum(distances) / len(distances)))
    return list(map(lambda x: x[0], sorted(hamming_distances, key=lambda x: x[1])[:3]))


def get_ith_byte_blocks(cipher, key_size):
    cipher_chunks = list_to_n_sized_chunks(cipher, key_size)
    transpose_ith_bytes = []
    for ith_byte in range(key_size):
        ith_byte_block = [cipher_chunk[ith_byte] for cipher_chunk in cipher_chunks if ith_byte < len(cipher_chunk)]
        transpose_ith_bytes.append(ith_byte_block)
    return transpose_ith_bytes


def break_repeating_key_xor():
    with open('resources/s1c6.txt') as s1c6:
        cipher = base64.b64decode(s1c6.read())

    potential_key_sizes = guess_potential_key_sizes(cipher)

    potential_keys = []
    for key_size in potential_key_sizes:
        ith_byte_blocks = get_ith_byte_blocks(cipher, key_size)
        potential_key = ''
        for ith_byte_block in ith_byte_blocks:
            kth_key_char = single_byte_xor_decipher(ith_byte_block)
            potential_key += kth_key_char[0]
        potential_keys.append(potential_key)

    for key in potential_keys:
        plaintext = bytes([cipher[i] ^ ord(key[i % len(key)]) for i in range(len(cipher))])
        print(plaintext)
    return potential_keys
