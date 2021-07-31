from django.test import TestCase
import requests, random, json, time

# Create your tests here.
class TriggerTest(TestCase):
    def testrequest(self):
        username = "username"   # Enter your username
        password = "password"   # and password
        accesstokenurl = "http://127.0.0.1:8000/api/token/" # url to get simplejwt access toke 
        body = '{{ "username": "{0}", "password": "{1}" }}'.format(username, password)
        header = {"Content-Type": "application/json"}
        tokendata = requests.post(url=accesstokenurl, data=body, headers=header)    # API with POST request to get simplejwt access token
        if tokendata.status_code == 200:
            token ="Bearer " + json.loads(tokendata.content)["access"]
            currentpriceurl = "http://127.0.0.1:8000/alerts/currentprice"   # url to post the current price of BTC to trigger the alert
            header = {"Authorization": token, "Content-Type": "application/json"}
            while(True):
                number = random.randint(67889,67892) # here we're generating random BTC current Price to trigger alert
                body = '{{ "currentPrice": {0} }}'.format(number)
                jsonresponse = requests.post(url=currentpriceurl, data=body, headers=header)    # API with POST request to send currentPrice
                content = json.loads(jsonresponse.content)
                if (jsonresponse.status_code == 201) and content:
                    print("The current price of BTC is {0}".format(str(number)))
                    for item in json.loads(jsonresponse.content):
                        print("Alert id {0} with targetPrice {1} has been triggered...".format(str(item["id"]), str(item["targetPrice"])))
                    # break
                elif jsonresponse.status_code != 201:
                    print("Something goes wrong...")
                time.sleep(10)  # Sleep timing of 10 seconds
        else:
            print("Invalid username or password.")