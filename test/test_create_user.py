import json
import requests


# Validate new user creation
def test_create_user():
    url = "https://reqres.in/api/users"

    file = open('utils/new_user_test_data.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)

    # validate the response code
    assert response.status_code == 201, "Response code is not 201. The response code is " + str(response.status_code)

    # validate the response data against the request data
    assert response.json()['name'] == request_json['name']
    assert response.json()['job'] == request_json['job']








