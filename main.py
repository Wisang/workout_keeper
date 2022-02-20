import requests
import os
from datetime import datetime

NUTRITION_ID = os.environ["NT_APP_ID"]
NUTRITION_KEY = os.environ["NT_API_KEY"]

# NUTRITION_ID = "56f4204d"
# NUTRITION_KEY = "0058ed8edb9817a2f81bc4886e9245fa"
SHEETY_PASS = "bnVsbDpudWxs"
SHEETY_AUTH_BASIC = "d2lzYW5nOmJuVnNiRHB1ZFd4cw"

natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheety_endpoint = "https://api.sheety.co/b11e9ee43e97ab01dec13f717b53914f/wisangsWorkouts/workouts"
sheety_endpoint = os.environ["SHEET_ENDPOINT"]
sheety_header = {
  "Authorization": "Bearer {os.environ['TOKEN']}"
}


header = {
  "x-app-id": NUTRITION_ID,
  "x-app-key": NUTRITION_KEY,
  "x-remote-user-id": "0",
}

user_answer = input("tell me which exercise you did: ")

natural_exercise_config = {
  "query": user_answer,
}

response = requests.post(url=natural_exercise_endpoint, headers=header, json=natural_exercise_config)

exercise_data = response.json()["exercises"]

print(exercise_data)

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in exercise_data:
  sheety_row = {
    "workout": {
      "date": today,
      "time": time,
      "exercise": f"{exercise['user_input']}",
      "duration": f"{exercise['duration_min']}",
      "calories": f"{exercise['nf_calories']}",
    }
  }

  response = requests.post(url=sheety_endpoint, headers=sheety_header, json=sheety_row)
  print(response.json())

