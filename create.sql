CREATE TABLE University(
    university_name VARCHAR(256) NOT NULL
    , country VARCHAR(256) NOT NULL
    , position VARCHAR(256) NOT NULL
    , year NUMBER(4,0) NOT NULL
    , CONSTRAINT university_pk PRIMARY KEY (university_name)
);
CREATE TABLE Years
(
    university_name VARCHAR(256) NOT NULL
    ,year NUMBER(4,0) NOT NULL
    , position VARCHAR(100) NOT NULL
    , CONSTRAINT year_university_fk PRIMARY KEY (university_name)
    ,CONSTRAINT year_pk FOREIGN KEY (university_name) REFERENCES university(university_name)
);
CREATE TABLE Country
(
    university_name VARCHAR(256) NOT NULL,
    country VARCHAR(256) NOT NULL,
    CONSTRAINT country_pk PRIMARY KEY (country),
    CONSTRAINT country_pk FOREIGN KEY (university_name) REFERENCES Years(university_name)
);
