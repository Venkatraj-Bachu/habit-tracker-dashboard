import requests

pixela_endpoint = "https://pixe.la/v1/users"


class UpdatePixel:
    def __init__(self, username, password, graph_id):
        self.update_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

        self.headers = {
            "X-USER-TOKEN": password,
        }

    def update_pixel(self, date, new_quantity):
        update_pixel_config = {
            'quantity': new_quantity,
        }
        response = requests.put(url=f"{self.update_pixel_endpoint}/{date}",
                                json=update_pixel_config,
                                headers=self.headers)

        return response
