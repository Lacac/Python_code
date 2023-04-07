import slack_sdk
import os
import time
import requests
from slack_sdk.errors import SlackApiError

# SLACK_TOKEN = 'xoxb-2710253165813-4001441352402-U4qCy3h56Rd0udmtHnSENg9D'
SLACK_TOKEN = 'xoxb-3998484931301-4025161047312-YmWB0zc9x4ttM4UMvBJTBjjb'


def get_image():
    response = requests.get('https://thecatapi.com/api/images/get?format=src&type=gif')
    f = open('./img.jpg', 'wb')
    for chunk in response.iter_content():
        f.write(chunk)
    return os.path.join(os.getcwd(), 'img.jpg')


class CatBot:
    def __init__(self, token, channel_id):
        self.client= slack_sdk.WebClient(token=token)
        self.channel_id = channel_id

    def upload_image(self, img_path):
        try:
            response = self.client.files_upload(file=img_path, channels=self.channel_id)
        except SlackApiError as e:
            assert e.response['ok'] is False
            assert e.response['error']
            print(f"Got an error: {e.response['error']}")


if __name__ == '__main__':
    cat_bot = CatBot(SLACK_TOKEN, '#test')
    while True:
        cat_bot.upload_image(get_image())
        print("upload success")
        time.sleep(5)
