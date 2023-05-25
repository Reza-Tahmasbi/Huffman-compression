#include "MinHeap.cpp"
#include <iostream>
#include <map>
#include <string>
using namespace std;

void buildFreqArr(map<char, int> frequencyMap, int* ptrFreq){
    // Count the frequency of each character in the input string
    map<char,int>::iterator it;
    int counter = 0;
    for (it = frequencyMap.begin(); it != frequencyMap.end(); it++) {
        *(ptrFreq+counter) = it->second;
        counter++;
    }
}
void buildKeyArr(map<char, int> frequencyMap, char* ptrKey){
    // Count the frequency of each character in the input string
    map<char,int>::iterator it;
    int counter = 0;
    for (it = frequencyMap.begin(); it != frequencyMap.end(); it++) {
        *(ptrKey+counter) = it->first;
        counter++;
    }
}
map<char, int> buildMap(string& input){
    map<char, int> frequencyMap;
    // Count the frequency of each character in the input string
    for (char ch : input) {
        frequencyMap[ch]++;
    }
    return frequencyMap;
}

// Driver code
int main()
{
    string input;
    cout << "pls in ina: \n";
    cin >> input;
	char key[40];
    char *ptrKey = key;
	int freq[40];
	int *ptrfreq = freq;
    map<char, int> myMap = buildMap(input);
    int size = myMap.size();
    buildFreqArr(myMap, ptrfreq);
    buildKeyArr(myMap, ptrKey);    
	HuffmanCodes(key, freq, size);

	return 0;
}




