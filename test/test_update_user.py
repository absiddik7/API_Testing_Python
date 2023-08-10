import json
import requests


def test_update_user():
    url = "https://reqres.in/api/users/2"
    updated_data = {
        "name": "James Bond",
        "job": "Spy"
    }
    response = requests.put(url, updated_data)

    # validate the response code
    assert response.status_code == 200, "Response code is not 200. The response code is " + str(response.status_code)

    # validate the response data against the request data
    assert response.json()['name'] == updated_data['name']
    assert response.json()['job'] == updated_data['job']
