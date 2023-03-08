import requests
import json


class FirstCallreqresclass():

    def __init__(self, Url):
        self.Url = Url

    def GetRequestsVerifyStatusCode(self):
        response = requests.get(self.Url)
        if response.status_code == 200:
            print('Success!')
        elif response.status_code == 404:
            print('Not Found.')
            print(response)
            
    def GetRequestsVerifyUsers(self):
        response = requests.get(self.Url)
        content = response.content
        print(content)

    def GetRequestsVerifyPage(self):
        response = requests.get(self.Url)
        content = response.content
        page = json.loads(content)
        print(page["page"])

    def GetRequestsVerifyEmail(self):
        response = requests.get(self.Url)
        content = response.content
        email = json.loads(content)
        print(email["email"])



        

