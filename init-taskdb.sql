CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (now() at time zone 'utc'),
    deadline TIMESTAMP WITHOUT TIME ZONE,
    is_completed BOOLEAN DEFAULT FALSE
);
