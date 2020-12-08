from restclient import RestClient
import sys


def getInput(string, l, ex=False):
    while True:
        val = int(input(string + "\n"))
        if(ex == True and val == 5):
            sys.exit()
        if val not in l:
            print('Invalid Input')
        else:
            break
    return val


a = RestClient("http://127.0.0.1:5000")
tables = {1: 'employees', 2: 'student', 3: 'cricket'}
employeeDict = {"LastName": "",
                "FirstName": "",
                "Title": "",
                "ReportsTo": "",
                "BirthDate": "",
                "HireDate": "",
                "Address": "",
                "City": "",
                "State": "",
                "Country": "",
                "PostalCode": "",
                "Phone": "",
                "Fax": "",
                "Email": ""}
studentDict = {"Name": "",
               "DOB": "",
               "Phone": "",
               "Email": "",
               "Branch": "",
               "Semester": "",
               "CGPA": "",
               "Quota": "",
               "YearOfAdmission": ""}
cricketDict = {"Team": "",
               "Owner": "",
               "Captain": "",
               "TeamSize": "",
               "NoOfForeignPlayers": "",
               "HighestRunsBy": "",
               "HighestRuns": "",
               "HighestWktBy": "",
               "HighestWkt": "",
               "BestBattingAvgBy": "",
               "BestBattingAvg": "",
               "BestBowlingAvgBy": "",
               "BestBowlingAvg": "",
               "AvgScoreBattingFirst": "",
               "AvgScoreBattingSecond": "",
               "MatchesPlayed": "",
               "won": "",
               "lost": "",
               "points": "",
               "NetRR": "",
               "HighestTotal": ""}
employeeKey = "LastName"
studentKey = "Name"
cricketKey = "Team"

attributes = {'employees': employeeDict,
              'student': studentDict, 'cricket': cricketDict}
keys = {'employees': employeeKey, 'student': studentKey, 'cricket': cricketKey}


def get(table):
    response = a.get("/"+table)
    print(response.json())
    return


def post(table, att):
    print("Enter The Values to be posted into "+table)
    for i in att.keys():
        print("\nEnter The Value for "+i, end=" ")
        att[i] = input()
    response = a.post(table, att)
    print(response)
    return


def delete(table, key):
    print("Enter the record with the key " + key + " to be deleted")
    val = input()
    response = a.delete(table, val)
    print(response)
    return


val = getInput('Enter:\n1. Perform Get Request\n2. Perform Post Request\n3. Perform Put Request\n4. Perform Delete Request\n5. Exit', [
               1, 2, 3, 4, 5], ex=True)
table = tables[getInput(
    'Select The Table to perform the request on:\n1. Employee\n2. Student\n3. Cricket', [1, 2, 3])]

while True:
    if val == 1:
        print("Performing GET Request on " + table + "...")
        get(table)
    elif val == 2:
        print("Performing POST Request on " + table + "...")
        post(table, attributes[table])
    elif val == 3:
        print("Performing PUT Request on " + table + "...")
        post(table, attributes[table])
    elif val == 4:
        print("Performing DELETE Request on " + table + "...")
        delete(table, keys[table])
    else:
        sys.exit()
    val = getInput(
        'Enter:\n1. Perform Get Request\n2. Perform Post Request\n3. Perform Put Request\n4. Perform Delete Request\n5. Exit', [1, 2, 3, 4, 5])
    if val == 5:
        continue
    table = tables[getInput(
        'Select The Table to perform the request on:\n1. Employee\n2. Student\n3. Cricket', [1, 2, 3])]
