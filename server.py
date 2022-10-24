from asyncio.windows_events import NULL
from flask import Flask,Blueprint,render_template

from htmlparser import api_request
from scrap import scrap_falabella
from config import URLS


app = Flask(__name__,template_folder='web/src')
@app.route('/')
def home():
    result = api_request(URLS[0])
    data = scrap_falabella(result)
    
    return render_template("index.html",data=data)


def run():
    app.run(host='0.0.0.0', port=81,debug=True)

run()