import cx_Oracle
import re
import chart_studio.plotly as py
import plotly.graph_objs as go
import chart_studio.dashboard_objs as dashboard
import chart_studio


username = 'hr'
password = '11'
database = 'localhost/ORCL'


def fileId_url(url):
    raw_filed = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return raw_filed.replace("/", ":")


connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

query1 = """select positions, count(university_name) as count_pos
from University_stat
GROUP BY position
order by count_pos DESC
"""

cursor.execute(query1)

dat = {}
for row in cursor:
    if row[0] in dat.keys():
        dat[row[0]] += int(row[1])
    else:
        dat[row[0]] = int(row[1])

data = [go.Bar(

    x=list(dat.keys()),
    y=list(dat.values())

)]

layout = go.Layout(
    xaxis=dict(
        titlefont=dict(
            family="monospace",
            size=18
        )
    ),
    yaxis=dict(
        autorange=True,
        rangemode="nonnegative",
        titlefont=dict(
            family="monospace",
            size=18
        )
    )
)

fig = go.Figure(data=data, layout=layout)

position_url = py.plot(fig, filename="first_url")

query2 = """select  round((count(university_name)/7) * 100, 2) as rate
    ,NVL(сountry, 0) as countries
from University_stat
GROUP by NVL(country, 0)
order by countries DESC
"""
cursor.execute(query2)

сountryes = dict()

for row in cursor:
    сountryes[row[0]] = row[1]

pie = go.Pie(labels=list(countries.keys()), values=list(countries.values()))

tems_University_stat_url = py.plot([pie], filename='University_stat')

query3 = """select count(university_name) as count_university
            , year as all_years

            from University_stat

GROUP by years
ORDER by count_university"""

cursor.execute(query3)

years_stat = dict()

for raw in cursor:
    years_stat[raw[0]] = raw[1]

years_stat_dynamic = go.Scatter(
    x=list(years_stat.keys()),
    y=list(years_stat.values())
)
data = [years_stat_dynamic]
years_stat_dunamic_url = py.plot(data, filename='years_stat_dynamic')

my_dboard = dashboard.Dashboard()

x = fileId_url(position_url)
y = fileId_url(tems_University_stat_url)
z = fileId_url(years_stat_dunamic_url)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': x,
    'title': 'The number university on position'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': y,
    'title': 'University statistic in countryes'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': z,
    'title': 'University statistic for year'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'Dashboard for DB')

cursor.close()
connection.close()