import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.datetime.now().strftime("%Y%m%d")


class PostPixel:
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
        response = requests.post(url=f"{self.post_pixel_endpoint}/{graph_id}",
                                 json=self.post_pixel_config,
                                 headers=self.headers)
        return response.text
