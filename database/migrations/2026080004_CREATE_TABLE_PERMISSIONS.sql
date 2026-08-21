CREATE TABLE permissions (
    id SMALLINT NOT NULL,
    codename VARCHAR(50) NOT NULL,
    description VARCHAR(255)
);

CREATE SEQUENCE seq_permissions_id
    START WITH 1
    INCREMENT BY 1
    NO CYCLE;

ALTER TABLE permissions
    ALTER COLUMN id SET DEFAULT nextval('seq_permissions_id');

ALTER TABLE permissions
    ADD CONSTRAINT PK_PERMISSIONS PRIMARY KEY (id);
