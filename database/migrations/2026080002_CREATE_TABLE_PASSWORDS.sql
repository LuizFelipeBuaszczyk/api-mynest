
CREATE TABLE passwords (
    id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    password VARCHAR(255) NOT NULL,
    fk_owner INTEGER NOT NULL
);

CREATE SEQUENCE seq_passwords_id
    START WITH 1
    INCREMENT BY 1
    NO CYCLE;

ALTER TABLE passwords
    ALTER COLUMN id SET DEFAULT nextval('seq_passwords_id');

ALTER TABLE passwords 
    ADD CONSTRAINT PK_PASSWORDS PRIMARY KEY (id);

ALTER TABLE passwords
    ADD CONSTRAINT FK_PASSWORD_OWNER FOREIGN KEY (fk_owner) REFERENCES users(id);


