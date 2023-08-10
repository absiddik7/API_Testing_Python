import json

import pytest
import requests
from jsonschema import validate


class TestDataSchemaValidation:
    base_url = "https://reqres.in/api"

    @pytest.fixture(autouse=True)
    def setup(self):
        self.session = requests.session()

    # validating user list JSON data against a schema
    def test_user_list_data_json_schema_validation(self):
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

        # validate the response using json schema
        schema = json.load(open('utils/user_list_json_schema.json'))
        validate(instance=json_object, schema=schema)


if __name__ == "__main__":
    pytest.main([__file__])
