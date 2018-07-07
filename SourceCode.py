#!/usr/bin/env python3
import psycopg2
conn = psycopg2.connect("dbname=news")
cur = conn.cursor()
query1 = """
select title, count(log.path) as views from articles join
log on concat('/article/', articles.slug) = log.path
where log.status like '200%'
group by log.path, articles.title order by views desc limit 3;
"""
query2 = """
select authors.name, count(log.path) as views from articles join
log on concat('/article/', articles.slug) = log.path join authors
on author=authors.id
where log.status like '200%'
group by name order by views desc limit 10;
"""
query3 = """
select * from ( select success.day,
round(cast(100*(failed.cc) as numeric) / cast(success.cc as numeric), 2)
as ErrorRate
from (select date(time) as day, count(log.status)
as cc from log group by day) as success
join
(select date(time) as day, count(log.status)
as cc from log where status not like '200%' group by day) as failed
on success.day = failed.day)
as Foo where ErrorRate > 1.0;
 """


def MostPopularArticles():
    cur.execute(query1)
    print("The most popular three articles of all time\n")
    ll = list(cur)
    counter = 0
    for row in ll:
        counter += 1
        print("Article "+str(counter)+" "+row[0]+" Views "+str(row[1]))


def MostPopulActors():
    cur.execute(query2)
    print("\nThe most popular article authors of all time")
    ll = list(cur)
    counter = 0
    for row in ll:
        counter += 1
        print("Artist "+str(counter)+" "+row[0]+" Views "+str(row[1]))


def MostErrorDay():
    cur.execute(query3)
    print("\nDays did more than 1% of requests lead to errors !")
    ll = list(cur)
    counter = 0
    for row in ll:
        counter += 1
        print("Day "+str(counter)+" "+str(row[0])+" Error Rate \
 "+str(row[1])+"%")


MostPopularArticles()
MostPopulActors()
MostErrorDay()
