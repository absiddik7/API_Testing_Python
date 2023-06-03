import json
import requests
import jsonpath


def test_get_list_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    assert response.status_code == 200, "Response code is not 200. The response code is " + str(response.status_code)

    # parse response to json
    json_object = json.loads(response.content)
    json_formatted_response = json.dumps(json_object, indent=2)
    print(json_formatted_response)

    # fetch value from the response using json path
    pages = jsonpath.jsonpath(json_object, 'total_pages')
    assert pages[0] == 2
    print(pages[0])

    data = jsonpath.jsonpath(json_object, 'data')
    json_formatted_data = json.dumps(data, indent=2)
    print(json_formatted_data)

    # validate the response using json path
    assert jsonpath.jsonpath(json_object, 'pages') == 2
    assert jsonpath.jsonpath(json_object, 'per_page') == 6
    assert jsonpath.jsonpath(json_object, 'total') == 12
    assert jsonpath.jsonpath(json_object, 'total_pages') == 2


def test_get_single_user():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)

    assert response.status_code == 200, "Response code is not 200. The response code is " + str(response.status_code)

    # parse response to json
    json_object = json.loads(response.content)
    json_formatted_response = json.dumps(json_object, indent=2)
    print(json_formatted_response)

    # validate the response using json path
    data = jsonpath.jsonpath(json_object, 'data')

    assert data[0]['id'] == 2
    assert data[0]['email'] == "janet.weaver@reqres.in"
    assert data[0]['first_name'] == "Janet"
    assert data[0]['last_name'] == "Weaver"
    assert data[0]['avatar'] == "https://reqres.in/img/faces/2-image.jpg"
