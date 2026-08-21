CREATE TABLE user_roles (
    id INTEGER NOT NULL,
    fk_user SMALLINT NOT NULL,
    fk_role SMALLINT NOT NULL
);

CREATE SEQUENCE seq_user_roles_id
    START WITH 1
    INCREMENT BY 1
    NO CYCLE;

ALTER TABLE user_roles
    ALTER COLUMN id SET DEFAULT nextval('seq_user_roles_id');

ALTER TABLE user_roles
    ADD CONSTRAINT PK_USER_ROLES PRIMARY KEY (id);

ALTER TABLE user_roles
    ADD CONSTRAINT FK_USER_USER_ROLES FOREIGN KEY (fk_user) REFERENCES users (id);

ALTER TABLE user_roles
    ADD CONSTRAINT FK_ROLE_USER_ROLES FOREIGN KEY (fk_role) REFERENCES roles (id);

ALTER TABLE user_roles
    ADD CONSTRAINT UQ_USER_ROLES UNIQUE (fk_user, fk_role);
