import os
import ast
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

APPID = os.environ.get("APPID")
APPKEY = os.environ.get("APPKEY")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

WEIGHT = os.environ.get("WEIGHT")
HEIGHT = os.environ.get("HEIGHT")
AGE = os.environ.get("AGE")
GENDER = os.environ.get("Gender")

SHEET_HEADER = ast.literal_eval(os.environ.get("HEADER"))

params = {
    "query": "",
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id": APPID,
    "x-app-key": APPKEY,
    "Content-Type": "application/json"
}

def input_exercise():
    exercise = input("Exercise Log: ")
    params["query"] = exercise
    response = requests.post(EXERCISE_ENDPOINT, json=params, headers=headers)
    return response.json()

def write_to_sheet():
    data = input_exercise()
    for exercise in data["exercises"]:
        payload = {
            "sheet1":{
                "date": datetime.today().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%H:%M"),
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        response = requests.post(SHEET_ENDPOINT, json=payload, headers=SHEET_HEADER)
        print(response.text)

write_to_sheet()