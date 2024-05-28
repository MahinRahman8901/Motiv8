"""
Python script for extracting exercise and calories burnt data
"""

# TODO: match data from exercises and calories burnt
# TODO: if cannot match, allow input for calories burnt
# TODO: combine the datasets and load onto database
# TODO: transform will include calculating calories burnt given a time duration
# TODO: create visualizations for dataset
# TODO: create login system (look at weather API from dom)
# TODO: update extract to return more than 1 exercise, pick from a list and upload that to database

from os import environ as ENV

import requests
from dotenv import load_dotenv


def get_queries() -> dict:
    """Request an input to get a query object"""

    search = {}

    muscle_group = ['abdominals',
                    'abductors',
                    'adductors',
                    'biceps',
                    'calves',
                    'chest',
                    'forearms',
                    'glutes',
                    'hamstrings',
                    'lats',
                    'lower_back',
                    'middle_back',
                    'neck',
                    'quadriceps',
                    'traps',
                    'triceps']

    exercise_types = ['cardio',
                      'olympic_weightlifting',
                      'plyometrics',
                      'powerlifting',
                      'strength',
                      'stretching',
                      'strongman']

    search['name'] = input(
        "Name an exercise you would like to do. (Leave empty if none)\n")
    search['muscle'] = input(
        f"What muscle group would you like to target?\n{muscle_group}")
    search['type'] = input(
        f"What type of exercise would you like to do?\n{exercise_types}")
    search['difficulty'] = input(
        f"How difficult of a workout would you like? beginner, intermediate, expert\n")
    search['weight'] = int(input('How much do you weigh, in kg?\n'))
    search['duration'] = int(
        input('How long would you like to work out for, in minutes?\n'))

    return search


def get_exercise_information(search: dict) -> list[dict]:
    """Retrieve exercise information given a query"""

    name = search.get('name')
    muscle = search.get('muscle')
    type = search.get('type')
    difficulty = search.get('difficulty')

    api_url = f'https://api.api-ninjas.com/v1/exercises?'

    if name:
        api_url += f'&name={name}'
    if muscle:
        api_url += f'&muscle={muscle}'
    if type:
        api_url += f'&type={type}'
    if difficulty:
        api_url += f'&difficulty={difficulty}'

    response = requests.get(api_url, headers={'X-Api-Key': ENV['API_KEY']})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


def get_calories_by_exercise(search: dict) -> list[dict]:
    """Retrieve the calories burnt by an exercise"""

    name = search.get('name')
    weight = search.get('weight')
    duration = search.get('duration')

    api_url = f'https://api.api-ninjas.com/v1/caloriesburned?activity={name}'

    if weight:
        api_url += f'&weight={weight}'
    if duration:
        api_url += f'&duration={duration}'

    response = requests.get(api_url, headers={'X-Api-Key': ENV['API_KEY']})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":

    load_dotenv()

    queries = get_queries()

    print(get_calories_by_exercise(queries))

    # print(get_exercise_information(queries))
