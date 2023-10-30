import requests

pixela_endpoint = "https://pixe.la/v1/users"


class CreateUser:
    def __init__(self, username: str, password: str):
        self.user_params = {
            "token": password,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }

    def create_user(self):
        response = requests.post(url=pixela_endpoint, json=self.user_params)
        return response.text
