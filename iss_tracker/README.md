# 🌌 ISS Notifier

A Python script that alerts you by email when the **International Space Station (ISS)** is overhead at your location during nighttime.  

---

## 🚀 Features

- Fetches the current **ISS position** using the [Open Notify API](http://open-notify.org/).  
- Determines if it is **dark** at your location using the [Sunrise-Sunset API](https://sunrise-sunset.org/api).  
- Sends an **email notification** when the ISS is overhead at night.  
- Runs continuously, checking every **60 seconds**.  

---

## 🛠️ Requirements

- Python 3.9+  
- Modules:
  - `requests`
  - `smtplib`
  - `datetime`
  - `time`  

Install the required module if you don’t have it:

```bash
pip install requests
```
## ⚡ How to Use

1. Open the script and set your latitude and longitude:
```python
my_lat = 58.485923
my_lng = 15.431997
```
2. Set your email credentials (use an app password if using Gmail):
````python
sender_email = "your_email@gmail.com"
senders_email_password = "your_app_password"
````
3. Run the script:
```` bash
python main.py
````
The script will check the ISS position every 60 seconds and email you when it’s overhead at night.

## ⚠️ Notes

- Gmail users need to create an App Password if 2FA is enabled.

- The script fetches sunrise and sunset times in UTC; your local timezone is handled automatically.

- The “night” condition wraps around midnight, so notifications work correctly even across days.

## 📬 Example Output

When the ISS is overhead at night, you will receive an email like:

**Subject**: Look up!

**Body**: The ISS is above you right now