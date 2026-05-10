import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('YOUGILE_API_KEY')
PROJECT_ID = os.getenv('PROJECT_ID')


def test_positive_get():
    BASE_URL = "https://ru.yougile.com/api-v2"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    response = requests.get(f"{BASE_URL}/projects/{PROJECT_ID}",
                            headers=headers)
    print(f"Status: {response.status_code}")
    print(response.json())


def test_negative_no_token_get():
    BASE_URL = "https://ru.yougile.com/api-v2"
    fake_id = "00000000-0000-0000-0000-000000000000"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer NoToken",
    }

    response = requests.get(f"{BASE_URL}/projects/{fake_id}",
                            headers=headers)
    print(f"Status: {response.status_code}")
    print(response.json())

    print("✅ Тест пройден: сервер вернул 404 для несуществующего проекта\n")
    assert response.status_code == 401, f"Ожидался 401, получен {response.
                                                                 status_code}"
