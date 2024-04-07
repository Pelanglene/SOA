CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    description TEXT,
    deadline TIMESTAMP,
    is_completed BOOLEAN DEFAULT FALSE,
    author_id INT
);
