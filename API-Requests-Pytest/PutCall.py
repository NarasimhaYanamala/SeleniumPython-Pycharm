import requests

head = {
    'Accept':'text/plain',
}
response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/3", headers=head)

print("before update")
print(response.status_code, response.json())


headerPut= {
    "Accept" : "test/plain",
    "Content-Type": "application/json",
}

payload = {
    "id": 4,
    "title": "string",
    "dueDate": "2024-03-21T05:56:20.922Z",
    "completed": True,   # in java it will small t
}
print("before update")
responsePut = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/12", headers=headerPut, json=payload)

print(responsePut.status_code, responsePut.json())

url= "https://fakerestapi.azurewebsites.net/api/v1/Activities"
#getResponse = requests.get(url+'/'+str(responsePut.json()["id"]), headers=head)
getResponse = requests.get(url+'/'+str(12), headers=head)
print(getResponse.json())
print("text is ", getResponse.text)
