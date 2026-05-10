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
