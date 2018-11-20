#!/usr/bin/env python3

import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
print('What are the most popular three articles of all time?')
c.execute("""select articles.title,count(*)
from articles, log
where log.path like concat('/article/', articles.slug)
and log.status = '200 OK'
group by articles.title order by count desc limit 3""")
db.commit()
printQ = c.fetchall()
for x in range(0, 3):
    print('"', printQ[x][0], '"', ' -- ', printQ[x][1], 'views \n')

print("\nWho are the most popular article authors of all time?")

c.execute("""select authors.name, count(*)
from authors,articles,log
where log.path like concat('/article/', articles.slug)
and log.status = '200 OK' and authors.id = articles.author
group by authors.name order by count desc limit 4""")
db.commit()
printQ = c.fetchall()
for x in range(0, 4):
    print(printQ[x][0], ' -- ', printQ[x][1], 'views \n')

print("\nOn which days did more than 1% of requests lead to errors?")

c.execute("""
select to_char(l.time, 'Month DD,YYYY'),
ROUND(((r1.sta) *100/(r2.nu)), 2) as per
from log l,
(select to_char(log.time, 'Month DD,YYYY') as r1da,
cast(count(status) as DECIMAL) as sta
from log where status!='200 OK'
group by to_char(log.time, 'Month DD,YYYY')) as r1,
(select to_char(log.time, 'Month DD,YYYY') as r2da,
cast(count(*) as DECIMAL) as nu
from log  group by to_char(log.time, 'Month DD,YYYY')) as r2
where (r1.sta*100/r2.nu) > 1 and r1.r1da = to_char(l.time, 'Month DD,YYYY')
and r2.r2da= to_char(l.time, 'Month DD,YYYY')
GROUP by to_char(l.time, 'Month DD,YYYY') , per
order by per desc;""")

db.commit()
printQ = c.fetchall()
le = len(printQ)
for x in range(0, le):
    print(printQ[x][0], ' -- ', printQ[x][1], '% \n')


db.close()
