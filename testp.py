import psycopg2

try:
    conn = psycopg2.connect("dbname='moderat' user='moderat' host='localhost' password='moderat'")
except:
    print 'err'