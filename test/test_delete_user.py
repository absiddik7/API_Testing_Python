import requests


# validate user deletion
def test_delete_user():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)

    # validate response code
    assert response.status_code == 204, "Response code is not 204. The response code is " + str(response.status_code)
