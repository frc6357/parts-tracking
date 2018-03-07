-- Create schemas

-- Create tables
CREATE TABLE IF NOT EXISTS Parts
(
    uid uuid DEFAULT uuid_generate_v4 () NOT NULL UNIQUE,
    part_number VARCHAR(0),
    description VARCHAR(0),
    unit uuid,
    PRIMARY KEY(uid)
);

CREATE TABLE IF NOT EXISTS Locations
(
    uid uuid DEFAULT uuid_generate_v4 () NOT NULL UNIQUE,
    name VARCHAR(0),
    description VARCHAR(0),
    PRIMARY KEY(uid)
);

CREATE TABLE IF NOT EXISTS Inventory
(
    uid uuid DEFAULT uuid_generate_v4 () NOT NULL UNIQUE,
    part_uid uuid NOT NULL,
    loc_uid uuid,
    qty DECIMAL(0, 0),
    PRIMARY KEY(uid)
);

CREATE TABLE IF NOT EXISTS Units
(
    uid uuid DEFAULT uuid_generate_v4 () NOT NULL UNIQUE,
    name VARCHAR(0),
    countable BOOLEAN DEFAULT false,
    PRIMARY KEY(uid)
);

CREATE TABLE IF NOT EXISTS Transactions
(
    uid uuid DEFAULT uuid_generate_v4 () NOT NULL UNIQUE,
    notes VARCHAR(0),
    user uuid,
    PRIMARY KEY(uid)
);

CREATE TABLE IF NOT EXISTS Actions
(
    uid uuid DEFAULT uuid_generate_v4 () NOT NULL UNIQUE,
    transaction uuid,
    target uuid,
    change DECIMAL(0, 0),
    PRIMARY KEY(uid)
);

CREATE TABLE IF NOT EXISTS users
(
    uid uuid DEFAULT uuid_generate_v4 () NOT NULL UNIQUE,
    user_id VARCHAR(0),
    password_hash BIGINT,
    PRIMARY KEY(uid)
);


-- Create FKs
ALTER TABLE Inventory
    ADD    FOREIGN KEY (part_uid)
    REFERENCES Parts(uid)
    MATCH SIMPLE
    ON UPDATE CASCADE
;
    
ALTER TABLE Inventory
    ADD    FOREIGN KEY (loc_uid)
    REFERENCES Locations(uid)
    MATCH SIMPLE
    ON UPDATE CASCADE
;
    
ALTER TABLE Parts
    ADD    FOREIGN KEY (unit)
    REFERENCES Units(uid)
    MATCH SIMPLE
    ON UPDATE CASCADE
;
    
ALTER TABLE Actions
    ADD    FOREIGN KEY (target)
    REFERENCES Inventory(uid)
    MATCH SIMPLE
    ON UPDATE CASCADE
;
    
ALTER TABLE Actions
    ADD    FOREIGN KEY (transaction)
    REFERENCES Transactions(uid)
    MATCH SIMPLE
    ON UPDATE CASCADE
;
    
ALTER TABLE Transactions
    ADD    FOREIGN KEY (user)
    REFERENCES users(uid)
    MATCH SIMPLE
    ON UPDATE CASCADE
;
    

-- Create Indexes

