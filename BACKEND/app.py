from flask import *  
from scraper import scraper
from summarizer import summarizer

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/with_url", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')

        try:
            article_title, text = scraper(url)
            summary = summarizer(text)
            return render_template("with_url.html", article_title = article_title, summary = summary)
        
        except TypeError():
            print('Invalid url entered')

    else: 
        return render_template("with_url.html")
    
    
@app.route("/with_text", methods=['GET', 'POST'])
def with_text():
    if request.method == 'POST':
        text = request.form.get('textarea')
        summary = summarizer(text)
        return render_template("with_text.html", summary = summary)

    else: 
        return render_template("with_text.html")

if __name__ == "__main__":
    app.run(debug = True)