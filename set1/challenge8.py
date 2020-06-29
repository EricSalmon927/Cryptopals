import codecs
from set1.challenge7 import aes_128_decrypt


def detect_aes_in_ecb_mode():
    with open('resources/s1c8.txt') as s1c8:
        for line in s1c8.read().splitlines():
            chunks = set()
            for i in range(0, len(line), 16):
                chunk = line[i:i+16]
                if chunk in chunks:
                    return line
                else:
                    chunks.add(chunk)
    return "AES-128 ECB mode encryption not detected"
