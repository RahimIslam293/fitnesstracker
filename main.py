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
print(EXERCISE_URL)
X_REMOTE_ID = "0"

ntx_headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": X_API_KEY,
    "x-remote-key": X_REMOTE_ID
}


#query = input("What workout did you do today?")
query = "I ran three miles"


ntx_query = {
    "query": query
}

resp = requests.post(url=EXERCISE_URL, headers=ntx_headers, json=ntx_query)
print(resp.text)