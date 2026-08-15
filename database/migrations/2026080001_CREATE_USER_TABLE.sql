CREATE TABLE users (
    id SMALLINT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    is_superuser BOOLEAN DEFAULT FALSE
);

CREATE SEQUENCE seq_user_id
    START WITH 1
    INCREMENT BY 1
    NO CYCLE;

ALTER TABLE users 
    ALTER COLUMN id SET DEFAULT nextval('seq_user_id');  

ALTER TABLE users
    ADD CONSTRAINT PK_USERS PRIMARY KEY (id);
