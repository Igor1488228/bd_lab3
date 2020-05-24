CREATE TABLE universities (
    university_name     VARCHAR2(50) NOT NULL,
    dynamic_year   NUMBER(4) NOT NULL,
    national_rank  NUMBER(3) NOT NULL,
    country_name  VARCHAR2(50) NOT NULL
);

ALTER TABLE universities
    ADD CONSTRAINT universities_pk PRIMARY KEY ( university_name,
                                          dynamic_year,
                                          country_name );

CREATE TABLE universities_ranks (
    university_rank    NUMBER(3,0) NOT NULL,
    university_name     VARCHAR2(50) NOT NULL,
    dynamic_year   NUMBER(4) NOT NULL,
    country_name  VARCHAR2(50) NOT NULL
);

ALTER TABLE universities_ranks
    ADD CONSTRAINT universities_ranks_pk PRIMARY KEY ( university_rank,
                                                 university_name,
                                                 dynamic_year,
                                                 country_name );

CREATE TABLE countries (
    country_name VARCHAR2(50) NOT NULL
);

ALTER TABLE countries ADD CONSTRAINT countries_pk PRIMARY KEY ( country_name );

CREATE TABLE quality_of_faculty (
    publications_number NUMBER NOT NULL,
    quality_of_faculty          INTEGER,
    university_name     VARCHAR2(50) NOT NULL,
    dynamic_year   NUMBER(4) NOT NULL,
    country_name  VARCHAR2(50) NOT NULL
);

ALTER TABLE quality_of_faculty
    ADD CONSTRAINT quality_of_faculty_pk PRIMARY KEY (publications_number,
                                         university_name,
                                         dynamic_year,
                                         country_name );

CREATE TABLE ranks (
    university_rank NUMBER(3,0) NOT NULL
);

ALTER TABLE ranks ADD CONSTRAINT ranks_pk PRIMARY KEY ( university_rank );

ALTER TABLE universities
    ADD CONSTRAINT universities_countries_fk FOREIGN KEY ( country_name )
        REFERENCES countries ( country_name );

ALTER TABLE universities_ranks
    ADD CONSTRAINT universities_ranks_fk1 FOREIGN KEY ( university_name,
                                                  dynamic_year,
                                                  country_name )
        REFERENCES universities ( university_name,
                                  dynamic_year,
                                  country_name );

ALTER TABLE universities_ranks
    ADD CONSTRAINT universities_ranks_fk2 FOREIGN KEY ( university_rank )
        REFERENCES ranks ( university_rank );

ALTER TABLE quality_of_faculty
    ADD CONSTRAINT quality_of_faculty_universities_fk FOREIGN KEY ( university_name,
                                               dynamic_year,
                                               country_name )
        REFERENCES universities ( university_name,
                            dynamic_year,
                           country_name );

