import wolframalpha
import sys
import os.path
import subprocess


# Get a free API key here http://products.wolframalpha.com/api/
# This is a fake ID.
app_id = "QWERTY-Q1W2E3R4T5"
client = wolframalpha.Client(app_id)
query = " ".join(sys.argv[1:])
#query = input("> ")

res = client.query(query)

#Execute UNIX command for speaking the texts returning from Wolfram Alpha API
def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

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

# speak aloud
c = 'espeak -ven+m5 -k5 -s160 -a200 --punct="<characters>" "%s" 2>>/dev/null' % texts
execute_unix(c)
