import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    

    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    url_short = "https://hidden-journey-62459.herokuapp.com"
    payload = {'input_text': get_fact()}
#    r = requests.post(url, payload)
#    soup = BeautifulSoup(r.content, 'html.parser')
#    pig = soup.h2.next_sibling.strip()
#    pig_latin = str(pig)
#
#    return ('The pig latin for "{}" is: {}').format(payload['input_text'], pig_latin)
    
    r = requests.post(url, payload, allow_redirects=False)
    r1 = r.content.decode()
    redirect = r1.replace('href="', 'href="' + url_short)
    redirect = redirect.replace('">', '">' + url_short)
    #print(redirect)
    
    return redirect

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

