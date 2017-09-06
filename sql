-- comotion@172.25.73.200

-- just basic information about each user
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	card_id VARCHAR(50) NOT NULL UNIQUE,
	uw_id INT NOT NULL UNIQUE,
	uw_netid VARCHAR(50) NOT NULL UNIQUE,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL
);

-- keeps track of which card readers users cards will work on
CREATE TABLE memberships (
	id SERIAL PRIMARY KEY,
	uw_id INT NOT NULL REFERENCES users( uw_id ),
	type VARCHAR(50) NOT NULL REFERENCES equipment_groups(type),
	join_date INT NOT NULL,
	expiration_date INT NOT NULL
);

-- keeps track of added bans added for users and which card reader type it applies to
CREATE TABLE card_ban (
	id SERIAL PRIMARY KEY,
	uw_id INT NOT NULL REFERENCES users( uw_id ),
	type VARCHAR(50) NOT NULL REFERENCES equipment_groups(type),
	start_date INT NOT NULL,
	end_date INT NOT NULL
);

-- keeps track of card swipes when they happen and on which card reader
CREATE TABLE card_activity (
	id SERIAL PRIMARY KEY,
	uw_id INT NOT NULL,
	type VARCHAR(50) NOT NULL REFERENCES equipment_groups(type),
	date INT NOT NULL
);

-- keeps track of each card reader by id and its type	
CREATE TABLE card_readers (
	id SERIAL PRIMARY KEY,
	type VARCHAR(50) NOT NULL REFERENCES equipment_groups(type),
	description VARCHAR(200) NOT NULL,
	active BIT(1) NOT NULL DEFAULT '1'
);

-- keeps track of equipment groups for giving user permissions
CREATE TABLE equipment_groups (
	id SERIAL PRIMARY KEY,
	type VARCHAR(50) NOT NULL UNIQUE,
	description VARCHAR(200) NOT NULL,
	active BIT(1) NOT NULL DEFAULT '1'
);

INSERT INTO card_readers (type, description) VALUES
	('main_door', 'Main Door'),
	('laser_cutter', '60 W Yellow Laser Cutter'),
	('laser_cutter', '150 W Red Laser Cutter'),
	('3d_printer', '3D Printer'),
	('othermill', 'Othermill v2'),
	('othermill', 'Othermill v2'),
	('othermill', 'Othermill Pro'),
	('vinyl_cutter', 'Vinyl Cutter');

INSERT INTO equipment_groups (type, description) VALUES
	('main_door', 'Main Door'),
	('laser_cutter', 'Laser Cutter'),
	('3d_printer', '3D Printer'),
	('othermill', 'Othermill'),
	('vinyl_cutter', 'Vinyl Cutter');

-- create duplicates of all tables above for handling deleted entries

FUNCTION users:
	add
	remove
	edit
	search
	view

FUNCTION ban_user:
	
FUNCTION card_swipe:

FUNCTION equipment:
	add
	remove
	edit

CREATE TABLE 3d_printer (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	card_id VARCHAR(50) NOT NULL,
	mass INT NOT NULL,
	start_time INT NOT NULL,
	duration INT NOT NULL,
	printer_id INT NOT NULL,
	color VARCHAR(50) NOT NULL,
	failed BIT NOT NULL
);
