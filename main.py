from news import NewsAlert
import requests
import os
from dotenv import load_dotenv

load_dotenv()



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_KEY")

# Twilio + News API credentials
account_sid = os.getenv("TWILIO_SID")
auth_token  = os.getenv("TWILIO_TOKEN")
trial_num = os.getenv("TWILIO_FROM")
my_number = os.getenv("MY_NUMBER")
news_api_key = os.getenv("NEWS_API_KEY")

# Step 1 — Get stock data
parameters = {
    "function": "TIME_SERIES_DAILY",
    "apikey": ALPHAVANTAGE_API_KEY,
    "outputsize": "compact",
    "symbol": STOCK,
}
# --- Fetch latest stock data ---
response = requests.get(STOCK_ENDPOINT, params= parameters)
response.raise_for_status()
data = response.json()

# --- Extract latest and previous close prices ---
daily_data = data["Time Series (Daily)"]
dates = list(daily_data.keys())
latest_date = dates[0]
previous_date = dates[1]

latest_close = float(daily_data[latest_date]["4. close"])
previous_close = float(daily_data[previous_date]["4. close"])

# --- Calculate percentage change ---
difference = ((latest_close - previous_close) / previous_close) * 100

# --- If movement > 5%, get news and send SMS ---
if abs(difference) > 5:
    if difference < 0:
        trend_symbol = "📉"
        trend_text = f"{COMPANY_NAME} went down {difference:.2f}%"
    else:
        trend_symbol ="📈"
        trend_text = f"{COMPANY_NAME} went up {difference:.2f}%"

    # Create your NewsAlert object
    alert = NewsAlert(
        company_name=COMPANY_NAME,
        twilio_sid=account_sid,
        twilio_token=auth_token,
        twilio_from=trial_num,
        to_number=my_number,
        news_api_key=news_api_key,
    )
    # Fetch top headlines and send SMS
    alert.get_headlines()
    alert.sms_send(trend_symbol, trend_text)
else:
    print("Nothing important happened")