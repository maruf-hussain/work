import http.client

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
conn.request("GET", '/users')
response = conn.getresponse()
print(response.status)
print(response.read())