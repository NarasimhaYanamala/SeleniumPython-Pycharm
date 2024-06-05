import requests
import pytest

def test_postreq_validation():
    head = {
        'Content-Type': 'application/json',
    }

    baseURL = "https://reqres.in"
    response=requests.get(url=str(baseURL+'/api/users/2'), headers=head)

    print(response.json())
    print(response.status_code)

    assert response.status_code == 200
    data=response.json()
    print("data is",data )

