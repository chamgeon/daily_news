from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

@app.route('/')
def homepage():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)