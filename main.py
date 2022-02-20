import requests

NUTRITION_ID = "56f4204d"
NUTRITION_KEY = "0058ed8edb9817a2f81bc4886e9245fa"

nutrition_log_endpoint = "https://trackapi.nutritionix.com//v2/auth/signin"

nutrition_permissions_config = {
  "users": [
    {
      "id": "string",
      "mobile_number": "string",
      "email": "string"
    }
  ]
}

response = requests.post(url=nutrition_log_endpoint, params=nutrition_sign_in_config)

print(response.text)
