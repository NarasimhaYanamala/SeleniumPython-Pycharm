import requests
import json

head = {
    'accept': 'text/plain',
    'Content-Type': 'application/json',
}

file = open('activity.json')
json_payload = json.load(file)
#json_payload1 = json.dump(file)

# if using data instead of json, use json.dumps method to load payload

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json=json_payload)

#response1 = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, data=json.dump(json_payload))

print(response.json())
print(response.status_code)

assert response.status_code == 200
data=response.json()
