import base64
from Crypto.Cipher import AES


s1c7_key = 'YELLOW SUBMARINE'


def aes_128_decrypt(ciphertext, key):
    aes_cipher = AES.new(key.encode(), AES.MODE_ECB)
    plaintext = aes_cipher.decrypt(ciphertext)
    return plaintext.decode()


def aes_in_ecb_mode():
    with open('resources/s1c7.txt') as s1c7:
        ciphertext = base64.b64decode(s1c7.read())
    return aes_128_decrypt(ciphertext, s1c7_key)

