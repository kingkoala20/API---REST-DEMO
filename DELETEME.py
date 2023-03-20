import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_simple_message():
    domain = os.getenv("MAILGUN_DOMAIN")
    return requests.post(
		f"https://api.mailgun.net/v3/{domain}/messages",
		auth=("api", os.getenv("MAILGUN_API_KEY")),
		data={"from": f"Excited User <mailgun@{domain}>",
			"to": ["bajprodo@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
    
send_simple_message()