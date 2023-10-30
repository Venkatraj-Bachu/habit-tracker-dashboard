import requests

pixela_endpoint = "https://pixe.la/v1/users"


class DeletePixel:
    def __init__(self, username, password):
        self.delete_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/"

        self.headers = {
            "X-USER-TOKEN": password,
        }

    def delete_pixel(self, graph_id: str, date: str):
        response = requests.delete(url=f"{self.delete_pixel_endpoint}/{graph_id}/{date}",
                                   headers=self.headers)

        return response