import requests

pixela_endpoint = "https://pixe.la/v1/users"


class CreateGraph:
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
        response = requests.post(url=self.graph_endpoint, json=self.graph_config, headers=self.headers)
        return response.text
