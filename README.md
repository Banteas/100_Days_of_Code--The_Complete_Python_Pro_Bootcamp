# Stock News Alert

This project monitors Tesla (TSLA) stock price changes and sends SMS alerts with the latest news if the stock moves more than 5% in a day.

It uses:
- [Alpha Vantage API](https://www.alphavantage.co/) for stock data
- [NewsAPI](https://newsapi.org/) for news headlines
- [Twilio](https://www.twilio.com/) for sending SMS

---

## Features

- Checks Tesla stock daily
- Calculates the percentage change from yesterday to the day before
- Fetches the top 3 news headlines if the stock moves more than 5%
- Sends each headline as a separate SMS with an up or down trend emoji

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Banteas/100_Days_of_Code--The_Complete_Python_Pro_Bootcamp.git
cd stock-news-hard
````
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Create a .env file in the project root and add your API keys:
````
ALPHAVANTAGE_KEY=your_alpha_vantage_key
NEWS_API_KEY=your_news_api_key
TWILIO_SID=your_twilio_sid
TWILIO_TOKEN=your_twilio_auth_token
TWILIO_FROM=your_twilio_phone_number
MY_NUMBER=your_personal_phone_number
````
## Usage

1. Open main.py.

2. Run the script:
````
python main.py
````
3. If the stock price moves more than 5%, you will receive an SMS with the trend and the top 3 news headlines.

## Files
- main.py — Main script to check stock price and send news alerts.
- news.py — Module handling news fetching and SMS sending.
- .env — Environment variables storing API keys (not included in GitHub for security).
## Notes
- Make sure your .env file is kept secret and is listed in .gitignore.
- This project uses the free tier of Twilio and NewsAPI, so some limitations may apply.