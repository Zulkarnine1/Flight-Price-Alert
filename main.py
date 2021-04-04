#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import datetime

ORIGIN_CITY_IATA = "DAC"

data_manager = DataManager()
flight_search = FlightSearch()
noti_manager = NotificationManager()


# will be called from datamanager but for shortage of requests using saved json
sheet_data = data_manager.get_sheety_data()
sheet_data = sheet_data['sheet1']
updated_data = flight_search.process_IATA_code(sheet_data)
if sheet_data != updated_data:
    data_manager.update_iatacode(sheet_data)


flight_list = []

for data in updated_data:
    date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    date_tomorrow = date_tomorrow
    date_6months = datetime.date.today() + datetime.timedelta(days=180)
    date_6months = date_6months
    flight_list.append(flight_search.search_flights(ORIGIN_CITY_IATA,data["iataCode"],date_tomorrow,date_6months))



prices = [past_data["lowestPrice"] for past_data in updated_data]
old_minimum = min(prices)

alert_list = []
for flight in flight_list:
    if flight != None:
        if  flight.price <= old_minimum:
            alert_list.append(flight)


noti_manager.send_mail(alert_list)
