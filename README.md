# Huffman Compression
Huffman Compression is a Python project that provides various compression functionalities, including string compression, paragraph compression in words, Hafez documentation compression, and image compression. The project aims to offer a smooth and simple user interface, allowing users to compress their data efficiently. It leverages the power of the Huffman coding algorithm to achieve effective compression.
## Features

- **String Compression:**
This feature enables users to compress individual strings using the Huffman coding algorithm, reducing their size and conserving storage space.
- **Paragraph Compression in Words:**
With this feature, users can compress entire paragraphs by encoding the words using Huffman coding. This allows for efficient storage and transmission of textual data.
- **Hafez Documentation Compression:**
Hafez, also known as Khwāja Shams-ud-Dīn Muḥammad Ḥāfeẓ-e Shīrāzī, was a Persian poet from the 14th century. He is widely regarded as one of the most celebrated and influential poets in Persian literature. His works are known for their deep wisdom, mystical themes, and intricate poetic structures.
By applying Huffman Compression to Hafez documentation, we aim to provide an efficient way of storing and transmitting these treasured poems while maintaining their essence. This feature enables users to compress and decompress Hafez's poetry with ease.
- **Image Compression:**
Huffman Compression also supports image compression. It applies the Huffman coding technique to represent image data more efficiently, reducing file size while preserving image quality.
- **Smooth and Simple UI:**
The project offers a user-friendly interface, making it easy for users to interact with the compression functionalities. The intuitive design ensures a smooth user experience.
- **Calculations:**
The project provides statistical calculations related to compression, such as compression ratio, compression time, and decompression time. These calculations allow users to evaluate the effectiveness and efficiency of the compression process.
## Encoding example
#### String : Hello Coders

### Huffman Table
| Character | Frequency | Code   |
| --------- | --------- | ------ |
| o         | 3         | 00     |
| l         | 2         | 010    |
| e         | 2         | 011    |
| h         | 1         | 1000   |
| c         | 1         | 1001   |
| d         | 1         | 1010   |
| s         | 1         | 1011   |
| r         | 1         | 1100   |
| space     | 1         | 1101   |

#### Encoded String : 100011011010010011010010000110011010011100

## Design

The Huffman tree in this project is visualized using the tikinter library with the help of the canvas module. This allows for an interactive and visually appealing representation of the Huffman coding tree.
![Image description]([image_path_or_url](https://github.com/Reza-Tahmasbi/Huffman-compression/blob/master/huffman%20coding.jpeg))

The project is entirely implemented in Python, utilizing the Qt GUI framework. Qt offers advanced graphical programming capabilities and facilitates efficient drawing operations. By leveraging the features and functionality provided by Qt, the project delivers a robust and versatile user interface.

## Why Python
Python was chosen as the programming language for this project due to its simplicity and ease of learning. Python's clean syntax and extensive set of libraries make it an ideal choice for implementing compression algorithms.

## Why Qt
The Qt GUI framework was selected for this project primarily because of its extensive documentation. Qt's comprehensive documentation greatly facilitates the process of developing GUI applications using Python. It provides clear examples, tutorials, and references, enabling developers to quickly grasp and utilize the power of GUI programming with Python.
By combining the simplicity of Python with the capabilities of the Qt framework, Huffman Compression aims to offer a user-friendly and efficient compression tool for various types of data.
## Getting Started

To use Huffman Compression, follow these steps:

1. Clone the project repository from GitHub.
2. Install the required dependencies, including Python and the Qt framework.
3. Run the main Python script to launch the Huffman Compression application.
4. Explore the different compression features provided by the application.
5. Enjoy efficient data compression and storage!

## Contributions
Contributions to Huffman Compression are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, please feel free to submit a pull request. We appreciate your contribution to making Huffman Compression even better.

## Project Contributors
We would like to acknowledge and thank the following coders for their contributions to this project:
<br>
Mohammad Biabani - @Mohammad-Biabani
<br>
Reza Tahmasbi - @rezatb
<br>
Ali Aziz - @S-AliAziz

## Contact
If you have any questions, suggestions, or feedback, please feel free to contact the project maintainers at [rezatb2002@gmail.com]. We appreciate your interest in Huffman Compression and look forward to hearing from you.
