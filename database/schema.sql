DROP TABLE IF EXISTS workout_plan;
DROP TABLE IF EXISTS exercise;
DROP TABLE IF EXISTS app_user;

CREATE TABLE app_user(
    user_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    dob TIMESTAMP NOT NULL,
    height SMALLINT NOT NULL,
    weight SMALLINT NOT NULL,
    email TEXT
);

CREATE TABLE exercise(
    exercise_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    exercise_name VARCHAR(100) UNIQUE NOT NULL,
    exercise_type VARCHAR(30) NOT NULL,
    exercise_desc text NOT NULL,
    calories_burnt INT NOT NULL,
    duration TIME NOT NULL,
    difficulty VARCHAR(15) NOT NULL,
    muscle_group VARCHAR(30) NOT NULL
);

CREATE TABLE workout_plan(
    workout_plan_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    workout_name VARCHAR(100) NOT NULL,
    workout_desc TEXT NOT NULL,
    user_id BIGINT,
        FOREIGN KEY (user_id) REFERENCES app_user(user_id),
    exercise_1_id INT NOT NULL,
        FOREIGN KEY (exercise_1_id) REFERENCES exercise(exercise_id),
    exercise_2_id INT,
        FOREIGN KEY (exercise_2_id) REFERENCES exercise(exercise_id),
    exercise_3_id INT,
        FOREIGN KEY (exercise_3_id) REFERENCES exercise(exercise_id),
    exercise_4_id INT,
        FOREIGN KEY (exercise_4_id) REFERENCES exercise(exercise_id),
    exercise_5_id INT,
        FOREIGN KEY (exercise_5_id) REFERENCES exercise(exercise_id)
);

-- Inserting data into user table
INSERT INTO app_user (user_name, dob, height, weight, email) 
VALUES 
('Smith101', '1990-05-15', 165, 65, 'alice@example.com');

-- Inserting data into exercise table
INSERT INTO exercise (exercise_name, exercise_type, exercise_desc, calories_burnt, duration, difficulty, muscle_group) 
VALUES 
('Running', 'Cardio', 'Run straight homie', 500, '00:30:00', 'intermediate', 'quadriceps');

-- Inserting data into workout_plan table
INSERT INTO workout_plan (workout_name, workout_desc, user_id, exercise_1_id) 
VALUES 
('Morning Cardio', 'Light cardio workout', 1, 1);