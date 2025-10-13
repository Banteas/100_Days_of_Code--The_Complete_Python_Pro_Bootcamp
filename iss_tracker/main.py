import requests
from datetime import datetime, timezone
import smtplib
import time


# If the ISS is close to my current position,
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds if the ISS overhead

def is_overhead():
    return (my_lat - 5) <= iss_latitude <= (my_lat + 5) and (my_lng - 5) <= iss_longitude <= (my_lng + 5)
def is_dark():
    return hour_now >= sunset or hour_now <= sunrise


response = requests.get(url= "http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_longitude = float(data['iss_position']['longitude'])
iss_latitude = float(data['iss_position']['latitude'])

# Your position is within +5 or -5 degrees of the ISS position. Create a boolean function
my_lat = 58.485923
my_lng = 15.431997


parameters = {
    "lat" : my_lat ,
    "lng" : my_lng ,
    "formatted" : 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
data = response.json()
response.raise_for_status()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc)
hour_now = time_now.hour
sender_email = "your_email@gmail.com" # your personal email
senders_email_password = "your_app_password" # your personal app password

while True:
    if is_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(sender_email, senders_email_password)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=sender_email,
                                msg="Subject: Look up!\n\nThe ISS is above you right now")
    time.sleep(60)