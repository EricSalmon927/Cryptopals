import codecs


s1c1_input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'


# Always operate at raw byte level, not string level
def hex_to_base64(input_string):
    hex_decoded = codecs.decode(input_string, 'hex')
    base64_encoded = codecs.encode(hex_decoded, 'base64')
    return base64_encoded
