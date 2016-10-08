# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC25117bbce1af54ed8f5243b1bdc6e236"
auth_token  = "c533d997c85e971648b8ab6656d942d3"
client = TwilioRestClient(account_sid, auth_token)

number = client.phone_numbers.purchase(voice_url="http://demo.twilio.com/docs/voice.xml", messaging_url="http://7dd9130f.ngrok.io/"
    ,phone_number="+15005550006")
print(number.phone_number)
