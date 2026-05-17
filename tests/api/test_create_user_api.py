import pytest
import requests
from faker import Faker

fake=Faker()

def test_create_user():

    payload={
        "name":fake.name(),
        "job":fake.job(),
    }
    
    response=requests.post(
        "http://reqres.in/api/users",
        json=payload

    )
    

    response_body=response.json()
    assert response.status_code==201
    assert response_body["name"]==payload["name"]
    assert response_body["job"]==payload["job"]
    assert "id" in response_body
    assert "createdAt" in response_body
