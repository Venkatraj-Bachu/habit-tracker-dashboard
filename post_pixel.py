import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.datetime.now().strftime("%Y%m%d")


class PostPixel:
    """
        A class for posting data points (pixels) to a graph on the Pixela API.

        This class simplifies the process of posting data points to a specific graph by providing
        a convenient way to send a POST request to the Pixela API with the required pixel data.

        Args:
            username (str): The username of the Pixela user account.
            password (str): The user's authentication token for accessing the Pixela API.
            quantity (str): The quantity or value to be posted on the graph.
            date (str, optional): The date for which the pixel should be posted. It should be
                in the "YYYYMMDD" format. If not provided, the current date is used.

        Attributes:
            username (str): The username of the Pixela user account.
            post_pixel_endpoint (str): The URL for posting pixels on the user's graph.
            post_pixel_config (dict): A dictionary containing the pixel data, including:
                - 'date': The date for which the pixel should be posted.
                - 'quantity': The quantity or value to be posted.
            headers (dict): Headers for the HTTP request, including the user's authentication token.

        Methods:
            post_pixel(graph_id):
                Posts a data point (pixel) to the specified graph on the Pixela API.
    """

    def __init__(self, username: str, password: str,
                 quantity: str, date: str = today):
        self.username = username
        self.post_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs"

        self.post_pixel_config = {
            'date': date,
            'quantity': quantity,
        }

        self.headers = {
            "X-USER-TOKEN": password,
        }

    def post_pixel(self, graph_id):
        """
            Post a data point (pixel) to a specific graph on the Pixela API.

            Args:
                graph_id (str): The ID of the graph to which the pixel should be posted.

            Returns:
                str: The response text from the POST request, typically containing information
                about the success of posting the pixel or any error messages.
        """

        response = requests.post(url=f"{self.post_pixel_endpoint}/{graph_id}",
                                 json=self.post_pixel_config,
                                 headers=self.headers)
        return response.text
