import datetime as dt
from quotes import Quotes
from mailer import Email
import random

QUOTES_FILE = "list_of_quotes.txt"
TO_ADDRESS = ""

email = Email()
quotes = Quotes(QUOTES_FILE)

now = dt.datetime.now()
day_of_week = now.weekday()

subject = "Quote of the Day"
body = random.choice(quotes.list)

if day_of_week == 0:
    email.send_msg(TO_ADDRESS, subject, body)
