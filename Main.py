from Huffman_v2 import huffman_encoder_decoder, encode_image

# Driver code
if __name__ == "__main__":
    encoded, decoded, code_map, freq_map, root, isParagraph = huffman_encoder_decoder(input())
    # encoded, decoded, code_map, freq_map, root = encode_image("flower.jpg")
    charList = sorted(code_map)
    for key in charList:
        print(key, code_map[key])
    # print(encoded)
    print(decoded)
