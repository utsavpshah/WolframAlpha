import wolframalpha
import sys
import os.path
import subprocess
import speech
import time

# Get a free API key here http://products.wolframalpha.com/api/
# This is a fake ID. 
app_id = "QWERTY-Q1W2E3R4T5"
client = wolframalpha.Client(app_id)
#query = " ".join(sys.argv[1:])

response = speech.input("Say something, please.")
#speech.say("You said " + response)

#Callback function for processing the speech
#If speech is goodbye stop listening
def callback(phrase, listener):
    if phrase == "goodbye":
        listener.stoplistening()
    #speech.say(phrase)
	
print (len(response.split()))
#Check if length of spoken word is greater than 3
#If length is greater than 3, then only call Wolfram Alpha API
if len(response.split()) > 3:
	res = client.query(response)
if len(res.pods) > 0:
	texts = ""
	pod = res.pods[1]
	if pod.text:
		texts = pod.text
	else:
		texts = "I have no answer for that"
# to skip ascii character in case of error
	texts = texts.encode('ascii', 'ignore')
	print (texts)
else:
	texts = "Sorry, I am not sure."
print (texts)

#Speaking out loud response coming from Wolfram Alpha API
speech.say(texts)

listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)
