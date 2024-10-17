DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;


CREATE SEQUENCE IF NOT EXISTS recipes_iq_seq;
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  title text,
  average_cooking_time int,
  rating int
);

INSERT INTO recipes (title, average_cooking_time, rating) VALUES ('Spagetti Bolognese', 90, 4);
INSERT INTO recipes (title, average_cooking_time, rating) VALUES ('Packet Ramen', 5, 3);
INSERT INTO recipes (title, average_cooking_time, rating) VALUES ('Smoked Rat with Rosemary Potatoes', 60, 1);
INSERT INTO recipes (title, average_cooking_time, rating) VALUES ('Chicken Kebab', 60, 4);
INSERT INTO recipes (title, average_cooking_time, rating) VALUES ('Chilli con Carne', 120, 5);
