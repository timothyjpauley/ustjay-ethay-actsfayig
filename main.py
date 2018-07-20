import os

import requests
from flask import Flask, send_file, Response, redirect, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def piglatin():

    url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    fact = get_fact()
    payload = {"input_text": fact}
    new_url = requests.post(url, allow_redirects=False, data=payload).headers.get('Location')
    return new_url

@app.route('/', methods=['GET'])
def home():
    url = piglatin()
    print(url)
    return render_template('piglatin.jinja2', url = url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
