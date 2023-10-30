import requests

pixela_endpoint = "https://pixe.la/v1/users"


class CreateUser:
    """
        A class for creating a new user on the Pixela API.

        This class simplifies the process of user registration by providing a convenient way to
        send a POST request to the Pixela API with the required user parameters.

        Args:
            username (str): The desired username for the new user account.
            password (str): The user's password for authentication.

        Attributes:
            user_params (dict): A dictionary containing user registration parameters, including:
                - 'token': The user's password for authentication.
                - 'username': The desired username for the new user account.
                - 'agreeTermsOfService': A string indicating agreement to the terms of service ('yes' or 'no').
                - 'notMinor': A string indicating that the user is not a minor ('yes' or 'no').

        Methods:
            create_user():
                Sends a POST request to the Pixela API to create a new user account.
    """

    def __init__(self, username: str, password: str):
        self.user_params = {
            "token": password,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }

    def create_user(self):
        """
            Create a new user account on the Pixela API.

            Sends a POST request to the Pixela API with the user parameters provided during
            object initialization. This method registers a new user with the specified username
            and password, agreeing to the terms of service and confirming that the user is not a minor.

            Returns:
                str: The response text from the POST request, typically containing information
                about the success of user creation or any error messages.
        """

        response = requests.post(url=pixela_endpoint, json=self.user_params)
        return response.text
