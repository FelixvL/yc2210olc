from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello_world():
    getal = 0
    getal += 1
    return "<p>Hello, World!"+str(getal)+"</p>"

@app.route("/tweede/<variabele>")
def hello_world2(variabele):
    return "<p>Hello, World!"+str(variabele)+"</p>"