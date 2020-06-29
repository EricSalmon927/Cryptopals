import codecs
from set1.challenge1 import hex_to_base64, s1c1_input
from set1.challenge2 import fixed_xor, s1c2_input1, s1c2_input2
from set1.challenge3 import single_byte_xor_decipher, s1c3_input
from set1.challenge4 import detect_single_character_xor
from set1.challenge5 import repeating_key_xor, s1c5_input, s1c5_key
from set1.challenge6 import break_repeating_key_xor
from set1.challenge7 import aes_in_ecb_mode
from set1.challenge8 import detect_aes_in_ecb_mode

if __name__ == '__main__':
    print("Solution Execution Result:")
    # print(hex_to_base64(s1c1_input))                                          # s1c1
    # print(fixed_xor(s1c2_input1, s1c2_input2))                                # s1c2
    # print(single_byte_xor_decipher(codecs.decode(s1c3_input, 'hex')))         # s1c3
    # print(detect_single_character_xor())                                      # s1c4
    # print(repeating_key_xor(s1c5_input, s1c5_key))                            # s1c5
    # print(break_repeating_key_xor())                                          # s1c6
    # print(aes_in_ecb_mode())                                                  # s1c7
    print(detect_aes_in_ecb_mode())                                           # s1c8
