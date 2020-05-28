import csv
import cx_Oracle


username = 'BATIAVGNEVE'
password = 'Ehuvum228'
dsn = 'localhost/xe'


connection = cx_Oracle.connect(username, password, dsn)

tables = ['Universities', 'Ranks', 'Countries', 'Universities_Ranks', 'Quality_of_faculty']


for table in tables:
    with open(table + '.csv', 'w', newline = '') as file:
        writer = csv.writer(file, delimiter=',')

        query = "SELECT * FROM " + table

        cursor = connection.cursor()
        cursor.execute(query)

        content = []
        column_names = []

        for name in cursor.description:
            column_names.append(name[0])

        writer.writerow(column_names)

        for row in cursor:
            content.append(list(row))

        for row in content:
            writer.writerow(row)

        cursor.close()
        

        
        connection.close()
