import requests

pixela_endpoint = "https://pixe.la/v1/users"


class UpdatePixel:
    """
        A class for updating the quantity of a specific pixel on a graph in the Pixela API.

        This class simplifies the process of updating the value of a pixel on a particular graph
        by providing a convenient way to send a PUT request to the Pixela API with the new quantity.

        Args:
            username (str): The username of the Pixela user account.
            password (str): The user's authentication token for accessing the Pixela API.
            graph_id (str): The ID of the graph to which the pixel belongs.

        Attributes:
            update_pixel_endpoint (str): The URL for updating a pixel on the specified graph.
            headers (dict): Headers for the HTTP request, including the user's authentication token.

        Methods:
            update_pixel(date, new_quantity):
                Updates the quantity of a pixel on the specified date for a specific graph.
    """
    def __init__(self, username, password, graph_id):
        self.update_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

        self.headers = {
            "X-USER-TOKEN": password,
        }

    def update_pixel(self, date, new_quantity):
        """
            Update the quantity of a pixel on a specific date for a specified graph on the Pixela API.

            Args:
                date (str): The date of the pixel to be updated in the "YYYYMMDD" format.
                new_quantity (str): The new quantity or value to be assigned to the pixel.

            Returns:
                requests.Response: The response object from the PUT request, which can be used
                to check the status of the update (success or failure).
        """
        update_pixel_config = {
            'quantity': new_quantity,
        }
        response = requests.put(url=f"{self.update_pixel_endpoint}/{date}",
                                json=update_pixel_config,
                                headers=self.headers)

        return response
