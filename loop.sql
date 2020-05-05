DECLARE
    items_count int := 7;
BEGIN 
    for i in 1..items_count LOOP
    
        INSERT INTO university ( university_name, country, position, year)
            values ('university' || i, 'United States', '1+i' || i, 2012+i);
    end loop;
END;