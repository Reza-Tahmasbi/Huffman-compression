from Huffman import huffman_encoder_decoder
import Draw
# Driver code
if __name__ == "__main__":
    encoded, decoded, code_map, freq_map, root = huffman_encoder_decoder(input())
    charList = sorted(code_map)
    for key in charList:
        print(key, code_map[key])
    print(encoded)
    print(decoded)
    Draw.draw_huffman_tree_gui(root)

