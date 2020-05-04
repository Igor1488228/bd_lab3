CREATE OR REPLACE VIEW University_stat as
    select university.university_name
    , years.position
    , years.year
    , country.country
    from university
    join years on years.university_name = university.university_name
    join country on country.university_name = university.university_name;
