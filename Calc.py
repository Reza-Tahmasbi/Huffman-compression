import Hafez
from Huffman import huffman_encoder_decoder

def getSizeOfStringInBit(string):
    sizeOfStringInBit = 8 * len(string.encode("utf_8"))
    return sizeOfStringInBit

def compressionRatioCalculator(encoded, decoded):
    encodedSize = len(encoded)
    decodedSize = getSizeOfStringInBit(decoded)
    compressionRatio = 100 - ((encodedSize / decodedSize) * 100)
    return compressionRatio

def compressionRatioAverageForSampleTexts():
    compressionRatioAverage = 0
    compressionRatioCommulative = 0
    for ghazal in Hafez.Divan_e_Hafez:
        encoded, decoded, code_map, freq_map, root = huffman_encoder_decoder(ghazal)
        compressionRatioCommulative += compressionRatioCalculator(encoded, decoded)
        
    compressionRatioAverage = compressionRatioCommulative / 100
    return compressionRatioAverage
    