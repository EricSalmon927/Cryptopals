import codecs


s1c2_input1 = '1c0111001f010100061a024b53535009181c'
s1c2_input2 = '686974207468652062756c6c277320657965'


def fixed_xor(string_input1, string_input2):
    hex_decoded_1 = codecs.decode(string_input1, 'hex')
    hex_decoded_2 = codecs.decode(string_input2, 'hex')
    return codecs.encode(bytes([a ^ b for a, b in zip(hex_decoded_1, hex_decoded_2)]), 'hex')
