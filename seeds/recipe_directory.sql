DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_iq_seq;
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  title text,
  average_cooking_time int,
  rating int
);