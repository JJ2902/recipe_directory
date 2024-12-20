-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    average_cooking_time INTEGER,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Risotto', 45, 4);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Miso Aubergine', 20, 3);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('BBQ Pork', 35, 5);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Tuna Mayo Rice', 15, 3);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Beef Stew', 67, 5);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Omelette', 10, 2);