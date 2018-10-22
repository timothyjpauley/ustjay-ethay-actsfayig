import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

BASE_URL = 'https://hidden-journey-62459.herokuapp.com'
URL = BASE_URL + '/piglatinize/'


def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText().strip()


def translate_facts(fact):
    data = {'input_text': str(fact)}
    response = requests.post(URL, data=data)
    response_url = a=requests.post(URL, data=data, allow_redirects=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup_url = BeautifulSoup(response_url.text, 'html.parser')
    return soup.find('body').text.strip().splitlines()[-1].strip(), soup_url.find('a').text


@app.route('/')
def home():
    facts = get_fact()
    pig_latin, pig_latin_link = translate_facts(facts)
    return f"""
    <html>
      <head>
          <title>Facts Converter</title>
      </head>
      <body>
          <h1>Fact: {facts} </h1>
          <p>Pig Latin: {pig_latin}</p>
          <a href="{str(BASE_URL + pig_latin_link)}">Click me!</a>
      </body>
    </html>
    
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='127.0.0.1', port=port)

