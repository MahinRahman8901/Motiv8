"""
Python script for combining and cleaning exercise and calories burnt data
"""
# TODO: get a brief instruction for each exercise w/GPT
# TODO: get an overall description of each workout plan
# TODO: configure workout plan as list of 1-5 exercises

from os import environ as ENV
import logging
import random

from dotenv import load_dotenv

from extract import (get_exercise_information,
                     get_calories_by_exercise)


def get_full_workout(search: dict) -> dict:
    """Retrieve the full details of a workout to be done/completed"""

    exercises = get_exercise_information(search)
    calories = get_calories_by_exercise(search)

    if len(exercises) > 5:
        select_exercises(exercises)

    if len(exercises) == 1:
        exercise = exercises[0]

        if exercise and calories:
            if exercise['name'].lower() in calories['name'].lower():
                exercise.update(calories)

    return exercise


def select_exercises(exercise: list[dict], num_exercises: int) -> list[dict]:
    """Retrieve full details of selected workouts"""

    workout = []
    for n in range(num_exercises):
        selected_exercise = random.choice(exercise)
        exercise.pop(n)
        workout.append(selected_exercise)

    return workout


if __name__ == "__main__":

    load_dotenv()

    exercises = get_exercise_information(
        {'name': 'running', 'difficulty': 'intermediate'})

    if exercises:
        print(select_exercises(exercises, 3))

    # print(get_full_workout({'name': 'skating'}))
