import requests
import json


def get_photos_rover(api_key: str) -> dict:
    rover_data = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/latest_photos?api_key="
                              f"{api_key}")
    jsondata = json.loads(rover_data.text)
    return jsondata['latest_photos']


def get_photos_space(api_key: str) -> list:
    space_data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}&count=10")
    jsondata = json.loads(space_data.text)
    return jsondata


