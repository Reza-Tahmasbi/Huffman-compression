from collections import defaultdict
from MinHeap import *

# to map each character to its Huffman value
codeMap = {}
# To store the frequency of characters in the input data
freqMap = defaultdict(int)


# utility function to print characters along with their Huffman value
def printCodes(root, string):
    if root is None:
        return
    if root.data != '$':
        print(root.data, ":", string)
    printCodes(root.left, string + "0")
    printCodes(root.right, string + "1")


# utility function to store characters along with their Huffman value in a hash table
def storeCodes(root, string):
    if root is None:
        return
    if root.key != '$':
        codeMap[root.key] = string
    storeCodes(root.left, string + "0")
    storeCodes(root.right, string + "1")


# function to build the Huffman tree and store it in minHeap
def HuffmanCodes():
    global minHeap
    minHeap = MinHeap()
    for key in freqMap:
        node = MinHeapNode(key, freqMap[key])
        minHeap.insert(node)
    while minHeap.size > 1:
        left = minHeap.extract_min()
        right = minHeap.extract_min()
        top = MinHeapNode('$', left.freq + right.freq)
        top.left = left
        top.right = right
        minHeap.insert(top)

    storeCodes(minHeap.heap[0], "")


# utility function to store the frequency of each character in the input string
def getFreq(string):
    for char in string:
        freqMap[char] += 1


# function iterates through the encoded string s
# if s[i]=='1' then move to node->right
# if s[i]=='0' then move to node->left
# if leaf node, append the node->data to our output string
def decodeFile(root, string):
    ans = ""
    current = root
    n = len(string)
    for i in range(n):
        if string[i] == '0':
            current = current.left
        else:
            current = current.right

        # reached leaf node
        if current.left is None and current.right is None:
            ans += current.key
            current = root
    return ans


# Driver code
if __name__ == "__main__":
    minHeap = MinHeap()
    string = input("Enter a string: ")
    encodedString = ""
    decodedString = ""
    getFreq(string)
    print(freqMap)
    HuffmanCodes()
    print("Characters with their Frequencies:")
    # Timsort -> combination of merge sort and insertion sort -> O(n log n)
    charList = sorted(codeMap)
    for key in charList:
        print(key, codeMap[key])

    for char in string:
        encodedString += codeMap[char]

    print("\nEncoded Huffman data:")
    print(encodedString)

    # Function call
    decodedString = decodeFile(minHeap.heap[0], encodedString)
    print("\nDecoded Huffman Data:")
    print(decodedString)
