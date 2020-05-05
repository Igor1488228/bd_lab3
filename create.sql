CREATE TABLE Universityes_rank (
     university_name VARCHAR(30) NOT NULL
    ,dynamic_year NUMBER(4,0) NOT NULL
    ,university_position NUMBER(4,0) NOT NULL
    ,country_name VARCHAR(20) NOT NULL
    ,CONSTRAINT PK_Universityes_rank PRIMARY KEY (university_name, dynamic_year, university_position, country_name)
    ,CONSTRAINT FK1_Universityes_rank FOREIGN KEY (university_position) REFERENCES Rank(university_position)
    ,CONSTRAINT FK2_Universityes_rank FOREIGN KEY (university_name, dynamic_year, country_name) REFERENCES Rank(university_name, dynamic_year, country_name)
)
