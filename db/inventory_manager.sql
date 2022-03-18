DROP TABLE IF EXISTS cameras;
DROP TABLE IF EXISTS makes;

CREATE TABLE makes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cameras (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    make_id INT REFERENCES makes(id),
    type VARCHAR(255),
    description TEXT,
    stock INT,
    buy_price INT,
    sell_price INT
);