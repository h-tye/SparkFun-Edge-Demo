
#created 5/27/24


import os
import re


# Define the file path
file_path = r'path\to\model.cc'
output_path = r'desired\path\to\model.bin'


# Check if the file exists
if not os.path.exists(file_path):
    print(f"File does not exist: {file_path}")
    exit(1)


# Print the current working directory
print(f"Current working directory: {os.getcwd()}")


# Read the C array file
with open(file_path, 'r') as file:
    data = file.read()


# Extract the hex values from the C array
hex_values = re.findall(r'0x[0-9a-fA-F]+', data)


# Convert hex values to binary data
binary_data = bytearray(int(value, 16) for value in hex_values)


# Save binary data to a .bin file
with open(output_path, 'wb') as bin_file:
    bin_file.write(binary_data)


print(f'Binary file created with {len(binary_data)} bytes.')


