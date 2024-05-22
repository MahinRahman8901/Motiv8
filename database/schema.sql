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
    exercise_name VARCHAR(100) NOT NULL,
    exercise_type VARCHAR(20) NOT NULL,
    calories_burnt INT NOT NULL,
    duration TIME NOT NULL
);

CREATE TABLE workout_plan(
    workout_plan_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    workout_name VARCHAR(100) NOT NULL,
    workout_desc TEXT NOT NULL,
    user_id BIGINT,
        FOREIGN KEY (user_id) REFERENCES app_user(user_id),
    exercise_id INT NOT NULL,
        FOREIGN KEY (exercise_id) REFERENCES exercise(exercise_id)
);

-- Inserting data into user table
INSERT INTO app_user (user_name, dob, height, weight, email) 
VALUES 
('Alice Smith', '1990-05-15', 165, 65, 'alice@example.com'),
('Bob Johnson', '1985-08-22', 180, 85, 'bob@example.com');

-- Inserting data into exercise table
INSERT INTO exercise (exercise_name, exercise_type, calories_burnt, duration) 
VALUES 
('Running', 'Cardio', 500, '00:30:00'),
('Bench Press', 'Strength', 300, '00:20:00');

-- Inserting data into workout_plan table
INSERT INTO workout_plan (workout_name, workout_desc, user_id, exercise_id) 
VALUES 
('Morning Cardio', '30 minutes of running at moderate pace.', 1, 1),
('Strength Session', 'Bench press for chest strength.', 2, 2);