import smtplib
from env import my_email,password,address
from data_manager import DataManager

data_manager = DataManager()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_mail(self,unsorted_flights):
        flights = sorted(unsorted_flights, key=lambda k: k.price)
        letters = ["New Cheap Flight Alert !!!\n\n\n"]
        for flight in flights:

            letter = f""" 
            from:{flight.origin_city},
            to:{flight.destination_city},
            price:{flight.price} USD,
            departure:{flight.out_date },
            route:{flight.via_city}
            
    """
            letters.append(letter)

        users = data_manager.get_users()["sheet2"]
        for user in users:
            From = my_email
            Pass = password
            To = user["email"]
            # Your stmp service provider eg. "smtp.gmail.com" for gmail
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=From, password=Pass)
                connection.sendmail(to_addrs=To, from_addr=From, msg=f"Subject: New Cheap Flight Alert!!!\n\n{ ''.join(letters)}")
            print("mail sent")