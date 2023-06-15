# Huffman Compression
Huffman Compression is a Python project that provides various compression functionalities, including string compression, paragraph compression in words, Hafez documentation compression, and image compression. The project aims to offer a smooth and simple user interface, allowing users to compress their data efficiently. It leverages the power of the Huffman coding algorithm to achieve effective compression.
## Features

- **String Compression:**
This feature enables users to compress individual strings using the Huffman coding algorithm, reducing their size and conserving storage space.
- **Paragraph Compression in Words:**
With this feature, users can compress entire paragraphs by encoding the words using Huffman coding. This allows for efficient storage and transmission of textual data.
- **Hafez Documentation Compression:**
Hafez documentation is a specific type of text commonly found in various domains. This feature focuses on compressing such documentation, enabling efficient storage and retrieval of this type of information.
- **Image Compression:**
Huffman Compression also supports image compression. It applies the Huffman coding technique to represent image data more efficiently, reducing file size while preserving image quality.
- **Smooth and Simple UI:**
The project offers a user-friendly interface, making it easy for users to interact with the compression functionalities. The intuitive design ensures a smooth user experience.
- **Calculations:**
The project provides statistical calculations related to compression, such as compression ratio, compression time, and decompression time. These calculations allow users to evaluate the effectiveness and efficiency of the compression process.
## Encoding example
#### String : hello coders

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
![Image description](image_path_or_url)

The project is entirely implemented in Python, utilizing the Qt GUI framework. Qt offers advanced graphical programming capabilities and facilitates efficient drawing operations. By leveraging the features and functionality provided by Qt, the project delivers a robust and versatile user interface.

## Why Python
Python was chosen as the programming language for this project due to its simplicity and ease of learning. Python's clean syntax and extensive set of libraries make it an ideal choice for implementing compression algorithms.

## Why Qt
The Qt GUI framework was selected for this project primarily because of its extensive documentation. Qt's comprehensive documentation greatly facilitates the process of developing GUI applications using Python. It provides clear examples, tutorials, and references, enabling developers to quickly grasp and utilize the power of GUI programming with Python.
By combining the simplicity of Python with the capabilities of the Qt framework, Huffman Compression aims to offer a user-friendly and efficient compression tool for various types of data.
## Getting Started
To use Huffman Compression, follow these steps:

Clone the project repository from GitHub.
Install the required dependencies, including Python and the Qt framework.
Run the main Python script to launch the Huffman Compression application.
Explore the different compression features provided by the application.
Enjoy efficient data compression and storage!

## Contributions
Contributions to Huffman Compression are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, please feel free to submit a pull request. We appreciate your contribution to making Huffman Compression even better.

## License
Huffman Compression is licensed under the **RTB** License. You are free to use, modify, and distribute the project in accordance with the terms and conditions of this license. See the LICENSE file for more details.

## Contact
If you have any questions, suggestions, or feedback, please feel free to contact the project maintainers at [rezatb2002@gmail.com]. We appreciate your interest in Huffman Compression and look forward to hearing from you.
