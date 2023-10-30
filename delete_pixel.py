import requests

pixela_endpoint = "https://pixe.la/v1/users"


class DeletePixel:
    """
        A class for deleting a specific pixel from a graph in the Pixela API.

        This class simplifies the process of deleting a pixel from a specified graph by providing
        a convenient way to send a DELETE request to the Pixela API.

        Args:
            username (str): The username of the Pixela user account.
            password (str): The user's authentication token for accessing the Pixela API.

        Attributes:
            delete_pixel_endpoint (str): The base URL for deleting pixels on the user's graphs.
            headers (dict): Headers for the HTTP request, including the user's authentication token.

        Methods:
            delete_pixel(graph_id, date):
                Deletes a specific pixel from a specified graph on the Pixela API.
    """

    def __init__(self, username, password):
        self.delete_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/"

        self.headers = {
            "X-USER-TOKEN": password,
        }

    def delete_pixel(self, graph_id: str, date: str):
        """
            Delete a specific pixel from a specified graph on the Pixela API.

            Args:
                graph_id (str): The ID of the graph from which the pixel should be deleted.
                date (str): The date of the pixel to be deleted in the "YYYYMMDD" format.

            Returns:
                requests.Response: The response object from the DELETE request, which can be used
                to check the status of the deletion (success or failure).
        """
        response = requests.delete(url=f"{self.delete_pixel_endpoint}/{graph_id}/{date}",
                                   headers=self.headers)

        return response
