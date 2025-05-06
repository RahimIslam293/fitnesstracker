import requests
import dotenv
import os
import datetime as dt

dotenv.load_dotenv()
BASE_URL = "https://trackapi.nutritionix.com/v2/natural"
SHEETY_URL = "https://api.sheety.co/354c60151bffcfc5fb8b6f35cc5c5dcc/myWorkouts/workouts"
NUTRIENT_URL = f"{BASE_URL}/nutrients"
EXERCISE_URL = f"{BASE_URL}/exercise"
GENDER= "male"
WEIGHT_KG = 88
HEIGHT_CM = 170
AGE = 32
X_APP_ID = os.getenv("APP_ID")
X_API_KEY = os.getenv("API_KEY")
X_REMOTE_ID = "0"


def build_sheety_entry(json_resp:dict) -> dict:
    global today
    global today_time
    exercise = json_resp["exercises"][0]["name"].title()
    duration = int(json_resp["exercises"][0]["duration_min"])
    calories = int(json_resp["exercises"][0]["nf_calories"])

    ntx_output = {
        "workout": {
            "date": today,
            "time": today_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
            "id":4
        }
    }
    return ntx_output

ntx_headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": X_API_KEY,
    "x-remote-key": X_REMOTE_ID
}


# query = input("What workout did you do today?")
query = "I ran three miles"


ntx_query = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE


}

#form sheety response
today = dt.datetime.today().date().strftime("%d/%m/%Y")
today_time = dt.datetime.today().time().strftime("%H:%M:%S")

print(today)
print(today_time)


resp = requests.post(url=EXERCISE_URL, headers=ntx_headers, json=ntx_query)
resp.raise_for_status()
json_resp = resp.json()
ntx_json = build_sheety_entry(json_resp)

print(ntx_json)
sheety_resp = requests.post(url=SHEETY_URL,json=ntx_json)
sheety_resp.raise_for_status()
print(sheety_resp.text)