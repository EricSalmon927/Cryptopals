import codecs


s1c5_input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
s1c5_key = "ICE"


def repeating_key_xor(input_string, input_key):
    input_string_bytes = input_string.encode()
    input_key_bytes = input_key.encode()
    result = []
    for i in range(len(input_string_bytes)):
        result.append(input_string_bytes[i] ^ input_key_bytes[i % len(input_key_bytes)])
    return codecs.encode(bytes(result), 'hex')
