#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///pbl.db')
app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        # This line performs query and returns json result
        query = conn.execute("select * from employees")
        # Fetches first column that is Employee ID
        return {'employees': [i for i in query.cursor.fetchall()]}

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        ReportsTo = request.json['ReportsTo']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Fax = request.json['Fax']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}')".format(LastName, FirstName, Title,
                                             ReportsTo, BirthDate, HireDate, Address,
                                             City, State, Country, PostalCode, Phone, Fax,
                                             Email))
        return {'status': 'success'}

    def put(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        ReportsTo = request.json['ReportsTo']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Fax = request.json['Fax']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}')".format(LastName, FirstName, Title,
                                             ReportsTo, BirthDate, HireDate, Address,
                                             City, State, Country, PostalCode, Phone, Fax,
                                             Email))
        return {'status': 'success'}

    def delete(self):
        conn = db_connect.connect()
        print(request.json)
        query = conn.execute(
            """delete from employees where LastName='%s'""" % request.json['LastName'])
        return{'status': 'success'}


class Cricket(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        # This line performs query and returns json result
        query = conn.execute("select * from cricket")
        # Fetches first column that is Team
        return {'cricket': [i for i in query.cursor.fetchall()]}

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        Team = request.json['Team']
        Owner = request.json['Owner']
        Captain = request.json['Captain']
        TeamSize = request.json['TeamSize']
        NoOfForeignPlayers = request.json['NoOfForeignPlayers']
        HighestRunsBY = request.json['HighestRunsBY']
        HighestRuns = request.json['HighestRuns']
        HighestWktBy = request.json['HighestWktBy']
        HighestWkt = request.json['HighestWkt']
        BestBattingAvgBy = request.json['BestBattingAvgBy']
        BestBattingAvg = request.json['BestBattingAvg']
        BestBowlingAvgBy = request.json['BestBowlingAvgBy']
        BestBowlingAvg = request.json['BestBowlingAvg']
        AvgScoreBattingFirst = request.json['AvgScoreBattingFirst']
        AvgScoreBattingSecond = request.json['AvgScoreBattingSecond']
        MatchesPlayed = request.json['MatchesPlayed']
        won = request.json['won']
        lost = request.json['lost']
        points = request.json['points']
        NetRR = request.json['NetRR']
        HighestTotal = request.json['HighestTotal']
        query = conn.execute("insert into cricket values('{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}')".format(Team, Owner, Captain,
                                                                                              TeamSize, NoOfForeignPlayers, HighestRunsBY, HighestRuns,
                                                                                              HighestWktBy, HighestWkt, BestBattingAvgBy, BestBattingAvg, BestBowlingAvgBy, BestBowlingAvg,
                                                                                              AvgScoreBattingFirst, AvgScoreBattingSecond, MatchesPlayed, won, lost, points, NetRR, HighestTotal))
        return {'status': 'success'}

    def put(self):
        conn = db_connect.connect()
        print(request.json)
        Team = request.json['Team']
        Owner = request.json['Owner']
        Captain = request.json['Captain']
        TeamSize = request.json['TeamSize']
        NoOfForeignPlayers = request.json['NoOfForeignPlayers']
        HighestRunsBy = request.json['HighestRunsBy']
        HighestRuns = request.json['HighestRuns']
        HighestWktBy = request.json['HighestWktBy']
        HighestWkt = request.json['HighestWkt']
        BestBattingAvgBy = request.json['BestBattingAvgBy']
        BestBattingAvg = request.json['BestBattingAvg']
        BestBowlingAvgBy = request.json['BestBowlingAvgBy']
        BestBowlingAvg = request.json['BestBowlingAvg']
        AvgScoreBattingFirst = request.json['AvgScoreBattingFirst']
        AvgScoreBattingSecond = request.json['AvgScoreBattingSecond']
        MatchesPlayed = request.json['MatchesPlayed']
        won = request.json['won']
        lost = request.json['lost']
        points = request.json['points']
        NetRR = request.json['NetRR']
        HighestTotal = request.json['HighestTotal']
        query = conn.execute("insert into cricket values('{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}')".format(Team, Owner, Captain,
                                                                                              TeamSize, NoOfForeignPlayers, HighestRunsBy, HighestRuns,
                                                                                              HighestWktBy, HighestWkt, BestBattingAvgBy, BestBattingAvg, BestBowlingAvgBy, BestBowlingAvg,
                                                                                              AvgScoreBattingFirst, AvgScoreBattingSecond, MatchesPlayed, won, lost, points, NetRR, HighestTotal))
        return {'status': 'success'}

    def delete(self):
        conn = db_connect.connect()
        print(request.json)
        query = conn.execute(
            """delete from cricket where Team='%s'""" % request.json['Team'])
        return{'status': 'success'}


class Student(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        # This line performs query and returns json result
        query = conn.execute("select * from student")
        # Fetches first column that is Student ID
        return {'Student': [i for i in query.cursor.fetchall()]}

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        Name = request.json['Name']
        DOB = request.json['DOB']
        Phone = request.json['Phone']
        Email = request.json['Email']
        Branch = request.json['Branch']
        Semester = request.json['Semester']
        CGPA = request.json['CGPA']
        Quota = request.json['Quota']
        YearOfAdmission = request.json['YearOfAdmission']

        query = conn.execute("insert into student values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}')".format(Name, DOB,
                                                                    Phone, Email, Branch, Semester, CGPA, Quota, YearOfAdmission))
        return {'status': 'success'}

    def put(self):
        conn = db_connect.connect()
        print(request.json)
        Name = request.json['Name']
        DOB = request.json['DOB']
        Phone = request.json['Phone']
        Email = request.json['Email']
        Branch = request.json['Branch']
        Semester = request.json['Semester']
        CGPA = request.json['CGPA']
        Quota = request.json['Quota']
        YearOfAdmission = request.json['YearOfAdmission']

        query = conn.execute("insert into student values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}')".format(Name, DOB,
                                                                    Phone, Email, Branch, Semester, CGPA, Quota, YearOfAdmission))
        return {'status': 'success'}

    def delete(self):
        conn = db_connect.connect()
        print(request.json)
        query = conn.execute(
            """delete from student where Name='%s'""" % request.json['Name'])
        return{'status': 'success'}


api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Cricket, '/cricket')
api.add_resource(Student, '/student')

if __name__ == '__main__':
    app.run()
