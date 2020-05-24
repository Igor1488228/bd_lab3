CREATE VIEW Countries_Universities AS
    SELECT
        u.university_name,
        u.dynamic_year,
        c.country_name
    FROM
        countries c
        LEFT JOIN universities u ON c.country_name = u.country_name;
