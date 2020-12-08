import requests


class RestClient:

    def __init__(self, url, headers=None, auth=None):
        self.url = url
        self.session = requests.session()
        if headers:
            self.session.headers = headers
        if auth:
            self.session.auth = auth

    def get(self, path="/", headers=None, params=None, debug=False):
        if debug:
            print("GET %s/%s\n" % (self.url, path))

        r = self.session.get(self.url+"/"+path, headers=headers, params=params)
        if debug:
            print("GET %s\n" % (r.url))
        return r

    def post(self, table, att):
        # if debug:
        #     print("PUT %s/%s\n" % (self.url, path))
        # print(data)
        # r = self.session.put(
        #     self.url+"/"+path, headers=headers, params=params, data=data)
        # if debug:
        #     print("PUT %s\n" % (r.url))
        # return r
        url = "http://127.0.0.1:5000/"+table
        if(table == "employees"):
            payload = "{\n      \t\"LastName\": \"%s\",\n                          \"FirstName\": \"%s\",\n                          \"Title\": \"%s\",\n                          \"ReportsTo\": \"%s\",\n                          \"BirthDate\": \"%s\",\n                          \"HireDate\": \"%s\",\n                          \"Address\": \"%s\",\n                          \"City\": \"%s\",\n                          \"State\": \"%s\",\n                          \"Country\": \"%s\",\n                          \"PostalCode\": \"%s\",\n                          \"Phone\": \"%s\",\n                          \"Fax\": \"%s\",\n                          \"Email\": \"%s\"\n\t\t\t\t\n}" % (
                att["LastName"], att["FirstName"], att["Title"], att["ReportsTo"], att["BirthDate"], att["HireDate"], att["Address"], att["City"], att["State"], att["Country"], att["PostalCode"], att["Phone"], att["Fax"], att["Email"])
        elif(table == "student"):
            payload = "{\n        \"Name\":\"%s\",\n        \"DOB\": \"%s\",\n        \"Phone\": \"%s\",\n        \"Email\": \"%s\",\n        \"Branch\": \"%s\",\n        \"Semester\": %s,\n        \"CGPA\":%s,\n        \"Quota\": \"%s\",\n        \"YearOfAdmission\": %s\n\n\n\t\t\t\t}" % (
                att["Name"], att["DOB"], att["Phone"], att["Email"], att["Branch"], att["Semester"], att["CGPA"], att["Quota"], att["YearOfAdmission"])
        elif(table == "cricket"):
            payload = "{\n      \t\n\t  \"Team\": \"%s\",\n        \"Owner\": \"%s\",\n        \"Captain\": \"%s\",\n        \"TeamSize\": \"%s\",\n        \"NoOfForeignPlayers\": \"%s\",\n        \"HighestRunsBY\": \"%s\", \n        \"HighestRuns\":\"%s\",\n        \"HighestWktBy\":\"%s\",\n        \"HighestWkt\" :\"%s\",\n        \"BestBattingAvgBy\" :\"%s\",\n        \"BestBattingAvg\":\"%s\",\n        \"BestBowlingAvgBy\" :\"%s\",\n        \"BestBowlingAvg\":\"%s\",\n        \"AvgScoreBattingFirst\":\"%s\",\n        \"AvgScoreBattingSecond\":\"%s\",\n        \"MatchesPlayed\":\"%s\",\n        \"won\":\"%s\",\n        \"lost\" :\"%s\",\n        \"points\" :\"%s\",\n        \"NetRR\" :\"%s\",\n        \"HighestTotal\":\"%s\"\n\n\n\t\t\t\t\n}" % (
                att["Team"], att["Owner"], att["Captain"], att["TeamSize"], att["NoOfForeignPlayers"], att["HighestRunsBy"], att["HighestRuns"], att["HighestWktBy"], att["HighestWkt"], att["BestBattingAvgBy"], att["BestBattingAvg"], att["BestBowlingAvgBy"], att["BestBowlingAvg"], att["AvgScoreBattingFirst"], att["AvgScoreBattingSecond"], att["MatchesPlayed"], att["won"], att["lost"], att["points"], att["NetRR"], att["HighestTotal"])
        else:
            return("Error")
        headers = {'Content-Type': 'application/json'}
        print(payload)
        print(url)
        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

    def delete(self, table, key):

        # if debug:
        #     print("DELETE %s/%s\n" % (self.url, path))
        # r = self.session.delete(
        #     self.url+"/"+path, headers=headers, params=params)
        # if debug:
        #     print("DELETE %s\n" % (r.url))
        # return r
        url = "http://127.0.0.1:5000/"+table
        print(table)
        if(table == "employees"):
            payload = "{\n      \t\"LastName\": \"%s\"\n\t\t\t\t\n}" % key
        elif(table == "student"):
            payload = "{\n      \t\"Name\": \"%s\"\n\t\t\t\t\n}" % key
        elif(table == "cricket"):
            payload = "{\n      \t\"Team\": \"%s\"\n\t\t\t\t\n}" % key
        else:
            return ("error")
        headers = {'Content-Type': 'application/json'}

        response = requests.request(
            "DELETE", url, data=payload, headers=headers)

        print(response.text)

    # get function that handles REST pagination

    def get_stream(self, path, headers=None, params=None, offset=0, end=None, limit=50, debug=False):
        position = offset

        if params == None:
            params = {}

        while True:
            offset = position
            params['limit'] = limit
            params['offset'] = offset
            results = self.get(path, params=params,
                               headers=headers, debug=debug)
            obj = results.json()
            if not "data" in obj:
                break

            if len(obj['data']) == 0:
                break

            for element in obj['data']:
                yield element
                position += 1

                if end != None:
                    if position >= end:
                        break
