import psycopg2
import csv
import os

result = 'result.csv'
QUERY = '''
    SELECT 
        zno_year,
        REGNAME,
        min(physBall100), 
        min(physBall12)
    FROM zno 
    WHERE physTestStatus = 'Зараховано' 
    GROUP BY zno_year, REGNAME
'''
COLUMNS = ['Year', 'Region', 'ZNO Grade', 'DPA Grade']


def select(conn):
    cur = conn.cursor()

    cur.execute(QUERY)
    res = cur.fetchall()

    with open(os.path.join('ZNOData', result), 'w', newline='') as csvf:
        csv_writer = csv.writer(csvf, dialect='excel')
        csv_writer.writerow(COLUMNS)
        csv_writer.writerows(res)

    cur.close()

conn = psycopg2.connect("dbname=postgres user=postgres password=password")
select(conn)
conn.close()
