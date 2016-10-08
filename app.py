from flask import Flask, request, redirect
import twilio.twiml
import datetime
import unicodedata

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


@app.route("/", methods=['GET', 'POST'])
def main_response():
        """Respond and greet the caller by name."""
        from_number = request.values.get('From', None)
        text = request.values.get('Body','Nothing recieved')
        num_media = request.values.get('NumMedia',0)
        if text:
            text = text.lower()
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
            else :
                message = "Not something I could think of!"
            resp = twilio.twiml.Response()  
            resp.message(message)
            print(message) 
            return str(resp)

if __name__ == "__main__":
        app.run(debug=True)
