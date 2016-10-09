from flask import Flask, request, redirect
import twilio.twiml
import datetime
import unicodedata
from wolfram import auto_answer

from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC194f638dd0a28e46ea3767b5a5c0767c"
AUTH_TOKEN = "c29f42bf54189047eea14a58c93bec93" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

app = Flask(__name__)

# Try adding your own number to this list!
responses = {
        "hello": "Hey there! What's up",
        "help": "I'm your offline personal assistant, just send your query to me, I'll try to resolve.",
        "hi": "Hey there! What's up"
}

callers = {
        "+19784068914": "Gautam",
        "+19282650595": "Mayank"
}

greeting = ['hi','hey','hello','ola']
map_keys = ['map','directions','route','neighbour']
relative_duration = ['after','before','every']

def match_intent(li,sentence):
    for word in sentence.split(' '):
        if word in li:
            return True
    return False

def send_mms(media_link="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg",to_number="+19784068914"):
    res = client.messages.create(
    to=to_number, 
    from_="+", 
    body="This message has image attached to it.", 
    media_url=media_link, 
    )
    print(res.status,res.price, res.num_media)

@app.route("/mms", methods=['GET'])
def check_mms():
    send_mms()
    return 'Success!'

@app.route("/", methods=['GET', 'POST'])
def main_response():
        """Respond and greet the caller by name."""
        from_number = request.values.get('From', None)
        text = request.values.get('Body','')
        num_media = request.values.get('NumMedia',0)
        if text:
            text = text.lower()
            if isinstance(text, unicode):
                text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
            print("Message recieved --> " + text)
            sender_name = ''
            message = 'Sorry couldn\'t understand you'
            if from_number in callers:
                sender_name = callers[from_number]
            if 'remind' in text:
                units =  str(filter(str.isdigit, text))
                i = -1 
                if(units):
                    word_index = text.split(' ').index(units)
                    i = text.index(units)
                    print("units -->"+units)
                if match_intent(relative_duration,text):
                    time = datetime.datetime.now()
                    repeat = False
                    if('after' in text[:i] and 'min' in text[i:]):
                        time += datetime.timedelta(minutes=units)
                    elif('after' in text[:i] and 'sec' in text[i:]):
                        time += datetime.timedelta(seconds=units)
                    elif('after' in text[:i] and 'day' in text[i:]):
                        time += datetime.timedelta(days=units)
                    elif('after' in text[:i] and 'year' in text[i:]):
                        time += datetime.timedelta(years=units)
                    elif('after' in text[:i] and 'month' in text[i:]):
                        time += datetime.timedelta(months=units)
                        print("Case encounte")
                    elif('after' in text[:i] and 'week' in text[i:]):
                        time += datetime.timedelta(weeks=units)
                    elif('before' in text[:i] and 'min' in text[i:]):
                        time -= datetime.timedelta(minutes=units)
                    elif('before' in text[:i] and 'sec' in text[i:]):
                        time -= datetime.timedelta(seconds=units)
                    elif('before' in text[:i] and 'day' in text[i:]):
                        time -= datetime.timedelta(days=units)
                    elif('before' in text[:i] and 'year' in text[i:]):
                        time -= datetime.timedelta(years=units)
                    elif('before' in text[:i] and 'month' in text[i:]):
                        time -= datetime.timedelta(months=units)
                    elif('before' in text[:i] and 'week' in text[i:]):
                        time -= datetime.timedelta(weeks=units)
                    elif('every') in text[:i]:
                        repeat = True
                    message = "All right you'll be notified."
                    print(time)
            elif match_intent(map_keys,text):
                message = "Here you go, the map is right here"
            elif match_intent(greeting,text):
                print("greeting")
                message = "Hi "+sender_name+", I'm your personal assistant. Feel free to ask me anything!"
            else:
                auto_reply = auto_answer(text)
                if auto_reply:
                    message = auto_reply
            resp = twilio.twiml.Response()  
            resp.message(message)
            print(message) 
            return str(resp)
            print("Response -->",resp)
        return "No text detected"

if __name__ == "__main__":
        app.run(debug=True)
