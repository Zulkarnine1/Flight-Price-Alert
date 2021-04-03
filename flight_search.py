from env import TEQ_ENDPOINT, TEQ_API_KEY
import requests as req
from flight_data import FlightData
import datetime


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass


    def process_IATA_code(self,input_data):
        for data in input_data:
            if data["iataCode"] == "":
                params = {
                    'term': data["city"],
                    'location_types': "city"
                }
                res = req.get(url=TEQ_ENDPOINT+"locations/query",params=params,headers = TEQ_API_KEY)
                res.raise_for_status()
                new_data = res.json()
                data["iataCode"] = new_data['locations'][0]['code']

        return input_data


    def search_flights(self,origin,to,from_time,to_time):
        # date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        # date_tomorrow = date_tomorrow.strftime('%d/%m/%Y')
        # date_6months = datetime.date.today() + datetime.timedelta(days=180)
        # date_6months = date_6months.strftime('%d/%m/%Y')

        params = {
            'fly_from':f"airport:{origin}",
            'fly_to':to,
            'date_from ': from_time.strftime("%d/%m/%Y"),
            'date_to ': to_time.strftime("%d/%m/%Y"),
            'nights_in_dst_from ': 7,
            'nights_in_dst_to ': 28,
            'flight_type ': 'round',
            'one_for_city ': 1,
            'curr':"USD",
            "selected_cabins":"M"

        }
        res = req.get(url=TEQ_ENDPOINT+"v2/search",params=params,headers=TEQ_API_KEY)
        res.raise_for_status()
        try:
            new_data = res.json()['data'][0]
        except:
            print("No flights available")
        else:
            flight_data = FlightData(
            price = new_data['price'],
            origin_city = new_data["cityFrom"],
            origin_airport = new_data["flyFrom"],
            destination_city = new_data["cityTo"],
            destination_airport = new_data["flyTo"],
            out_date = new_data["route"][0]["local_departure"].split("T")[0],
            return_date = new_data["route"][len(new_data["route"])-1]["local_departure"].split("T")[0],
            airports = [port["cityTo"] for port in new_data["route"]]
            )
            return flight_data


