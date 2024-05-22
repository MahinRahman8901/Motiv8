"""
Python script for combining and cleaning exercise and calories burnt data
"""
from os import environ as ENV
import logging

from dotenv import load_dotenv
from psycopg2 import connect, OperationalError
from psycopg2.extras import execute_values, RealDictCursor

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


def get_db_connection():
    """
    Gets a connection to the specified database
    """
    load_dotenv()
    try:
        conn = connect(
            host=ENV["DATABASE_IP"],
            database=ENV["DATABASE_NAME"],
            cursor_factory=RealDictCursor)
        logging.info('Connected to database successfully')
        return conn
    except OperationalError as err:
        logging.error('Connection attempt to database unsuccessful. %s', err)
        return None


if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection()

    workout = get_full_workout('skating', 100, 30)

    try:
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT 'hi'
                        """)
            result = cur.fetchone()
        print(result)
    except TypeError:
        print(1)
