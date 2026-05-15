import requests
from utils.config import BASE_URL

def login(email, password):
    url = f"{BASE_URL}/api/auth/login"

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(url, json=payload)

    # Debug dulu (biar lu ngerti response)
    print("LOGIN RESPONSE:", response.status_code, response.text)

    assert response.status_code == 200, f"Login gagal: {response.text}"

    data = response.json()

    # Handle kemungkinan struktur beda
    if "token" in data:
        return data["token"]
    elif "data" in data and "token" in data["data"]:
        return data["data"]["token"]
    else:
        raise AssertionError(f"Token tidak ditemukan di response: {data}")
    
    