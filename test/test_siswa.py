import pytest
from api.auth import login
from api.siswa_api import get_all_siswa, create_siswa
import random


EMAIL = "eco@gmail.com"
PASSWORD = "Test123!@"

@pytest.fixture
def token():
    return login(EMAIL, PASSWORD)


# Login Success
def test_login_success():
    token = login(EMAIL, PASSWORD)
    assert token is not None


# Get All Siswa
def test_get_all_siswa():
    token = login(EMAIL, PASSWORD)
    response = get_all_siswa(token)

    data = response.json()

    assert response.status_code == 200
    assert "data" in data
    assert "data" in data["data"]

    siswa_list = data["data"]["data"]

    assert isinstance(siswa_list, list)


# Create Siswa
def test_create_siswa(token):
    payload = {
        "nama": "Budiono Wongsi",
        ""nis": str(random.randint(1000000000, 9999999999)),
        "kelas": "X-IPA-2",
        "jurusan": "IPA",
        "email": "wongso@mail.com",
        "alamat": "Bandung"
    }

    response = create_siswa(token, payload)

    print("CREATE RESPONSE:", response.status_code, response.text)

    assert response.status_code in [200, 201]

    data = response.json()
    assert data["success"] == True


# Get Siswa lagi (validasi data tetap ada)
def test_get_all_siswa_again():
    token = login(EMAIL, PASSWORD)
    response = get_all_siswa(token)

    assert response.status_code == 200


# 5. Token valid check
def test_token_access():
    token = login(EMAIL, PASSWORD)
    assert len(token) > 10


# ❌ 6. NEGATIVE TEST (tanpa token)
def test_get_siswa_without_token():
    response = get_all_siswa(token="")

    assert response.status_code in [401, 403]
    
    
    
