CREATE DATABASE IF NOT EXISTS mydatabase;

USE mydatabase;

CREATE TABLE
    IF NOT EXISTS employees (
        id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        salary FLOAT NOT NULL
    );