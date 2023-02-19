import urllib.request
import urllib.parse
import json

data = {'key1': 'value1', 'key2': 'value2'}

query_string = urllib.parse.urlencode(data)

# Construct the URL with the query string
url = 'https://lanugagelink.pythonanywhere.com/test' + query_string

# Send a GET request to the URL
response = urllib.request.urlopen(url)

# Read the response data
response_data = response.read()

# Decode the response data from bytes to string
response_text = response_data.decode('utf-8')

# Parse the response data as JSON
response_json = json.loads(response_text)

# Print the response data
print(response_json)