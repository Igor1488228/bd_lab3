  
BEGIN
    FOR i IN 1..20 LOOP
        INSERT INTO countries (country_name) VALUES ('country' || i);
    
        INSERT INTO universities (
            university_name,
            dynamic_year,
            national_rank,
            country_name
        ) VALUES (
            'Univercity' || i,
            1930 - 3 * i,
            1930 + 4 * i,
            'country' || i
        );

    END LOOP;

END;
