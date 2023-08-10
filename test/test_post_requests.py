import json
import requests
import jsonpath


def test_create_user():
    url = "https://reqres.in/api/users"

    file = open('test/newUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201, "Response code is not 201. The response code is " + str(response.status_code)
    print(response.content)


    # # parse response to json
    # json_object = json.loads(response.content)
    # json_formatted_response = json.dumps(json_object, indent=2)
    # print(json_formatted_response)
    #
    # # validate the response using json path
    # data = jsonpath.jsonpath(json_object, 'data')
    #
    # assert data[0]['id'] == 4
    # assert data[0]['email'] == ""


    # open json file newUser.json




