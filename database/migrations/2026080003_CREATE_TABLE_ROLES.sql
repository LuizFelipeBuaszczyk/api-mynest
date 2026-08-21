CREATE TABLE roles (
    id SMALLINT NOT NULL,
    codename VARCHAR(50) NOT NULL,
    description VARCHAR(255)
);

CREATE SEQUENCE seq_roles_id
    START WITH 1
    INCREMENT BY 1
    NO CYCLE;

ALTER TABLE roles
    ALTER COLUMN id SET DEFAULT nextval('seq_roles_id');

ALTER TABLE roles
    ADD CONSTRAINT PK_ROLES PRIMARY KEY (id);
