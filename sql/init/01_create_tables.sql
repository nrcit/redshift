-- https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_NEW.html

CREATE TABLE IF NOT EXISTS users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
