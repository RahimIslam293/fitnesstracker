import requests
import dotenv
import os

dotenv.load_dotenv()
BASE_URL = "https://trackapi.nutritionix.com/v2/natural"
NUTRIENT_URL = f"{BASE_URL}/nutrients"
EXERCISE_URL = f"{BASE_URL}/exercise"
X_APP_ID = os.getenv("APP_ID")
X_API_KEY = os.getenv("API_KEY")
print(X_APP_ID)
print(X_API_KEY)
X_REMOTE_ID = "0"

headers = {
    "x-app-id": X_APP_ID,
    "x-api-key": X_API_KEY,
    "x-remote-key": X_REMOTE_ID
}


query = input("What workout did you do today?")

ntx_query = {
    "query": query
}

resp = requests.post(url=EXERCISE_URL, headers=headers, json=ntx_query)
resp.raise_for_status()
print(resp.text)