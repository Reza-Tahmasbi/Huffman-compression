#include <bits/stdc++.h>
#define MAX_TREE_HT 256
using namespace std;
#include <locale.h>
#include <wchar.h>
#include <iostream>
// setlocale(LC_ALL, "fa_IR.UTF-8");
 
// to map each character its huffman value
map<char, string> codes;
 
// To store the frequency of character of the input data
map<char, int> freq;
 
// A Huffman tree node
struct MinHeapNode {
    char data; // One of the input characters
    int freq; // Frequency of the character
    MinHeapNode *left, *right; // Left and right child
 
    MinHeapNode(char data, int freq)
    {
        left = right = NULL;
        this->data = data;
        this->freq = freq;
    }
};
 
// utility function for the priority queue
struct compare {
    bool operator()(MinHeapNode* l, MinHeapNode* r)
    {
        return (l->freq > r->freq);
    }
};
 
// Utility function to implement min heap using a vector
class MinHeap
{
    vector<MinHeapNode*> heap;
public:
    // Constructor
    MinHeap()
    {
        heap = vector<MinHeapNode*>();
    }
    int getSize()
    {
        return heap.size();
    }
    vector<MinHeapNode*> getHeap(){
        return heap;
    }
    // Get the parent index
    int parent(int i)
    {
        return (i - 1) / 2;
    }
 
    // Get the leftchild index
    int left(int i)
    {
        return (2 * i + 1);
    }
 
    // Get the right child index
    int right(int i)
    {
        return (2 * i + 2);
    }
 
    // Insert a new node into the heap
    void insertNode(MinHeapNode* node)
    {
        heap.push_back(node);
        int i = heap.size() - 1;
        while (i != 0 && heap[parent(i)]->freq > heap[i]->freq)
        {
            swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }
 
    // Extract the minimum node from the heap
    MinHeapNode* extractMin()
    {
        if (heap.size() == 0)
            return NULL;
 
        MinHeapNode* root = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
 
        MinHeapify(0);
 
        return root;
    }
 
    // Heapify the node at index i
    void MinHeapify(int i)
    {
        int l = left(i);
        int r = right(i);
        int smallest = i;
        if (l < heap.size() && heap[l]->freq < heap[i]->freq)
            smallest = l;
        if (r < heap.size() && heap[r]->freq < heap[smallest]->freq)
            smallest = r;
        if (smallest != i)
        {
            swap(heap[i], heap[smallest]);
            MinHeapify(smallest);
        }
    }
 
    // Check if the heap is empty
    bool isEmpty()
    {
        return heap.size() == 0;
    }
};
 
void storeCodes(struct MinHeapNode* root, string str)
{
    if (root == NULL)
        return;
    if (root->data != '$')
        codes[root->data] = str;
    storeCodes(root->left, str + "0");
    storeCodes(root->right, str + "1");
}
// function to build the Huffman tree and store it
// in minHeap
struct MinHeapNode* HuffmanCodes(int size)
{
    MinHeap minHeap;
    struct MinHeapNode *left, *right, *top;
    for (map<char, int>::iterator v = freq.begin(); v != freq.end(); v++)
        minHeap.insertNode(new MinHeapNode(v->first, v->second));
    while (!minHeap.isEmpty() && minHeap.getSize() != 1) {
        left = minHeap.extractMin();
        right = minHeap.extractMin();
        top = new MinHeapNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;
        minHeap.insertNode(top);
    }
    storeCodes(minHeap.getHeap()[0], "");
    return minHeap.getHeap()[0];
}
 
// utility function to store map each character with its
// frequency in input string
void calcFreq(string str)
{
    for (char ch: str)
        freq[ch]++;
}
 
// utility function to print characters along with
// their Huffman value
void printCodes(struct MinHeapNode* root, string str)
{
    if (!root)
       return;
    if (root->data != '$')
        cout << root->data << ": " << str << "\n";
    printCodes(root->left, str + "0");
    printCodes(root->right, str + "1");
}
 
// utility function to store characters along with
// their Huffman value in a hash table, here we
// have C++ STL map
 
// function iterates through the encoded string s
// if s[i]=='1' then move to node->right
// if s[i]=='0' then move to node->left
// if leaf node append the node->data to our output string
string decode_file(struct MinHeapNode* root, string s)
{
    string ans = "";
    struct MinHeapNode* curr = root;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '0')
            curr = curr->left;
        else
            curr = curr->right;
 
        // reached leaf node
        if (curr->left == NULL and curr->right == NULL) {
            ans += curr->data;
            curr = root;
        }
    }
    // cout<<ans<<endl;
    return ans + '\0';
}
 #include <fcntl.h>
 #include <fstream>
// Driver code
int main()
{
    string str;
    cin >> str;
    string encodedString, decodedString;
    calcFreq(str);
    struct MinHeapNode* root = HuffmanCodes(str.length());
    cout << "Character With there Frequencies:\n";
    for (auto v = codes.begin(); v != codes.end(); v++)
        cout << v->first << ' ' << v->second << endl;
 
    for (auto i : str)
        encodedString += codes[i];
 
    cout << "\nEncoded Huffman data:\n"
         << encodedString << endl;
 
      // Function call
    decodedString
        = decode_file(root, encodedString);
    cout << "\nDecoded Huffman Data:\n"
         << decodedString << endl;
    return 0;
}