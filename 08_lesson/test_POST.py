import requests
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv('password')
login = os.getenv('login')
TOKEN = os.getenv('YOUGILE_API_KEY')
NoTOKEN = os.getenv('negativtoken')


def test_create_project():
    BASE_URL = "https://ru.yougile.com/api-v2/"

    payload = {
        "title": "проект 2",
        "users": {
            '363be750-07ca-491b-b974-f59473364037': 'admin',
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    response = requests.post(f"{BASE_URL}/projects", json=payload,
                             headers=headers)
    if response.status_code == 201:
        data = response.json()
        print(f"✅ Проект создан! ID: {data.get('id')}")
    else:
        print(f"❌ Ошибка {response.status_code}: {response.text}")


def test_negative_create_project():
    BASE_URL = "https://ru.yougile.com/api-v2/"

    payload = {
        "title": "проект 2",
        "users": {
            '363be750-07ca-491b-b974-f59473364037': 'admin',
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {NoTOKEN}",
    }

    response = requests.post(f"{BASE_URL}/projects", json=payload,
                             headers=headers)

    assert response.status_code == 401, f"Ожидался 401, получен {response.
                                                                 status_code}"
    print("✅ Тест пройден: сервер вернул 401 при невалидном токене\n")
