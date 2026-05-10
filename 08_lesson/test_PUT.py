import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('YOUGILE_API_KEY')
PROJECT_ID = os.getenv('PROJECT_ID')


def test_positive_put():
    BASE_URL = "https://ru.yougile.com/api-v2"

    payload = {
        "deleted": False,
        "title": "название проекта",
        "users": {
            '363be750-07ca-491b-b974-f59473364037': 'admin',
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
    }

    response = requests.put(f"{BASE_URL}/projects/{PROJECT_ID}", json=payload,
                            headers=headers)
    if response.status_code == 200:
        print("✅ Проект обновлён!")
    else:
        print(f"❌ Ошибка {response.status_code}: {response.text}")
