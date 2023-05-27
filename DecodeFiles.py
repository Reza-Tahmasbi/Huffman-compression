import os
from Huffman import huffman_encoder_decoder

input_directory = "C:/Users/reza/PycharmProjects/huffman/Hafez/input"
output_directory = "C:/Users/reza/PycharmProjects/huffman/Hafez/output"
output_directory_map = "C:/Users/reza/PycharmProjects/huffman/Hafez/output_map"
# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

for i in range(1, 500):
    input_file = os.path.join(input_directory, f"{i}.txt")
    output_file = os.path.join(output_directory, f"{i}.txt")
    output_file_code_map = os.path.join(output_directory_map, f"{i}.txt")
    with open(input_file, "r", encoding="utf-8") as file1:
        with open(output_file, "w", encoding="utf-8") as file2:
            for line in file1:
                line = line.strip()
                encoded_line, _, codeMap, _ = huffman_encoder_decoder(line)

                # Process the encoded line as needed
                print(line)
                print(encoded_line)
                file2.write(encoded_line)
                file2.write("\n")
    with open(output_file_code_map, "w", encoding="utf-8") as file:
        charList = sorted(codeMap)
        for key in charList:
            file.write(key + " " + codeMap[key])
            file.write("\n")