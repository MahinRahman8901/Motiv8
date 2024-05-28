"""
Python script for combining and cleaning exercise and calories burnt data
"""
# TODO: get a brief instruction for each exercise w/GPT
# TODO: get an overall description of each workout plan
# TODO: configure workout plan as list of 1-5 exercises

from os import environ as ENV
import logging

from dotenv import load_dotenv

from extract import (get_exercises_by_name,
                     get_calories_by_exercise)


def get_full_workout(search: str, weight=None, duration=None) -> dict:
    """Retrieve the full details of a workout to be done/completed"""

    exercise = get_exercises_by_name(search)[0]
    calories = get_calories_by_exercise(search, weight, duration)[0]

    if exercise and calories:
        if exercise['name'].lower() in calories['name'].lower():
            exercise.update(calories)

    return exercise


if __name__ == "__main__":

    load_dotenv()
