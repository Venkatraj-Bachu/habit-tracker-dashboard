import requests

pixela_endpoint = "https://pixe.la/v1/users"


class CreateGraph:
    """
        A class for creating a new graph on the Pixela API.

        This class simplifies the process of creating a new graph by providing a convenient way to
        send a POST request to the Pixela API with the required graph configuration.

        Args:
            username (str): The username of the Pixela user account.
            password (str): The user's authentication token for accessing the Pixela API.
            graph_id (str): The ID for the new graph.
            graph_name (str): The name of the new graph.
            unit_measure (str): The unit of measurement for the data in the graph.
            data_type (str): The type of data for the graph (e.g., 'int', 'float').
            color (str, optional): The color of the graph (default is 'shibafu').

        Attributes:
            graph_endpoint (str): The URL for creating a new graph in the user's profile.
            graph_config (dict): A dictionary containing the graph configuration, including:
                - 'id': The ID for the new graph.
                - 'name': The name of the new graph.
                - 'unit': The unit of measurement for the data.
                - 'type': The type of data (e.g., 'int', 'float').
                - 'color': The color of the graph.
            headers (dict): Headers for the HTTP request, including the user's authentication token.

        Methods:
            create_graph():
                Creates a new graph on the Pixela API with the specified configuration.
    """

    def __init__(self, username: str, password: str,
                 graph_id: str, graph_name: str,
                 unit_measure: str, data_type: str,
                 color: str ="shibafu"):

        self.graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
        self.graph_config = {
            "id": graph_id,
            "name": graph_name,
            "unit": unit_measure,
            "type": data_type,
            "color": color,
        }

        self.headers = {
            "X-USER-TOKEN": password,
        }

    def create_graph(self):
        """
            Create a new graph on the Pixela API with the specified configuration.

            Returns:
                str: The response text from the POST request, typically containing information
                about the success of graph creation or any error messages.
        """
        response = requests.post(url=self.graph_endpoint, json=self.graph_config, headers=self.headers)
        return response.text
