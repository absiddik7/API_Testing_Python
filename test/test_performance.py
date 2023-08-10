import pytest
import requests
import time


class TestPerformance:
    base_url = "https://reqres.in/api"

    @pytest.fixture(autouse=True)
    def setup(self):
        self.session = requests.Session()

    def test_user_list_response_time(self):
        url = f"{self.base_url}/users?page=1"

        start_time = time.time()
        response = self.session.get(url)
        end_time = time.time()

        response_time = end_time - start_time
        max_response_time = 1  # Max acceptable response time in seconds

        assert response.status_code == 200
        assert response_time <= max_response_time, f"Response time exceeded {max_response_time} seconds"

    def test_single_user_response_time(self):
        user_id = 1
        url = f"{self.base_url}/users/{user_id}"

        start_time = time.time()
        response = self.session.get(url)
        end_time = time.time()

        response_time = end_time - start_time
        max_response_time = 1  # Max acceptable response time in seconds

        assert response.status_code == 200
        assert response_time <= max_response_time, f"Response time exceeded {max_response_time} seconds"


if __name__ == "__main__":
    pytest.main([__file__])
