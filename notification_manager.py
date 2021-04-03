import smtplib
from env import my_email,password,address

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_mail(self,flight):


        letter = f""" New Cheap Flight Alert !!!
        from:{flight.origin_city},
        to:{flight.destination_city},
        price:{flight.price} USD,
        departure:{flight.out_date },
        airports:{",".join(flight.airports)}
"""

        From = my_email
        Pass = password
        To = address
        # Your stmp service provider eg. "smtp.gmail.com" for gmail
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=From, password=Pass)
            connection.sendmail(to_addrs=To, from_addr=From, msg=f"Subject: New Cheap Flight Alert!!!\n\n{letter}")
        print("mail sent")