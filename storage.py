#!/usr/bin/python
import datetime
import psycopg2
import json


class DatetimeEventStore :

    # Initializing
    def __init__(self):
        #first setting your database with db_config.json
        try:
            #get setting :
            with open('db_config.json', 'r') as file:
                db_config = json.load(file)

            # print (db_config)
            #connect database
            self.conn = psycopg2.connect(
                host=db_config['host'],
                database=db_config['database'],
                user=db_config['user'],
                password=db_config['password']
            )

            self.cursor = self.conn.cursor()

        except(Exception, psycopg2.Error) as error :
            if(self.conn):
                print("Failed to insert record into mobile table", error)


    # Deleting (Calling destructor)
    def __del__(self):
        # use del for close database
        if(self.conn):
            self.cursor.close()
            self.conn.close()
            print("PostgreSQL connection is closed")


    def store_event(self, *args, **kwargs):

        date = kwargs['at']
        data = kwargs['data']

        postgres_insert_query = """
            INSERT INTO events(time, event)
            VALUES (%s, %s)
        """

        record_to_insert = ( date.isoformat(), data)

        self.cursor.execute(postgres_insert_query, record_to_insert)

        self.conn.commit()


    def get_events(self, *args, **kwargs) :

        start = kwargs['start']
        end = kwargs['end']

        # print(start, end)

        postgres_insert_query = """
            SELECT * FROM events
            WHERE time > %s AND time < %s;
        """

        record_to_insert = ( start.isoformat(), end.isoformat())

        self.cursor.execute(postgres_insert_query, record_to_insert)
        self.conn.commit()

        enventsListe = self.cursor.fetchall()
        return enventsListe
