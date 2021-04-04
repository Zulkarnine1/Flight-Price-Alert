from env import SHEETY_ENDPOINT,SHEETY_ENDPOINT2
import requests as req



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_sheety_data(self):
        res = req.get(url=SHEETY_ENDPOINT)
        res.raise_for_status()
        data = res.json()
        return data

    def update_iatacode(self,input_data):
        for data in input_data:
            body = {"sheet1":{
                'city': data['city'],
                'iataCode': data['iataCode'],
                'lowestPrice': data['lowestPrice']
            }}

            res = req.put(url=SHEETY_ENDPOINT+f"/{data['id']}",json=body)
            res.raise_for_status()
            print(res.text)

    def get_users(self):
        res = req.get(url=SHEETY_ENDPOINT2)
        res.raise_for_status()
        data = res.json()
        return data



