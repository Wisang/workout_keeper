import duration as duration
import requests

from datetime import datetime

NUTRITION_ID = "56f4204d"
NUTRITION_KEY = "0058ed8edb9817a2f81bc4886e9245fa"

natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/b11e9ee43e97ab01dec13f717b53914f/wisangsWorkouts/workouts"

header = {
  "x-app-id": NUTRITION_ID,
  "x-app-key": NUTRITION_KEY,
  "x-remote-user-id": "0",
}

sheety_header = {
  "workouts": {
    "name": "wisang",
    "email": "wseom7@gmail.com"
  }
}

user_answer = input("tell me which exercise you did: ")

natural_exercise_config = {
  "query": user_answer,
}

response = requests.post(url=natural_exercise_endpoint, headers=header, json=natural_exercise_config)

exercise_data = response.json()["exercises"][0]

print(exercise_data)

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H/%M/%S")

sheety_header = {
  "Content-Type": "application/json",
}

sheety_row = {
  "workout": {
    "date": today,
    "time": time,
    "exercise": f"{exercise_data['user_input']}",
    "duration": f"{exercise_data['duration_min']}",
    "calories": f"{exercise_data['nf_calories']}",
  }
}

response = requests.post(url=sheety_endpoint, json=sheety_row)
print(response.json())

