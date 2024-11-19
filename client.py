import requests

proxies = {
    # 'http': 'http://127.0.0.1:8888',
    # 'https': 'http://127.0.0.1:8888',
}

url = 'http://127.0.0.1:5000/EQ06.xlsx'
response = requests.get(url, verify=False, proxies=proxies)

# Save the Excel file
with open('downloaded_EQ06_via_code.xlsx', 'wb') as file:
    file.write(response.content)

# Print the response headers
print(url)
print('Content-Length:', response.headers.get('Content-Length'))
print('Transfer-Encoding:', response.headers.get('Transfer-Encoding'))


#-----------
print('------------------------')


url = 'http://127.0.0.1:5000/chunks/EQ06.xlsx'
response = requests.get(url, verify=False, proxies=proxies)

# Save the Excel file
with open('downloaded_chunks_EQ06_via_code.xlsx', 'wb') as file:
    file.write(response.content)

# Print the response headers
print(url)
print('Content-Length:', response.headers.get('Content-Length'))
print('Transfer-Encoding:', response.headers.get('Transfer-Encoding'))