import json
import requests
import jsonpath


def test_get_request():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    # parse response to json
    json_object = json.loads(response.content)
    json_formatted_response = json.dumps(json_object, indent=2)
    #print(json_formatted_response)

    # fetch value from the response using json path
    pages = jsonpath.jsonpath(json_object, 'total_pages')
    assert pages[0] == 2
    print(pages[0])

    data = jsonpath.jsonpath(json_object, 'data')
    json_formatted_data = json.dumps(data, indent=2)
    print(json_formatted_data)




