"""
Python script for extracting exercise and calories burnt data
"""

# TODO: match data from exercises and calories burnt
# TODO: if cannot match, allow input for calories burnt
# TODO: combine the datasets and load onto database
# TODO: transform will include calculating calories burnt given a time duration
# TODO: create visualizations for dataset
# TODO: create login system (look at weather API from dom)
# TODO: take the workout instructions and make GPT briefly describe the workout plan.

from os import environ as ENV

import requests
from dotenv import load_dotenv


def get_exercises_by_name(search: str) -> list[dict]:
    """Retrieve the exercise information by name"""

    api_url = f'https://api.api-ninjas.com/v1/exercises?name={search}'
    response = requests.get(api_url, headers={'X-Api-Key': ENV['API_KEY']})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


def get_exercises_by_muscle(search: str) -> list[dict]:
    """Retrieve the exercise information by muscle"""

    api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={search}'
    response = requests.get(api_url, headers={'X-Api-Key': ENV['API_KEY']})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


def get_exercises_by_type(search: str) -> list[dict]:
    """Retrieve the exercise information by type"""

    api_url = f'https://api.api-ninjas.com/v1/exercises?type={search}'
    response = requests.get(api_url, headers={'X-Api-Key': ENV['API_KEY']})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


def get_calories_by_exercise(search: str, weight=None, duration=None) -> list[dict]:
    """Retrieve the calories burnt by an exercise"""

    if weight and duration:
        api_url = f'https://api.api-ninjas.com/v1/caloriesburned?activity={search}&weight={weight}&duration={duration}'
    if weight:
        api_url = f'https://api.api-ninjas.com/v1/caloriesburned?activity={search}&weight={weight}'
    if duration:
        api_url = f'https://api.api-ninjas.com/v1/caloriesburned?activity={search}&duration={duration}'
    else:
        api_url = f'https://api.api-ninjas.com/v1/caloriesburned?activity={search}'

    response = requests.get(api_url, headers={'X-Api-Key': ENV['API_KEY']})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":

    load_dotenv()
