# -----------------------------------------------------------
# working case: Content-Length


# Read the content of the fiddler log file
with open('79_Full_Succeeded.txt', 'rb') as file:
    content = file.read()

# Find the start of the binary data
binary_data_start = content.find(b'PK\x03\x04') # Excel start with PK\x03\x04

# Extract the binary data
binary_data = content[binary_data_start:]

# Save the binary data to an Excel file
with open('Content-Length_working.xlsx', 'wb') as excel_file:
    excel_file.write(binary_data)



#------------------------------------------------------------
# non-working case: Transfer-Encoding: chunked
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding

# Read the content of the fiddler log file
with open('31_Full_failed_excel.txt', 'rb') as file:
    content = file.read()

# Find the start of the response body, 
binary_data_start = content.find(b'40000\x0D\x0A')

# Extract the binary data
binary_chunks = content[binary_data_start:]

binary_data = b''

while True:
    rn_index = binary_chunks.find(b'\x0D\x0A') #\r\n
    if rn_index == -1: 
        break

    chunkSize = int(binary_chunks[:rn_index], 16) #at the beginning of each chunk you need to add the length of the current chunk in hexadecimal format
    if chunkSize == 0:
        break
    
    binary_data += binary_chunks[rn_index+2:rn_index+2+chunkSize] # chunkSizeHex\r\nChunk_size_length_of_Data\r\n, chunkSize does not include the \r\n at end of data
    
    binary_chunks = binary_chunks[rn_index+2+chunkSize+2:]

    if binary_chunks.find(b'0\x0D\x0A') == 0:
        break
    

# Save the binary data to an Excel file
with open('chunked_non_working.xlsx', 'wb') as excel_file:
    excel_file.write(binary_data)
