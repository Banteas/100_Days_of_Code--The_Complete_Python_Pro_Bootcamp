
import requests
from datetime import timedelta, date
from twilio.rest import Client





class NewsAlert:
    def __init__(self, company_name, twilio_sid, twilio_token, twilio_from, to_number, news_api_key):
        self.company = company_name
        self.client = Client(twilio_sid, twilio_token)
        self.from_number = twilio_from
        self.to_number = to_number
        self.news_api = "https://newsapi.org/v2/everything"
        self.news_api_key = news_api_key
        self.headlines = []


    def get_headlines(self):
        today = date.today()
        yesterday = today - timedelta(days=1)

        parameters = {
            "apiKey": self.news_api_key,
            "q": self.company,
            "from": yesterday.isoformat(),
            "sortBy": "publishedAt",
            "pageSize": 3,
            "language": "en",
        }


        response = requests.get(self.news_api,params= parameters)
        response.raise_for_status()
        data = response.json()

        articles = data.get('articles',[])
        self.headlines = [article['title'] for article in articles]
        return self.headlines

    def sms_send(self, trend_symbol, trend_text):
        if not self.headlines:
            print("⚠️ No headlines found — SMS not sent.")
            return

        try:
            for headline in self.headlines:
                # Build a short message for each headline
                message_body = f"{trend_symbol} {trend_text}\n{headline}"

                message = self.client.messages.create(
                    body=message_body,
                    from_=self.from_number,
                    to=self.to_number,
                )
                print("✅ SMS sent:", message.sid)

        except Exception as e:
            print("❌ Error sending SMS:", e)