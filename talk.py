
import os
import openai
from flask import Flask, render_template, request
app = Flask(__name__)
openai.api_key = 'YOUR-API-KEY'

prompt = 'The following is a conversation with Leonardo. Leonardo is a bot acting like the painter and inventor Leonardo Da Vinci.\nYou: Can you paint?\nLeonardo: Yes I can actually paint very well, I painted the famous Mona Lisa\nYou: When were you born?\nLeonardo: I was born on 15 April 1452\nYou: When did you die?\nLeonardo: I died on the 2nd of May 1519, I was 67 years old\n'


def get_response(q):
    global prompt
    prompt=prompt+'You: '+q+'\n'
    response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["\n", " You:", " Leonardo:"],
    )
    return response['choices'][0]['text']
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    global prompt
    userText = request.args.get('msg')
    response = get_response(userText)
    prompt = prompt + response
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
