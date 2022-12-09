import speech_recognition as sr
from openai import api_key
import openai

# Set the OpenAI API key
openai.api_key = "YOUR-API-KEY"

# Initialize the speech recognition module
r = sr.Recognizer()

# Create a function that inputs voice and transcribes the voice command
def transcribe_voice_command():
  with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    print("Recognizing...")
    try:
      command = r.recognize_google(audio)
      print("You said: " + command)
      return command
    except sr.UnknownValueError:
      print("Could not understand audio")
    except sr.RequestError as e:
      print("Error: {0}".format(e))

# Create a function that uses the ChatGPT3 model to generate a response to the voice command
def generate_response(command):
  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=command,
      max_tokens=1024,
      temperature=0.5,
  )
  return response["choices"][0]["text"]

# Create a function that outputs the response via sound
def output_response(response):
  print("The response is: " + response)
  import pyttsx3
  engine = pyttsx3.init()
  engine.say(response)
  engine.runAndWait()

# Use the functions to input voice, transcribe the command, generate a response, and output the response
command = transcribe_voice_command()
response = generate_response(command)
output_response(response)

