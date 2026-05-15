import requests
from utils.config import BASE_URL

def get_all_siswa(token):
    url = f"{BASE_URL}/api/siswa"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(url, headers=headers)


def create_siswa(token, payload):
    url = f"{BASE_URL}/api/siswa"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.post(url, json=payload, headers=headers)


