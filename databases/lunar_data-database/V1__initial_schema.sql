CREATE TABLE samples (
	id UUID NOT NULL, 
	original_sample_id VARCHAR, 
	generic_id VARCHAR, 
	bag_number VARCHAR, 
	original_weight FLOAT, 
	sample_type VARCHAR, 
	sample_subtype VARCHAR, 
	pristinity FLOAT, 
	pristinity_date VARCHAR, 
	has_thin_section BOOLEAN, 
	has_display BOOLEAN, 
	generic_description VARCHAR, 
	mission_id UUID, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	UNIQUE (original_sample_id), 
	FOREIGN KEY(mission_id) REFERENCES missions (id)
)

CREATE TABLE missions (
	id UUID NOT NULL, 
	name VARCHAR, 
	PRIMARY KEY (id), 
	UNIQUE (id), 
	UNIQUE (name)
)