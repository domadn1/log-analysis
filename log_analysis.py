#!/usr/bin/env python3

import psycopg2


DBNAME = 'news'

# Find most popular three articles of all time
query1 = """ SELECT a.title, count(l.path) as views
            FROM articles a, log l
            WHERE l.path like '/article/' || a.slug
                AND l.status like '%200%'
            GROUP BY a.title
            ORDER BY views desc
            LIMIT 3
    """

# Find the most popular article authors of all time
query2 = """ SELECT au.name, count(l.path) as views
            FROM log l, articles a
            LEFT JOIN authors au
                ON a.author = au.id
            WHERE l.path like '/article/' || a.slug
                AND l.status like '%200%'
            GROUP BY au.name
            ORDER BY views desc
    """

# Find days on which more than 1% of requests led to errors
query3 = """ SELECT a.fdate, (a.failed*100.0/b.total) as percent
            FROM (SELECT date(time) as fdate, count(*) as failed
                    FROM log
                    WHERE status like '%404%'
                    GROUP BY date(time)) as a
            JOIN (SELECT date(time), count(*) as total
                    FROM log
                    GROUP BY date(time)) as b
                ON a.fdate = b.date
                AND (a.failed*100.0/b.total) > 1.0
    """


def get_result(query):
    """Return results of the query"""
    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute(query)
    results = cur.fetchall()
    db.close()
    return results


if __name__ == '__main__':

    # Fetch popular 3 Articles
    print('\n\nArticle Title with number of views')
    for title, views in get_result(query1):
        print(title, ' - ', views)

    # Fetch Popular Authors
    print('\n\nAuthor name with number of views')
    for name, views in get_result(query2):
        print(name, ' - ', views)

    # Fetch days with more than 1% error
    print('\n\nAuthor name with number of views')
    for fdate, percent in get_result(query3):
        print(fdate.strftime('%d %b, %Y'), ' - ', round(percent, 2))

# Run as python log_analysis/log_analysis.py
