# This code is a Python script that uses the psycopg2 library to connect to a PostgreSQL database 
# and insert random values for various sensor readings into different tables within the database. 
# The purpose of this code is likely to generate test data for the database.


import psycopg2
import random
from datetime import datetime
import time as t

hostname = 'postgres'
database = 'fmdashboard'
username = 'postgres'
pwd = '1234'
port_id = 5432


try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd)

    cur = conn.cursor()
    # changed table names added prefix app_
    # double quoted column names to ensure 
    # that PostgreSQL interprets it as a column identifier rather than a reserved keyword
    cur.execute("DELETE FROM app_step_count;")
    for i in range(10):

        time = datetime.now()
        value = round(random.uniform(20, 85), 2)

        insert_step_count = ''' INSERT INTO app_step_count(time, "Count") VALUES (%s, %s)'''
        cur.execute(insert_step_count,(time, value))


    cur.execute("DELETE FROM app_calories_burnt;")
    for i in range(10):
        
        time = datetime.now()
        value = round(random.uniform(6.5, 7),2) 

        insert_calories_burnt = ''' INSERT INTO app_calories_burnt(time, "Joule") VALUES (%s, %s)'''
        cur.execute(insert_calories_burnt,(time, value))


    cur.execute("DELETE FROM app_distance_covered;")
    for i in range(10):

        time = datetime.now()
        value = round(random.uniform(0,100),2) 

        insert_distance_covered = ''' INSERT INTO app_distance_covered(time, "KM") VALUES (%s, %s)'''
        cur.execute(insert_distance_covered,(time, value))


    cur.execute("DELETE FROM app_heart_rate;")
    for i in range(10):

        time = datetime.now()
        value = round(random.uniform(0, 5),2) 

        insert_heart_rate = ''' INSERT INTO app_heart_rate(time, "BPM") VALUES (%s, %s)'''
        cur.execute(insert_heart_rate,(time, value))

    conn.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()