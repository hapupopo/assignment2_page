from flask import Flask, render_template

app = Flask(__name__)
server = app.server

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/details")
def detail():
    return render_template('portfolio_details.html')

if __name__ == '__main__':
    app.run()
