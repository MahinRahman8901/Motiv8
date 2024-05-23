"""
Python script for loading transformed exercise and calories burnt data
"""

from os import environ as ENV
import logging
from datetime import timedelta
from dotenv import load_dotenv

from psycopg2 import connect, OperationalError
from psycopg2.extras import execute_values, RealDictCursor
from transform import get_full_workout


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


def get_exercise_id_by_name(conn, exercise: dict) -> None:
    """
    Retrieve the exercise id if it already exists in the database by name.
    """

    exercise_name = exercise.get('name')

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT exercise_id
                FROM exercise
                WHERE exercise_name = %s
                """,
                (exercise_name,)
            )
            result = cur.fetchone()
        return result['exercise_id'] if result else None
    except OperationalError:
        logging.error("Could not query database for id")


def upload_exercise(conn, exercise: dict) -> None:
    """
    Uploads transformed exercise to a given database. 
    """
    ex_name = exercise.get('name')
    ex_type = exercise.get('type').title()
    ex_desc = exercise.get('instructions')
    ex_calories = exercise.get('total_calories')
    duration = str(timedelta(minutes=exercise.get('duration_minutes')))
    difficulty = exercise.get('difficulty')
    muscle_group = exercise.get('muscle')

    sql_query = """
                INSERT INTO exercise
                    (exercise_name, exercise_type, exercise_desc, calories_burnt, duration, difficulty, muscle_group)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s);
                """

    params = (ex_name, ex_type, ex_desc, ex_calories,
              duration, difficulty, muscle_group)
    try:
        with conn.cursor() as cur:
            cur.execute(sql_query, params)
            conn.commit()
            logging.info('Uploaded exercises successfully to database')
    except OperationalError:
        logging.error('Unsuccessful attempt to upload to database.')


def upload_data(conn, data) -> None:
    """
    Uploads transformed exercise to a given database. 
    Tries to obtain the keys of existing data; if it does not exist,
    uploads the data.
    """

    exercise_id = get_exercise_id_by_name(conn, data)
    if exercise_id is None:
        upload_exercise(conn, data)


if __name__ == "__main__":

    load_dotenv()

    conn = get_db_connection()

    workout = get_full_workout('skating', 100, 30)

    upload_data(conn, workout)
