import mysql.connector


class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='root',
                database='atomm'
            )
            self.mycursor = self.conn.cursor()
            print("Connection established")
        except:
            print("Connection error")

    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
        SELECT distinct(Source) FROM atomm.flights
        UNION
        SELECT distinct(Destination) FROM atomm.flights
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self, source, destination):

        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price FROM atomm.flights
        where Source = '{}' AND Destination = '{}'
        """.format(source, destination))

        data = self.mycursor.fetchall()
        return data

    def fetch_Airline_frequency(self):

        airline = []
        frequency = []
        self.mycursor.execute("""
                SELECT Airline,count(*) FROM atomm.flights
                group by Airline
                """)
        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):

        city = []
        frequency = []
        self.mycursor.execute("""
        select Source,count(*) from (SELECT Source FROM atomm.flights
		UNION ALL
		SELECT Destination FROM atomm.flights) t1
        GROUP BY Source
        ORDER BY COUNT(*) DESC
        """)
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):

        dates = []
        frequency = []
        self.mycursor.execute("""
        SELECT Date_of_Journey,count(*) FROM atomm.flights
        group by Date_of_Journey
        """)
        data = self.mycursor.fetchall()

        for item in data:
            dates.append(item[0])
            frequency.append(item[1])

        return dates, frequency

