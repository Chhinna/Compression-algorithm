# LZW Encoder
# Name: Aditya Gupta
# ID: 800966229
# ITCS 6114

import sys
from sys import argv
from struct import *

# taking the input file and the number of bits from command line
# defining the maximum table size
# opening the input file
# reading the input file and storing the file data into data variable
#input_file, n = argv[1:]
input_file = "my_text.txt"
n = 32
maximum_table_size = pow(2,int(n))      
file = open("my_text.txt")
#print("ok")
#print(file)
data = file.read()
print(data)
i = 0
#print("ok")
# Building and initializing the dictionary.
dictionary_size = 256                   
dictionary = {chr(i): i for i in range(dictionary_size)}    
string = ""             # String is null.
compressed_data = []    # variable to store the compressed data.

# iterating through the input symbols.
# LZW Compression algorithm
for symbol in data:
    #print(symbol)
    string_plus_symbol = string + symbol # get input symbol.
    if string_plus_symbol in dictionary: 
        string = string_plus_symbol
    else:
        compressed_data.append(dictionary[string])
        #print(dictionary[string])
        i = i+1
        if(len(dictionary) <= maximum_table_size):
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1
        string = symbol

if string in dictionary:
    compressed_data.append(dictionary[string])
    #print(dictionary[string])
    i=i+1

# storing the compressed string into a file (byte-wise).
out = input_file.split(".")[0]
output_file = open(out + ".lzw", "wb")
print(compressed_data)
print(dictionary)
for data in compressed_data:
    output_file.write(pack('>H',int(data)))
    print(pack('>H',int(data)))
    
output_file.close()
#print(pack('>H',int('119')))
#print(i)
file.close()
