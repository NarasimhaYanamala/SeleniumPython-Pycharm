import json

import requests

head = {
    'accept': 'text/plain',
    'Content-Type': 'application/json',
}

payload = {
    "id": 100,
    "title": "string",
    "dueDate": "2024-03-21T05:56:20.922Z",
    "completed": True,
}
response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json=payload)

# Method 2
response2 = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, data=json.dumps(payload))
r = response2.json()
print("response 2 'ID :", r.get('id'))
r1 = response2.text
print(r1)


#Method 3
# payload =json.dumps( {
#     "id": 100,
#     "title": "string",
#     "dueDate": "2024-03-21T05:56:20.922Z",
#     "completed": True,
# })
#response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, data=payload

#print(response.text)

print("Json Response is: ", response.json())
print("id is: ", response.json()["id"])
print(response.status_code)

assert response.status_code == 200
data=response.json()

