import json

import pytest
import requests
import jsonpath


class TestGetUser:
    base_url = "https://reqres.in/api"

    @pytest.fixture(autouse=True)
    def setup(self):
        self.session = requests.Session()

    # validate get single user response
    def test_get_single_user(self):
        user_id = 2
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url)

        # validate the response code
        assert response.status_code == 200, "Response code is not 200. The response code is " + str(
            response.status_code)
        # parse response to json
        json_object = json.loads(response.content)
        json_formatted_response = json.dumps(json_object, indent=2)
        print(json_formatted_response)

        # validate the response using json path
        data = jsonpath.jsonpath(json_object, 'data')

        assert data[0]['id'] == 25
        assert data[0]['email'] == "janet.weaver@reqres.in"
        assert data[0]['first_name'] == "Janet"
        assert data[0]['last_name'] == "Weaver"
        assert data[0]['avatar'] == "https://reqres.in/img/faces/2-image.jpg"

    # validate get list of users response
    def test_get_list_users(self):
        page_number = 2
        url = f"{self.base_url}/users?page={page_number}"

        response = requests.get(url)

        # validate response code
        assert response.status_code == 200, "Response code is not 200. The response code is " + str(
            response.status_code)

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
        assert jsonpath.jsonpath(json_object, 'page')[0] == 2
        assert jsonpath.jsonpath(json_object, 'per_page')[0] == 6
        assert jsonpath.jsonpath(json_object, 'total')[0] == 12
        assert jsonpath.jsonpath(json_object, 'total_pages')[0] == 2


if __name__ == "__main__":
    pytest.main([__file__])
