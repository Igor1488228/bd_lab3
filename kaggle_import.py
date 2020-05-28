import csv
import cx_Oracle

username = 'BATIAVGNEVE'
password = 'Ehuvum228'
dsn = 'localhost/xe'

connection = cx_Oracle.connect(username, password, dsn)

with open('C:/Users/admin/Desktop/university.csv') as file:
    reader = csv.reader(file)

    next(reader)
    country_unique = []
    rank_unique = []
    universities_unique = []
    quality_of_faculty_unique = []
    universities_rank_unique = []
    error_counter = 0

    cursor = connection.cursor()
    try:
        for row in reader:

            country = row[4].split(',')[0].strip()
            university = row[1].strip()
            ranks = row[6].split(',')
            record = '28.05.2020'

            try:
                dynamic = int(row[3])
            except:
                continue


            try:
                quality_of_faculty = int(row[2])
            except:
                quality_of_faculty = None


            try:
                national = int(row[5])
            except:
                national = None


            if (not country) or (not university) or (not dynamic):
                continue



            if country.lower() not in country_unique:
                cursor.execute("INSERT INTO Countries (country_name) VALUES (:country)", country=country)
                country_unique.append(country.lower())


            if (university.lower(), dynamic, country.lower()) not in universities_unique:
                cursor.execute("INSERT INTO Universities (university_name, dynamic_year, country_name, national_rank) VALUES " +
                               "(:university, :dynamic, :country, :national)", (university, dynamic, country, national))
                universities_unique.append((university.lower(), dynamic, country.lower()))


            for rank in ranks:
                if rank.lower().strip() not in rank_unique:
                    cursor.execute("INSERT INTO Ranks (university_rank) VALUES (:rank)", rank=rank.strip())
                    rank_unique.append(rank.strip().lower())

                if (university.lower(), dynamic, country.lower(),rank.lower().strip()) not in universities_ranks_unique:
                    cursor.execute("INSERT INTO Universities_Ranks (university_name, dynamic_year, country_name, university_rank) VALUES " +
                                   "(:university, :dynamic, :country, :rank)", (university, dynamic, country, rank.strip()))
                    universities_ranks_unique.append((university.lower(), dynamic, country.lower(), rank.lower().strip()))



            if (university.lower(), dynamic, country.lower(), record) not in quality_of_faculty_unique:
                cursor.execute("INSERT INTO Quality_of_faculty (university_name, dynamic_year, country_name, record_date, quality_of_faculty) VALUES " +
                    "(:university, :dynamic, :country, TO_DATE(:record, 'DD-MM-YYYY'), :quality_of_faculty)", (university, dynamic, country, record, quality_of_faculty))
                quality_of_faculty_unique.append((university.lower(), dynamic, country.lower(), record))

            error_counter +=1

    except:
        print(f"The error occurred on the {error_counter} line", error_counter)

    cursor.close()
    connection.commit()
    connection.close()
