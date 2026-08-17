CREATE TABLE role_permissions (
    id INTEGER NOT NULL,
    fk_role SMALLINT NOT NULL,
    fk_permission SMALLINT NOT NULL
);

CREATE SEQUENCE seq_role_permissions_id
    START WITH 1
    INCREMENT BY 1
    NO CYCLE;

ALTER TABLE role_permissions 
    ALTER COLUMN id SET DEFAULT nextval('seq_role_permissions_id');

ALTER TABLE role_permissions
    ADD CONSTRAINT PK_ROLE_PERMISSIONS PRIMARY KEY (id);

ALTER TABLE role_permissions
    ADD CONSTRAINT FK_ROLE_ROLE_PERMISSIONS FOREIGN KEY (fk_role) REFERENCES roles (id);

ALTER TABLE role_permissions
    ADD CONSTRAINT FK_PERMISSION_ROLE_PERMISSIONS FOREIGN KEY (fk_permission) REFERENCES permissions (id);
