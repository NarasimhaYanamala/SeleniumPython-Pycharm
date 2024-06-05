import requests
import json
import os

head = {
    'accept': 'text/plain',
    'Content-Type': 'application/json',
}

payload ={
    "firstName": "John",
    "lastName": "doe",
    "age": 26,
    "address": {
        "streetAddress": "naist street",
        "city": ["hyd","MAN", "MUM", "DEL"],
        "postalCode": "630-0192"
    },
    "phoneNumbers":
    [
        {
            "type": "iPhone",
            "number": "0123-4567-8888"
        },
        {
            "type": "home",
            "number": "0123-4567-8910"
        }
    ]
}

# payload = {
#     "id": 100,
#     "title": "string",
#     "dueDate": "2024-03-21T05:56:20.922Z",
#     "completed": True,
# }
#response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json=payload)

print(payload)
print(payload.get('firstName'))

#print("id is: ", response.json()["id"])
#print(response.status_code)