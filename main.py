import chart_studio
import cx_Oracle
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard
import re

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')


chart_studio.tools.set_credentials_file(username='igor_bitsan', api_key='bhnfddDmgSjhdre0')

username = 'BATIAVGNEVE'
password = 'Ehuvum228'
dsn = 'localhost/xe'

connection = cx_Oracle.connect(username, password, dsn)
cursor = connection.cursor()



first_query = """SELECT
    TRIM(c.country_name) country,
    COUNT(u.university_name) universities
FROM
    Countries   c
    LEFT JOIN Universities u ON c.country_name = u.country_name
GROUP BY
    TRIM(c.country_name)
ORDER BY
   universities DESC;"""

cursor.execute(first_query)
country_universities = dict()

for raw in cursor:
    country_universities[raw[0]] = raw[1]


data = [go.Bar(
            x=list(country_universities.keys()),
            y=list(country_universities.values())
)]

layout = go.Layout(
    title='',
    xaxis=dict(
        title='Countries',
        titlefont=dict(
            family='',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Universities',
        rangemode='',
        autorange=True,
        titlefont=dict(
            family='',
            size=18,
            color='#7f7f7f'
        )
    )
)

fig = go.Figure(data=data, layout=layout)

number_of_universities_in_each_country_url = py.plot(fig, filename='number_of_universities_in_each_country_2')






 second_query = """SELECT
    TRIM(r.university_rank) ranks,
    COUNT(u.university_name) universities
FROM
    ranks r
    LEFT JOIN Universities_Ranks ur ON r.university_rank = ur.university_rank
    LEFT JOIN Universities u         ON u.university_name = ur.university_name
                             AND u.dynamic_year = ur.dynamic_year
                             AND u.country_name = ur.country_name
GROUP BY
    TRIM(r.university_rank)
ORDER BY
    universities DESC;"""

country_ranks = dict()

cursor.execute(second_query)
for raw in cursor:
    country_genres[raw[0]] = raw[1]

pie = go.Pie(labels=list(country_ranks.keys()), values=list(country_ranks.values()))
percent_of_ranks_url = py.plot([pie], filename='ranks_2')







third_query = """SELECT 
    TRIM(c.country_name) country, 
    NVL(SUM(u.quality_of_faculty), 0) quality_of_faculty
FROM 
    Countries c
    LEFT JOIN Universities u ON c.country_name = u.country_name
GROUP BY 
    TRIM(c.country_name)
ORDER BY 
       quality_of_faculty DESC;"""


country_quality_of_faculty = dict()
cursor.execute(third_query)

for raw in cursor:
    country_quality_of_faculty[raw[0]] = raw[1]



country_quality_of_faculty_dynamic = go.Scatter(
    x=list(country_quality_of_faculty.keys()),
    y=list(country_quality_of_faculty.values()),
    mode='lines+markers'
)
data = [country_quality_of_faculty_dynamic]
country_quality_of_faculty_dynamic_url=py.plot(data, filename='country_quality_of_faculty_dynamic_2')







"""--------CREATE DASHBOARD------------------ """




my_dboard = dashboard.Dashboard()

number_of_universities_in_each_country_id = fileId_from_url(number_of_universities_in_each_country_url)
ranks_id = fileId_from_url(ranks_url)
country_ranks_dynamic_id = fileId_from_url(country_ranks_dynamic_url)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': number_of_niversities_in_each_country_id,
    'title': 'Number of niversities in each country 2'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': ranks_id,
    'title': 'ranks_id 2'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': country_ranks_dynamic_id,
    'title': 'ranks by country 2',
}



my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'right', 2)

py.dashboard_ops.upload(my_dboard, '3 Laboratory Dashboard')


cursor.close()
connection.close()
