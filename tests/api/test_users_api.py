import requests
import pytest

@pytest.mark.api

def test_get_users():
    response=requests.get(

        "https://jsonplaceholder.typicode.com/users"

        )
    response_body=response.json()
    assert response.status_code==200
    assert len(response_body)>0
    assert response_body[0]["name"]=="Leanne Graham"