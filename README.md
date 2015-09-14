# Siri on Windows
Example code for using Wolfram Alpha API to get Siri/Cortana like experience on windows machine as well as Raspberry Pi.
Here, we are using Windows' in-built speech recognition input for speech recognition. Once speech is available, we are fetching user query result from Wolfram Alpha API.

You can explore Wolfram Alpha API here. http://products.wolframalpha.com/api/explorer.html

For converting the result response to Speech, we are using Speech module for Python. 

# Wolfram Alpha Usage on Raspberry Pi
On Raspberry PI, we are using Speech Reognition from Universal Translator (http://makezine.com/projects/make-42/universal-translator/)
Once, speech is converted in text, we can use that text for fetching our query from Wolfram Alpha. On Raspberry Pi, we are usinh eSpeak module for converting text to speech.
