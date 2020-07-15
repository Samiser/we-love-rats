from flask import Flask, render_template
app = Flask(__name__)
app.config['SERVER_NAME'] = 'xn--qei6438m.ws'

@app.route("/")
def hello():
    phrase = "try putting an emoji as the subdomain 😄"
    return render_template('index.html', phrase=phrase)

@app.route("/", subdomain='<sub>')
def hello_sub(sub):
    phrase = ''
    if sub[:4] == 'xn--':
        phrase = sub[4:].encode().decode('punycode') + "❤🐀"
    else:
        phrase = "u need to use an emoji in the subdomain 😊"
    return render_template('index.html', phrase=phrase)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
