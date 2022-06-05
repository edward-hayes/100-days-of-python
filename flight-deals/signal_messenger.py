import base64
import requests

URL = 'http://192.168.86.100:8888/v2/send'


class Signal():
    def __init__(self, api_url, from_number) -> None:
        self.url = api_url
        self.from_number = from_number

    def send_text(self, recipients: list[str], message: str):
        parameters = {
            "message" : message,
            "number" : self.from_number,
            "recipients": recipients
        }
        self.send(parameters)

    def send_photo(self, image_path: str, recipients: list[str], message: str):
        with open(image_path, "rb") as file:
            image_bytes = file.read()
        image_b64 = base64.b64encode(image_bytes).decode("utf8")
        parameters = {
            "base64_attachments" : [image_b64],
            "message" : message,
            "number" : self.from_number,
            "recipients": recipients
        }
        self.send(parameters)

    def send(self,parameters):
        response = requests.post(
            url= self.url,
            json=parameters
        )
        print(response.json())